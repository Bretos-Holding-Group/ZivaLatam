# ZivaID R00 — Evidence Validation Engine Test Matrix v0.1

**Status:** Draft — implementation gate

## Purpose

Define deterministic acceptance tests for the Evidence Validation Engine before it can be declared operational.

| Test | Input condition | Expected disposition | Hypothesis count |
|---|---|---|---|
| EV-001 | Complete valid W01 record | USABLE | Yes |
| EV-002 | Missing evidence ID | QUARANTINE | No |
| EV-003 | Duplicate evidence ID | EXCLUDED | No |
| EV-004 | Wrong wave | QUARANTINE | No |
| EV-005 | Wrong instrument version | QUARANTINE | No |
| EV-006 | Discovery/concept order unknown | QUARANTINE | No |
| EV-007 | Prohibited sensitive data | EXCLUDED | No |
| EV-008 | Possible participant duplicate | QUARANTINE | No |
| EV-009 | Hypothetical answer presented as experience | QUARANTINE | No |
| EV-010 | Material contradiction preserved | USABLE | Yes |
| EV-011 | Unknown frequency with otherwise valid record | USABLE | Yes |
| EV-012 | Unresolved material deviation | QUARANTINE | No |
| EV-013 | Fabricated/unverifiable interaction | EXCLUDED | No |
| EV-014 | Multiple evidence units from one participant | USABLE | Yes, but participant-independent count unchanged |
| EV-015 | Corrected record | New validation ID; prior decision retained | Per new disposition |

## Required assertions

Each automated test must assert:

- final disposition;
- failed/passed rule IDs;
- `counts_for_hypotheses`;
- `review_required`;
- deterministic output for identical input and ruleset;
- no mutation of the original input record;
- validation record contains a reproducible input fingerprint.

## Release gate

The engine cannot be marked operational until all tests pass and the test result is recorded against a specific engine and ruleset version.
