import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "zivaid"))

from r00_evidence_validation_engine import ENGINE_VERSION, RULESET_ID, validate


def valid_record():
    return {
        "evidence_id": "BBX-R00-001",
        "participant_id": "BBX-P-001",
        "wave_id": "R00-W01",
        "protocol_version": "R00-v0.2",
        "instrument_id": "R00-INSTR-v0.2",
        "concept_id": "",
        "researcher_id": "BBX-R-001",
        "channel": "street",
        "segment_primary": "migrant",
        "recruitment_source": "synthetic-test",
        "discovery_before_concept": "yes",
        "evidence_type": "direct_experience",
        "problem_present": "yes",
        "evidence_strength": "strong",
        "frequency": "4-5",
        "severity": "4",
        "consequence": "time",
        "behavioral_signal": "none",
        "contradiction": "no",
        "source_summary": "Synthetic black-box observation only.",
        "researcher_interpretation": "Synthetic test fixture.",
        "hypotheses": ["H-BBX-001"],
        "status": "usable",
        "created_at": "2026-08-17T00:00:00+00:00",
        "updated_at": "2026-08-17T00:00:00+00:00",
    }


class TestR00EvidenceEngineBlackBox(unittest.TestCase):
    def assert_decision(self, record, expected):
        result = validate(record, now="2026-08-17T00:00:00+00:00")
        self.assertEqual(result["final_disposition"], expected)
        self.assertEqual(result["ruleset_id"], RULESET_ID)
        self.assertEqual(result["engine_version"], ENGINE_VERSION)
        self.assertTrue(result["validation_id"].startswith("VAL-R00-"))
        return result

    def test_001_valid_record_is_usable(self):
        result = self.assert_decision(valid_record(), "USABLE")
        self.assertTrue(result["counts_for_hypotheses"])
        self.assertFalse(result["review_required"])

    def test_002_missing_required_identifier_is_not_usable(self):
        record = valid_record()
        del record["evidence_id"]
        result = self.assert_decision(record, "QUARANTINE")
        self.assertFalse(result["counts_for_hypotheses"])

    def test_003_invalid_instrument_is_not_usable(self):
        record = valid_record()
        record["instrument_id"] = "R00-INSTR-v0.1"
        self.assert_decision(record, "QUARANTINE")

    def test_004_unknown_sequence_is_quarantined(self):
        record = valid_record()
        record["discovery_before_concept"] = "unknown"
        self.assert_decision(record, "QUARANTINE")

    def test_005_prohibited_sensitive_field_is_excluded(self):
        record = valid_record()
        record["passport_number"] = "SYNTHETIC-NOT-REAL"
        result = self.assert_decision(record, "EXCLUDED")
        self.assertFalse(result["counts_for_hypotheses"])

    def test_006_existing_participant_is_quarantined(self):
        record = valid_record()
        result = validate(record, existing_participant_ids=["BBX-P-001"], now="2026-08-17T00:00:00+00:00")
        self.assertEqual(result["final_disposition"], "QUARANTINE")

    def test_007_contradiction_is_not_invalidity(self):
        record = valid_record()
        record["contradiction"] = "yes"
        result = self.assert_decision(record, "USABLE")
        self.assertTrue(any(r["rule_id"] == "R00-EVID-004" and r["result"] == "pass" for r in result["rule_results"]))

    def test_008_unknown_controlled_value_is_quarantined(self):
        record = valid_record()
        record["frequency"] = "unknown-value"
        self.assert_decision(record, "QUARANTINE")

    def test_009_identical_input_is_deterministic(self):
        record = valid_record()
        first = validate(record, now="2026-08-17T00:00:00+00:00")
        second = validate(record, now="2026-08-17T00:00:00+00:00")
        self.assertEqual(first["final_disposition"], second["final_disposition"])
        self.assertEqual(first["rule_results"], second["rule_results"])
        self.assertEqual(first["input_fingerprint"], second["input_fingerprint"])
        self.assertEqual(first["validation_id"], second["validation_id"])
        self.assertEqual(first["ruleset_id"], second["ruleset_id"])
        self.assertEqual(first["engine_version"], second["engine_version"])

    def test_010_validation_does_not_mutate_or_create_production_records(self):
        record = valid_record()
        before = copy.deepcopy(record)
        result = validate(record, now="2026-08-17T00:00:00+00:00")
        self.assertEqual(record, before)
        self.assertTrue(result["evidence_id"].startswith("BBX-R00-"))
        self.assertTrue(result["validation_id"].startswith("VAL-R00-"))
        self.assertNotRegex(result["evidence_id"], r"^EVID-R00-")
        self.assertNotRegex(record["participant_id"], r"^P-")


if __name__ == "__main__":
    unittest.main()
