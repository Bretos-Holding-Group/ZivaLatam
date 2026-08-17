# R00 Evidence Engine — Black-Box Fixture Manifest v0.1

**Status:** Draft — test-only

All fixtures are synthetic and must remain outside the production Evidence Register.

| Fixture | Purpose | Expected class | Production namespace allowed? |
|---|---|---|---|
| BBX-001 | valid evidence-shaped record | USABLE | No |
| BBX-002 | missing required identifier | non-USABLE | No |
| BBX-003 | invalid instrument | non-USABLE | No |
| BBX-004 | unknown protocol sequence | QUARANTINE | No |
| BBX-005 | prohibited sensitive-data marker | non-USABLE | No |
| BBX-006 | duplicate concern | non-USABLE | No |
| BBX-007 | contradiction | admissibility independent of polarity | No |
| BBX-008 | unknown classification | rule-governed | No |
| BBX-009 | deterministic replay | identical output | No |
| BBX-010 | production isolation | zero production writes | No |

No fixture contains real personal information, real participant identifiers, real evidence identifiers, or real campaign observations.
