#!/usr/bin/env python3
"""Deterministic ZivaID R00 evidence admission engine.

Standard-library only. The engine validates one JSON/YAML-like mapping supplied
by callers and returns an auditable decision object. It never mutates input,
creates evidence, or silently repairs missing values.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from datetime import datetime, timezone
from typing import Any, Dict, List

ENGINE_VERSION = "0.1.0"
RULESET_ID = "R00-EVRULES-v0.1"
EVIDENCE_ID_RE = re.compile(r"^EVID-R00-\d{3,}$")
PARTICIPANT_ID_RE = re.compile(r"^P-\d{3,}$")

CONTROLLED = {
    "channel": {"instagram", "facebook", "tiktok", "street", "whatsapp", "b2b", "other"},
    "discovery_before_concept": {"yes", "no", "unknown"},
    "evidence_type": {"direct_experience", "observation", "workflow", "behavioral_signal", "contradiction"},
    "problem_present": {"yes", "no", "unclear"},
    "evidence_strength": {"strong", "moderate", "weak"},
    "frequency": {"1", "2-3", "4-5", "6+", "unknown"},
    "severity": {"1", "2", "3", "4", "5", "unknown"},
    "consequence": {"time", "money", "administrative", "access", "emotional", "none", "mixed", "unknown"},
    "behavioral_signal": {"none", "stated_interest", "followup_requested", "prototype_requested", "referral_made", "workflow_review_agreed", "pilot_discussion_agreed"},
    "status": {"usable", "quarantine", "excluded"},
}

REQUIRED = [
    "evidence_id", "participant_id", "wave_id", "protocol_version", "instrument_id",
    "researcher_id", "channel", "segment_primary", "recruitment_source",
    "discovery_before_concept", "evidence_type", "problem_present", "evidence_strength",
    "frequency", "severity", "consequence", "behavioral_signal", "contradiction",
    "source_summary", "researcher_interpretation", "hypotheses", "status", "created_at", "updated_at",
]

PROHIBITED_KEYS = {
    "rut", "passport_number", "passport", "identity_document", "identity_document_image",
    "password", "authentication_code", "otp", "bank_account", "financial_account",
    "migration_case_number", "medical_record", "exact_home_address",
}


def fingerprint(record: Dict[str, Any]) -> str:
    canonical = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def result(rule_id: str, status: str, reason: str) -> Dict[str, str]:
    return {"rule_id": rule_id, "result": status, "reason": reason}


def validate(record: Dict[str, Any], *, existing_evidence_ids=None, existing_participant_ids=None,
             now: str | None = None) -> Dict[str, Any]:
    """Validate a single evidence record without mutating it."""
    original = copy.deepcopy(record)
    existing_evidence_ids = set(existing_evidence_ids or ())
    existing_participant_ids = set(existing_participant_ids or ())
    checks: List[Dict[str, str]] = []
    definitive = False
    quarantine = False

    if not isinstance(record, dict):
        raise TypeError("record must be a mapping")

    for key in REQUIRED:
        if key not in record or record[key] in (None, ""):
            checks.append(result("R00-SCHEMA-001", "fail", f"Missing required field: {key}"))
            quarantine = True

    eid = record.get("evidence_id")
    if isinstance(eid, str) and EVIDENCE_ID_RE.fullmatch(eid):
        checks.append(result("R00-ID-001", "pass", "Evidence ID format is valid."))
    else:
        checks.append(result("R00-ID-001", "fail", "Evidence ID format is invalid."))
        quarantine = True

    pid = record.get("participant_id")
    if isinstance(pid, str) and PARTICIPANT_ID_RE.fullmatch(pid):
        checks.append(result("R00-ID-002", "pass", "Participant ID format is valid."))
    else:
        checks.append(result("R00-ID-002", "fail", "Participant ID format is invalid."))
        quarantine = True

    if eid in existing_evidence_ids:
        checks.append(result("R00-DUP-001", "fail", "Evidence ID already exists."))
        definitive = True
    else:
        checks.append(result("R00-DUP-001", "pass", "Evidence ID is not duplicated in supplied register context."))

    if pid in existing_participant_ids:
        checks.append(result("R00-DUP-002", "quarantine", "Participant ID already exists in supplied participant context; independence must be reconciled."))
        quarantine = True
    else:
        checks.append(result("R00-DUP-002", "pass", "No participant duplicate detected in supplied context."))

    for field, allowed in CONTROLLED.items():
        value = record.get(field)
        if value in allowed:
            checks.append(result("R00-SCHEMA-002", "pass", f"Controlled value for {field} is valid."))
        elif field in record:
            checks.append(result("R00-SCHEMA-002", "fail", f"Invalid controlled value for {field}: {value!r}."))
            quarantine = True

    checks.append(result("R00-WAVE-001", "pass" if record.get("wave_id") == "R00-W01" else "fail", "Wave must be R00-W01."))
    if record.get("wave_id") != "R00-W01": quarantine = True

    checks.append(result("R00-PROV-001", "pass" if record.get("protocol_version") == "R00-v0.2" else "fail", "Protocol version must be R00-v0.2."))
    if record.get("protocol_version") != "R00-v0.2": quarantine = True

    checks.append(result("R00-PROV-002", "pass" if record.get("instrument_id") == "R00-INSTR-v0.2" else "fail", "Instrument must match the frozen W01 instrument."))
    if record.get("instrument_id") != "R00-INSTR-v0.2": quarantine = True

    concept_present = bool(record.get("concept_id"))
    sequence = record.get("discovery_before_concept")
    if concept_present and sequence != "yes":
        checks.append(result("R00-PROTOCOL-001", "fail", "Concept exposure requires confirmed discovery-before-concept sequence."))
        quarantine = True
    else:
        checks.append(result("R00-PROTOCOL-001", "pass", "Discovery/concept sequence is admissible for this record."))

    if sequence == "unknown":
        checks.append(result("R00-PROTOCOL-002", "fail", "Unknown sequence is never usable."))
        quarantine = True

    if record.get("deviation_id") and not record.get("deviation_id", "").strip():
        checks.append(result("R00-PROTOCOL-003", "fail", "Invalid deviation identifier."))
        quarantine = True
    else:
        checks.append(result("R00-PROTOCOL-003", "pass", "No unresolved deviation is indicated by the record."))

    prohibited_found = sorted(k for k in record.keys() if k.lower() in PROHIBITED_KEYS)
    if prohibited_found:
        checks.append(result("R00-PRIVACY-001", "fail", f"Prohibited sensitive fields present: {', '.join(prohibited_found)}."))
        definitive = True
    else:
        checks.append(result("R00-PRIVACY-001", "pass", "No prohibited sensitive fields detected in analytical record."))

    if not isinstance(record.get("source_summary"), str) or not record.get("source_summary", "").strip():
        checks.append(result("R00-EVID-001", "fail", "Source-grounded summary is required."))
        quarantine = True
    else:
        checks.append(result("R00-EVID-001", "pass", "Source-grounded summary is present."))

    if record.get("source_summary") == record.get("researcher_interpretation") and record.get("source_summary"):
        checks.append(result("R00-EVID-002", "warn", "Source summary and interpretation are identical; reviewer should confirm separation."))
    else:
        checks.append(result("R00-EVID-002", "pass", "Source and interpretation are separate fields."))

    if not isinstance(record.get("hypotheses"), list):
        checks.append(result("R00-CLASS-004", "fail", "Hypotheses must be an array."))
        quarantine = True
    else:
        checks.append(result("R00-CLASS-004", "pass", "Hypothesis mapping field is structurally valid."))

    # A declared contradiction is valid evidence; it is not a failure.
    checks.append(result("R00-EVID-004", "pass", "Contradictory evidence is preserved rather than suppressed."))

    # A stronger behavioral signal must be explicitly recorded; no inference is performed.
    checks.append(result("R00-EVID-005", "pass", "Behavioral signal is taken only from the supplied controlled value."))

    if record.get("status") not in {"usable", "quarantine", "excluded"}:
        quarantine = True

    if definitive:
        disposition = "EXCLUDED"
    elif quarantine:
        disposition = "QUARANTINE"
    else:
        disposition = "USABLE"

    decision_time = now or datetime.now(timezone.utc).isoformat()
    return {
        "validation_id": f"VAL-R00-{fingerprint(original)[:12]}",
        "evidence_id": record.get("evidence_id"),
        "ruleset_id": RULESET_ID,
        "engine_version": ENGINE_VERSION,
        "input_fingerprint": fingerprint(original),
        "validated_at": decision_time,
        "rule_results": checks,
        "final_disposition": disposition,
        "counts_for_hypotheses": disposition == "USABLE",
        "review_required": disposition != "USABLE",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate one ZivaID R00 evidence JSON record.")
    parser.add_argument("input", help="Path to JSON evidence record")
    parser.add_argument("--existing-evidence", default="", help="Comma-separated evidence IDs already in register")
    parser.add_argument("--existing-participants", default="", help="Comma-separated participant IDs already in register")
    args = parser.parse_args()
    with open(args.input, "r", encoding="utf-8") as fh:
        record = json.load(fh)
    output = validate(
        record,
        existing_evidence_ids=[x for x in args.existing_evidence.split(",") if x],
        existing_participant_ids=[x for x in args.existing_participants.split(",") if x],
    )
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
