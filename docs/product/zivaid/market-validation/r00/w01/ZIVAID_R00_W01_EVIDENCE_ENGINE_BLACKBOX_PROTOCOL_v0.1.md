# ZivaID R00 — Evidence Validation Engine Black-Box Verification Protocol v0.1

**Status:** Draft — controlled verification artifact
**Scope:** Post-merge operational verification of the deterministic Evidence Validation Engine
**Base implementation:** `7c9ff1ac1faf6d9c3b648bc7dfdfbf8a9e6fcf49`

## 1. Objective

Verify externally observable behavior of the merged Evidence Validation Engine without adding any synthetic record to the real W01 Evidence Register.

The black-box test is independent of the engine's internal unit-test assertions. It evaluates inputs, outputs, invariants and isolation behavior.

## 2. Test isolation

All test records MUST use the namespace `BBX-R00-###` and must never use production identifiers such as `P-###` or `EVID-R00-###`.

The black-box dataset is test-only. It must not be copied into the campaign evidence register, hypothesis counts, participant counts, coverage ledger or commercial results.

## 3. Required scenarios

### BBX-001 — Valid record
Expected: `USABLE`.

The input must contain valid identifiers, the frozen wave/instrument, valid provenance, valid protocol order, no prohibited sensitive data, no duplicate condition, and a complete evidence classification.

### BBX-002 — Missing required identifier
Expected: `QUARANTINE` or `EXCLUDED` according to the engine's implemented rule disposition.

The test verifies that a structurally incomplete record cannot become `USABLE`.

### BBX-003 — Invalid instrument version
Expected: not `USABLE`.

The input uses an instrument version different from the frozen W01 instrument.

### BBX-004 — Unknown discovery/concept sequence
Expected: `QUARANTINE`.

The engine must prevent uncertain protocol sequence from being treated as valid discovery evidence.

### BBX-005 — Privacy violation
Expected: `QUARANTINE` or `EXCLUDED` according to the implemented rule.

The test uses a synthetic marker representing prohibited sensitive data. The marker is not a real person's data.

### BBX-006 — Duplicate/independence concern
Expected: not `USABLE` when the duplicate condition is material and unresolved.

### BBX-007 — Contradictory evidence
Expected: admissibility remains independent of whether the evidence supports or contradicts a hypothesis.

The test verifies that contradiction does not itself cause automatic exclusion.

### BBX-008 — Unknown classification value
Expected: the engine must not silently convert `unknown` to `no`, and must follow the documented disposition rule.

### BBX-009 — Determinism
Run the exact same input and ruleset at least twice.

Expected: identical decision, rule results and ruleset/version identity.

### BBX-010 — Production-register isolation
Verify that none of BBX-001 through BBX-009 creates or modifies a real `EVID-R00-###` record, participant count, hypothesis count or campaign dataset.

## 4. Acceptance criteria

The black-box verification passes only if:

1. every required scenario produces the expected disposition class;
2. no invalid scenario becomes `USABLE`;
3. contradiction is not treated as invalidity by itself;
4. deterministic replay produces the same decision;
5. the validation result contains traceable engine/ruleset/version identity;
6. test identifiers remain outside production namespaces;
7. no test data enters the W01 Evidence Register;
8. failures are documented rather than manually overridden.

## 5. Evidence package

The verification package must contain:

- scenario manifest;
- input fixture manifest;
- observed outputs;
- expected outputs;
- pass/fail result per scenario;
- deterministic replay result;
- production-isolation check;
- execution timestamp;
- tested commit SHA;
- engine version;
- ruleset version;
- final verification decision.

## 6. Release gate

`BLACKBOX_PASS` is required before W01 real-data collection can be considered eligible for activation.

A black-box pass does not itself approve the market hypotheses or the product. It only verifies the operational evidence-admission boundary.
