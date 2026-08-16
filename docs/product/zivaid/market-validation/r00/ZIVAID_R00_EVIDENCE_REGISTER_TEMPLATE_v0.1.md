# ZivaID R00 — Evidence Register Template v0.1

**Status:** Controlled template — pre-execution

## Purpose

Record research evidence without turning the repository into a database of personal information.

## Evidence ID format

Use `EVID-R00-###`.

## Required record

```text
Evidence ID:
Participant ID:
Date:
Channel:
Segment:
Context:
Hypothesis ID(s):
Evidence type: direct experience / observation / quote summary / organization workflow / behavioral signal
Problem present: yes / no / unclear
Frequency:
Severity:
Current workaround:
Concept reaction:
Strongest objection:
Behavioral commitment:
Researcher interpretation:
Contradictory evidence:
Source location:
Sensitivity classification:
Follow-up required: yes / no
```

## Evidence strength

### Strong

Recent concrete experience, repeated pattern across independent participants, observable behavior, organizational workflow evidence, pilot commitment or comparable high-intent behavior.

### Moderate

Specific participant statement or recurring qualitative pattern without behavioral commitment.

### Weak

Generic opinion, like, compliment, hypothetical statement or unprompted enthusiasm without a concrete problem.

## Evidence rules

1. One participant may generate multiple evidence records if separate claims are supported.
2. Do not aggregate contradictory evidence into a single positive record.
3. Do not remove negative evidence because it conflicts with the hypothesis.
4. Distinguish participant statement from researcher interpretation.
5. Do not store identity documents or unnecessary sensitive data.
6. Do not use participant names as evidence IDs.
7. If a quote is recorded, minimize identifying context and obtain any permission required by the approved research process.
8. Do not store raw direct-message threads, phone numbers, email addresses or contact lists in the evidence register.
9. `Source location` must identify the controlled evidence location without exposing personal contact information; use an internal evidence reference rather than a public social profile or private message URL where possible.
10. Participant IDs must be unique and pseudonymous. The mapping between a participant ID and optional follow-up contact must remain outside the evidence register.
11. If the same participant supports multiple claims, preserve the participant ID linkage but do not treat repeated statements from that participant as independent participants.
12. Organizational evidence must be anonymized unless the organization has explicitly approved attribution.

## Data minimization

The register is not the participant database. Store only the structured research attributes necessary to evaluate the hypotheses. Do not copy RUTs, passport numbers, medical details, financial account data, migration case numbers, prescriptions, authentication secrets or other sensitive source records.

If a future research need requires identifiable or sensitive data, execution must stop until a separately approved protocol establishes necessity, lawful handling, access control and retention rules.

## Analysis summary template

```text
Hypothesis:
Evidence supporting:
Evidence against:
Evidence strength:
Segments affected:
Key uncertainty:
Current status: supported / mixed / not supported / untested
Decision implication:
Sampling limitation:
Independence check:
```

## Independence check

For every material conclusion, the analyst must state whether the supporting evidence comes from:

- one participant;
- multiple independent participants;
- multiple channels;
- multiple segments;
- one or more independent organizations.

Repeated statements from the same participant, copied social comments, referrals from the same recruitment source and duplicated reports of the same event must not be counted as independent corroboration.

## Final R00 evidence standard

A market conclusion must be traceable from conclusion → hypothesis → evidence IDs → research method.

A conclusion that cannot be traced to evidence is not a certified R00 finding.
