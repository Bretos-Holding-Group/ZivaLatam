# ZivaID R00-W01 — Intake QA Checklist v0.1

**Status:** Draft — controlled implementation package

## A. Participant integrity

- [ ] Participant ID is unique.
- [ ] Existing participant match was checked.
- [ ] Recruitment source is recorded.
- [ ] Primary segment was assigned without reference to hypothesis outcome.

## B. Protocol integrity

- [ ] `R00-W01` recorded.
- [ ] Exact instrument version recorded.
- [ ] Exact concept version recorded when applicable.
- [ ] Discovery occurred before concept exposure.
- [ ] Any deviation has a `deviation_id`.
- [ ] Instrument mismatch results in quarantine.

## C. Privacy integrity

- [ ] No unnecessary sensitive personal data is in the analytical record.
- [ ] No identity-document image is stored in the evidence register.
- [ ] No password/authentication code is stored.
- [ ] No financial-account or migration-case data is stored.
- [ ] Follow-up contact information, if any, remains outside the evidence register.

## D. Evidence integrity

- [ ] Evidence is tied to a concrete participant interaction.
- [ ] Source summary is separated from interpretation.
- [ ] Concrete experience is distinguished from hypothetical reaction.
- [ ] Contradictory evidence is preserved.
- [ ] Behavioral signal is not inferred beyond what actually occurred.

## E. Classification integrity

- [ ] Evidence type is assigned.
- [ ] Evidence strength is assigned.
- [ ] Frequency is not guessed.
- [ ] Severity is not guessed.
- [ ] `unknown` is used when information is unavailable.
- [ ] Hypothesis mapping has an explicit rationale.

## F. Disposition

### Usable

All critical checks pass.

### Quarantine

One or more critical checks require resolution. Do not count toward hypothesis thresholds.

### Excluded

Evidence cannot be used. Preserve the audit reason.

## G. Reviewer sign-off

- Intake reviewer:
- Review timestamp:
- Record IDs reviewed:
- Disposition:
- Notes:

A reviewer must not approve a record merely because it supports a desired hypothesis.
