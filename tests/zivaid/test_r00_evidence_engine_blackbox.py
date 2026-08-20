import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "zivaid"))

from r00_evidence_validation_engine import ENGINE_VERSION, RULESET_ID, validate


# Reserved synthetic IDs: valid engine shape, never written to any register.
TEST_EVIDENCE_ID = "EVID-R00-900001"
TEST_PARTICIPANT_ID = "P-900001"


def valid_record():
    return {
        "evidence_id": TEST_EVIDENCE_ID, "participant_id": TEST_PARTICIPANT_ID, "wave_id": "R00-W01",
        "protocol_version": "R00-v0.2", "instrument_id": "R00-INSTR-v0.2", "concept_id": "",
        "researcher_id": "R-900001", "channel": "street", "segment_primary": "migrant",
        "recruitment_source": "synthetic-test", "discovery_before_concept": "yes",
        "evidence_type": "direct_experience", "problem_present": "yes", "evidence_strength": "strong",
        "frequency": "4-5", "severity": "4", "consequence": "time", "behavioral_signal": "none",
        "contradiction": "no", "source_summary": "Synthetic black-box observation only.",
        "researcher_interpretation": "Synthetic test fixture.", "hypotheses": ["H-BBX-001"],
        "status": "usable", "created_at": "2026-08-17T00:00:00+00:00", "updated_at": "2026-08-17T00:00:00+00:00",
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
        result = validate(record, existing_participant_ids=[TEST_PARTICIPANT_ID], now="2026-08-17T00:00:00+00:00")
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
        for key in ("final_disposition", "rule_results", "input_fingerprint", "validation_id", "ruleset_id", "engine_version"):
            self.assertEqual(first[key], second[key])

    def test_010_validation_does_not_mutate_or_create_production_records(self):
        record = valid_record()
        before = copy.deepcopy(record)
        result = validate(record, now="2026-08-17T00:00:00+00:00")
        self.assertEqual(record, before)
        self.assertEqual(result["evidence_id"], TEST_EVIDENCE_ID)
        self.assertEqual(record["participant_id"], TEST_PARTICIPANT_ID)
        self.assertTrue(result["validation_id"].startswith("VAL-R00-"))


if __name__ == "__main__":
    unittest.main()
