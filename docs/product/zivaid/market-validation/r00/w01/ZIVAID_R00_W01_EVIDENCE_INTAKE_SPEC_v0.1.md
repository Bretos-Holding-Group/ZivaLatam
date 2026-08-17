# ZivaID R00-W01 — Evidence Intake Specification v0.1

**Status:** Draft — controlled implementation package
**Parent:** R00 v0.2 + R00-W01 Execution Package v0.1
**Purpose:** Define the canonical path from a real research interaction to admissible R00 evidence.

## 1. Core rule

No participant record becomes research evidence merely because an interviewer created a note. Every record must pass identity, provenance, protocol, privacy, sequence and quality checks before it can enter the Evidence Register.

```text
Field interaction
  ↓
P-### participant record
  ↓
Raw research record
  ↓
Intake validation
  ↓
Privacy / sensitive-data check
  ↓
Protocol + instrument verification
  ↓
Duplicate / provenance check
  ↓
Evidence extraction
  ↓
EVID-R00-###
  ↓
QA state
  ├─ usable
  ├─ quarantine
  └─ excluded
  ↓
Evidence Register
  ↓
Hypothesis Mapping
```

## 2. Required identifiers

Every W01 interaction must have:

- `wave_id = R00-W01`
- `instrument_id = R00-INSTR-v0.2`
- `concept_id = CONCEPT-R00-v0.2` when concept exposure occurred
- unique `participant_id = P-###`
- unique `evidence_id = EVID-R00-###` for each material evidence unit
- `protocol_version`
- `record_created_at`
- `researcher_id`
- `channel`
- `segment_primary`

If any required identifier is unavailable, the record cannot be marked `usable`.

## 3. Participant record boundary

`P-###` is a pseudonymous research identifier. The research evidence dataset must not become a contact database.

Optional follow-up contact information must remain outside the evidence register and be referenced only by a separate controlled follow-up ID when necessary.

Do not store RUTs, passport numbers, identity-document images, passwords, authentication codes, migration case numbers, financial account numbers, medical records or exact home addresses.

## 4. Raw record vs evidence unit

A raw record preserves what was collected from the interaction.

An evidence unit captures one analytically relevant finding from that record.

One participant may generate multiple evidence units. Those units must not be treated as multiple independent participants.

Example:

`P-017 → EVID-R00-041, EVID-R00-042`

Both remain attributed to `P-017` for independence analysis.

## 5. Minimum intake schema

| Field | Required | Rule |
|---|---|---|
| evidence_id | yes | unique `EVID-R00-###` |
| participant_id | yes | unique `P-###` |
| wave_id | yes | `R00-W01` |
| instrument_id | yes | exact frozen instrument |
| concept_id | conditional | required if concept exposed |
| protocol_version | yes | exact protocol version |
| researcher_id | yes | controlled researcher identifier |
| channel | yes | controlled vocabulary |
| segment_primary | yes | assigned before analysis |
| discovery_before_concept | yes | `yes/no` |
| evidence_type | yes | controlled vocabulary |
| problem_present | yes | `yes/no/unclear` |
| evidence_strength | yes | `strong/moderate/weak` |
| contradiction | yes | `yes/no` |
| source_summary | yes | neutral summary of participant evidence |
| researcher_interpretation | yes | separate from source summary |
| severity | conditional | `1–5/unknown` when applicable |
| frequency | conditional | controlled vocabulary |
| consequence | conditional | controlled vocabulary |
| behavioral_signal | conditional | controlled vocabulary |
| status | yes | `usable/quarantine/excluded` |
| exclusion_reason | conditional | required for quarantine/excluded |
| deviation_id | conditional | required when protocol deviated |

## 6. Intake sequence

### Step 1 — Create participant ID

Assign the next unused `P-###`. Never recycle an ID.

### Step 2 — Register interaction metadata

Record channel, date/time band, segment, researcher, recruitment source and protocol/instrument version.

### Step 3 — Run privacy check

Remove unnecessary sensitive information before analytical evidence is created. If sensitive material is embedded in the raw record, quarantine the record and document the issue without reproducing the sensitive content.

