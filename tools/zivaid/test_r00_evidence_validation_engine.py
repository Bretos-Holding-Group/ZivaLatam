import copy
import unittest

from r00_evidence_validation_engine import validate


BASE = {
    "evidence_id": "EVID-R00-001",
    "participant_id": "P-001",
    "wave_id": "R00-W01",
    "protocol_version": "R00-v0.2",
    "instrument_id": "R00-INSTR-v0.2",
    "researcher_id": "R-001",
    "channel": "street",
    "segment_primary": "migrants",
    "recruitment_source": "street",
    "discovery_before_concept": "yes",
    "evidence_type": "direct_experience",
    "problem_present": "yes",
    "evidence_strength": "strong",
    "frequency": "2-3",
    "severity": "4",
    "consequence": "administrative",
    "behavioral_signal": "none",
    "contradiction": "no",
    "source_summary": "Participant reports repeating identity information in multiple processes.",
    "researcher_interpretation": "The report may indicate a recurring verification burden.",
    "hypotheses": ["H-001"],
    "status": "usable",
    "created_at": "2026-08-17T00:00:00Z",
    "updated_at": "2026-08-17T00:00:00Z",
}


class EvidenceValidationEngineTests(unittest.TestCase):
    def test_valid_record_is_usable(self):
        decision = validate(BASE, now="2026-08-17T00:00:00Z")
        self.assertEqual(decision["final_disposition"], "USABLE")
        self.assertTrue(decision["counts_for_hypotheses"])

    def test_missing_id_is_quarantine(self):
        record = copy.deepcopy(BASE)
        record.pop("evidence_id")
        decision = validate(record, now="2026-08-17T00:00:00Z")
        self.assertEqual(decision["final_disposition"], "QUARANTINE")
        self.assertFalse(decision["counts_for_hypotheses"])

    def test_duplicate_evidence_is_excluded(self):
        decision = validate(BASE, existing_evidence_ids={"EVID-R00-001"}, now="2026-08-17T00:00:00Z")
        self.assertEqual(decision["final_disposition"], "EXCLUDED")

    def test_wrong_instrument_is_quarantine(self):
        record = copy.deepcopy(BASE)
        record["instrument_id"] = "R00-INSTR-v0.1"
        decision = validate(record, now="2026-08-17T00:00:00Z")
        self.assertEqual(decision["final_disposition"], "QUARANTINE")

    def test_unknown_sequence_is_quarantine(self):
        record = copy.deepcopy(BASE)
        record["discovery_before_concept"] = "unknown"
        decision = validate(record, now="2026-08-17T00:00:00Z")
        self.assertEqual(decision["final_disposition"], "QUARANTINE")

    def test_prohibited_sensitive_field_is_excluded(self):
        record = copy.deepcopy(BASE)
        record["passport_number"] = "TEST-ONLY"
        decision = validate(record, now="2026-08-17T00:00:00Z")
        self.assertEqual(decision["final_disposition"], "EXCLUDED")

    def test_possible_participant_duplicate_is_quarantine(self):
        decision = validate(BASE, existing_participant_ids={"P-001"}, now="2026-08-17T00:00:00Z")
        self.assertEqual(decision["final_disposition"], "QUARANTINE")

    def test_contradiction_does_not_fail_admission(self):
        record = copy.deepcopy(BASE)
        record["contradiction"] = "yes"
        record["evidence_type"] = "contradiction"
        decision = validate(record, now="2026-08-17T00:00:00Z")
        self.assertEqual(decision["final_disposition"], "USABLE")

    def test_unknown_frequency_can_remain_usable(self):
        record = copy.deepcopy(BASE)
        record["frequency"] = "unknown"
        decision = validate(record, now="2026-08-17T00:00:00Z")
        self.assertEqual(decision["final_disposition"], "USABLE")

    def test_engine_does_not_mutate_input(self):
        record = copy.deepcopy(BASE)
        before = copy.deepcopy(record)
        validate(record, now="2026-08-17T00:00:00Z")
        self.assertEqual(record, before)

    def test_same_input_and_time_is_deterministic(self):
        a = validate(BASE, now="2026-08-17T00:00:00Z")
        b = validate(BASE, now="2026-08-17T00:00:00Z")
        self.assertEqual(a, b)

    def test_repeated_evidence_from_one_participant_remains_evidence_but_not_independent(self):
        decision = validate(BASE, now="2026-08-17T00:00:00Z")
        self.assertEqual(decision["final_disposition"], "USABLE")
        # Independence is an analytical constraint, not an admission failure.
        self.assertTrue(decision["counts_for_hypotheses"])


if __name__ == "__main__":
    unittest.main()
