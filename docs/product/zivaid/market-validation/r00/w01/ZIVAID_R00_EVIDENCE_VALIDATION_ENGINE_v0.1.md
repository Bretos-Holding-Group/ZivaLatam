# ZivaID R00 — Evidence Validation Engine v0.1

**Status:** Draft — implementation candidate; not operational until approved and merged
**Scope:** R00-W01 evidence admissibility and disposition
**Authority:** R00 v0.2 + approved W01 intake specification and evidence register schema

## 1. Purpose

Provide a deterministic, auditable gate that evaluates an evidence record and returns exactly one disposition:

- `USABLE`
- `QUARANTINE`
- `EXCLUDED`

The engine determines **admissibility**, not truth, market demand, statistical significance, or commercial success.

## 2. Non-negotiable properties

1. Same input + same ruleset version = same decision.
2. Every decision records the ruleset version, timestamp, input fingerprint, rule results, and final disposition.
3. The engine never silently repairs evidence.
4. Unknown values are not converted to negative values.
5. A quarantined record never counts toward hypothesis thresholds.
6. An excluded record never counts toward R00 conclusions.
7. The engine cannot invent participant IDs, evidence IDs, provenance, consent, sequence, or observations.
8. Human review may resolve quarantine but must create an auditable decision record.
9. Rule changes require a new ruleset version and revalidation; historical decisions remain immutable.

## 3. Decision model

```text
INPUT RECORD
   |
   +--> Schema validation
   +--> Identifier/provenance validation
   +--> Wave/instrument/concept validation
   +--> Protocol sequence validation
   +--> Privacy boundary validation
   +--> Duplicate/independence checks
   +--> Source/interpretation separation
   +--> Evidence classification validation
   +--> Deviation validation
   |
   v
RULE EVALUATION
   |
   +--> critical failure --------> EXCLUDED
   +--> unresolved critical ----- QUARANTINE
   +--> all mandatory gates pass -> USABLE
```

## 4. Rule severity

Each rule has one of three effects:

- `BLOCK`: a failure prevents `USABLE`; disposition is `EXCLUDED` when the failure is definitive, otherwise `QUARANTINE`.
- `QUARANTINE`: requires human resolution before the evidence can be usable.
- `WARN`: does not block usability but must be recorded.

The engine must not infer a disposition from a score. Disposition is rule-based.

## 5. Canonical ruleset v0.1

### Identity and schema

- `R00-ID-001`: `evidence_id` exists and matches `EVID-R00-###`.
- `R00-ID-002`: `participant_id` exists and matches `P-###`.
- `R00-ID-003`: evidence ID is unique within the register.
- `R00-ID-004`: participant ID is stable and is not reused for another person.
- `R00-SCHEMA-001`: all mandatory fields are present.
- `R00-SCHEMA-002`: enumerated fields contain only controlled values.

### Wave and provenance

- `R00-WAVE-001`: `wave_id == R00-W01`.
- `R00-PROV-001`: `protocol_version == R00-v0.2` for W01.
- `R00-PROV-002`: `instrument_id == R00-INSTR-v0.2`.
- `R00-PROV-003`: `concept_id` exists when and only when concept exposure occurred.
- `R00-PROV-004`: researcher and channel are recorded.

### Protocol sequence

- `R00-PROTOCOL-001`: discovery-before-concept is `yes` for records that include concept exposure.
- `R00-PROTOCOL-002`: `unknown` sequence is never usable.
- `R00-PROTOCOL-003`: an unresolved material deviation is not usable.

### Privacy

- `R00-PRIVACY-001`: prohibited sensitive data is absent from the analytical record.
- `R00-PRIVACY-002`: contact data remains outside the evidence register.
- `R00-PRIVACY-003`: identity documents, passwords, authentication codes and financial-account data are not admitted.

### Evidence integrity

- `R00-EVID-001`: `source_summary` is present and source-grounded.
- `R00-EVID-002`: `researcher_interpretation` is separate.
- `R00-EVID-003`: hypothetical reaction is not represented as a direct experience.
- `R00-EVID-004`: contradiction is preserved when material.
- `R00-EVID-005`: behavioral signal is supported by an actual recorded action or explicit statement at the corresponding level.

### Classification

- `R00-CLASS-001`: evidence type is controlled.
- `R00-CLASS-002`: strength is controlled.
- `R00-CLASS-003`: unknown frequency/severity remains unknown.
- `R00-CLASS-004`: hypothesis mapping has documented rationale.

### Duplicate and independence

- `R00-DUP-001`: exact evidence duplicate is rejected/excluded.
- `R00-DUP-002`: possible participant duplicate is quarantined.
- `R00-DUP-003`: multiple evidence units from one participant do not become independent observations.

## 6. Decision precedence

When multiple rules fail, the engine records all failures and applies this precedence:

1. definitive fabrication or impossible provenance → `EXCLUDED`;
2. prohibited/unremediable data → `EXCLUDED`;
3. unresolved identity/provenance/protocol/privacy issue → `QUARANTINE`;
4. duplicate evidence → `EXCLUDED`;
5. possible participant duplicate → `QUARANTINE`;
6. all mandatory gates pass → `USABLE`.

The engine must not hide lower-level failures simply because a higher-priority failure occurred.

## 7. Decision record

Every validation produces an immutable decision object logically equivalent to:

```yaml
validation_id: VAL-R00-####
evidence_id: EVID-R00-###
ruleset_id: R00-EVRULES-v0.1
input_fingerprint: <sha256>
validated_at: <timestamp>
engine_version: 0.1.0
rule_results:
  - rule_id: R00-ID-001
    result: pass|fail|not_applicable
    reason: <short reason>
final_disposition: usable|quarantine|excluded
counts_for_hypotheses: true|false
review_required: true|false
review_id: <optional>
```

## 8. Human resolution

Human review is allowed only for records in `QUARANTINE` or for explicit correction workflows. The reviewer cannot erase the original engine decision.

A review creates:

- `review_id`;
- reviewer ID;
- timestamp;
- original validation ID;
- decision `release_to_usable` or `exclude`;
- rationale;
- affected rules;
- whether hypothesis counts change.

## 9. Revalidation

A record may be revalidated after a correction, but the prior decision remains immutable. The new validation must reference the prior validation ID and the changed input fingerprint.

## 10. Test matrix requirement

Before this engine can be declared operational, automated tests must cover at minimum:

1. valid complete record → `USABLE`;
2. missing evidence ID → `QUARANTINE`;
3. duplicate evidence ID → `EXCLUDED`;
4. wrong wave → `QUARANTINE`;
5. wrong instrument version → `QUARANTINE`;
6. unknown discovery/concept order → `QUARANTINE`;
7. prohibited sensitive data → `EXCLUDED`;
8. possible participant duplicate → `QUARANTINE`;
9. hypothetical response presented as experience → `QUARANTINE`;
10. contradiction preserved → may remain `USABLE`;
11. valid record with unknown frequency → `USABLE`;
12. unresolved material deviation → `QUARANTINE`;
13. definitive fabricated/unverifiable interaction → `EXCLUDED`;
14. repeated evidence from same participant → `USABLE` but not independently countable;
15. correction → new validation ID, old decision retained.

## 11. Operational boundary

This engine does not:

- decide whether the market exists;
- determine product-market fit;
- determine willingness to pay;
- rewrite participant statements;
- generate evidence;
- infer missing facts;
- replace human judgment for unresolved quarantine cases.

It is the **admission control layer** between collected research material and the canonical Evidence Register.