### Step 4 — Verify protocol sequence

Confirm discovery occurred before concept exposure. If the sequence cannot be established, quarantine.

### Step 5 — Check duplication

Search for an existing participant match using the controlled follow-up/duplicate procedure. Never create a second participant solely because the person arrived through another channel.

### Step 6 — Extract evidence

Create one `EVID-R00-###` for each material finding. Preserve both supporting and contradictory findings.

### Step 7 — Classify

Assign evidence type, strength, problem status, severity/frequency where applicable, and behavioral signal.

### Step 8 — Separate observation from interpretation

`source_summary` must state what the participant reported or what was directly observed. `researcher_interpretation` may explain analytical significance but cannot rewrite the source summary.

### Step 9 — QA state

Apply `usable`, `quarantine` or `excluded` according to the QA gate.

### Step 10 — Hypothesis mapping

Only `usable` evidence may support a hypothesis classification. Quarantined evidence may be listed as pending but must not count toward thresholds.

## 7. QA gate

### Usable

All required identifiers exist; provenance is adequate; sequence is valid; privacy boundary is respected; participant independence is known; source and interpretation are separated; no unresolved critical deviation exists.

### Quarantine

Potentially useful but one or more critical conditions require resolution.

Examples:

- instrument version unknown;
- discovery/concept order uncertain;
- possible duplicate participant;
- sensitive information requires removal;
- provenance incomplete;
- unresolved protocol deviation.

### Excluded

The record cannot be used as evidence.

Examples:

- fabricated or unverifiable interaction;
- duplicate evidence copy;
- material protocol violation that invalidates the finding;
- prohibited source data that cannot be safely remediated;
- evidence generated outside the authorized wave.

Excluded records remain auditable with a reason.

## 8. Hypothesis mapping rule

An evidence unit may map to zero, one or multiple hypotheses. Mapping must explain why.

Example:

`EVID-R00-041 → H-001, H-002`

because the same concrete incident may demonstrate repetition and a measurable consequence.

Do not map evidence to a hypothesis merely because it contains related keywords.

## 9. Contradiction rule

If a participant reports that repeated verification is easy, acceptable or absent, record that as evidence where relevant. Do not suppress it because it conflicts with H-001.

Contradictory evidence receives its own `EVID-R00-###` identifier when analytically material.

## 10. Behavioral evidence rule

Stated intent and observed/committed action must remain separate.

Allowed values:

- `none`
- `stated_interest`
- `followup_requested`
- `prototype_requested`
- `referral_made`
- `workflow_review_agreed`
- `pilot_discussion_agreed`

A stronger behavioral category cannot be inferred from a weaker one.

## 11. Correction protocol

Corrections never overwrite the evidentiary history silently.

When a classification is corrected:

1. preserve the original value;
2. record correction timestamp;
3. record correction reason;
4. record researcher/reviewer ID;
5. record affected evidence ID;
6. state whether the correction changes hypothesis counting.

## 12. Closure conditions for W01

Before W01 can be closed:

- all participant IDs are reconciled;
- all evidence IDs are unique;
- all records have QA status;
- all quarantined records have disposition;
- all deviations are resolved or explicitly accepted;
- all sensitive-data incidents are resolved;
- hypothesis mappings are traceable;
- contradictory evidence is included;
- coverage ledger reconciles with participant records;
- final dataset hash/package identity is recorded;
- results report references the frozen W01 protocol and instrument versions.

## 13. Prohibited shortcuts

Never:

- manually invent an evidence ID to fill a sequence gap;
- turn a social-media like into evidence;
- convert a hypothetical answer into a concrete incident;
- count repeated statements by one participant as independent corroboration;
- change a participant's segment after seeing hypothesis results without an amendment;
- delete negative evidence because it weakens a hypothesis;
- overwrite a prior evidence classification without an audit trail;
- import evidence from another wave without explicit amendment and provenance.

## 14. Admission principle

The Evidence Register is the canonical analytical boundary for R00. Data outside the register may exist as operational material, but it cannot support a certified R00 conclusion until it passes the intake and QA process defined here.
