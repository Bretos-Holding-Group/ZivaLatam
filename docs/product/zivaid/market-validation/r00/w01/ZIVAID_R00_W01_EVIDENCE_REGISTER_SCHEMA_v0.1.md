# ZivaID R00-W01 — Evidence Register Schema v0.1

**Status:** Draft — controlled implementation package
**Canonical role:** analytical register for admissible R00 evidence

## 1. Record format

Each evidence record must contain the following logical fields:

```yaml
evidence_id: EVID-R00-###
participant_id: P-###
wave_id: R00-W01
protocol_version: R00-v0.2
instrument_id: R00-INSTR-v0.2
concept_id: CONCEPT-R00-v0.2 # required only if exposed
researcher_id: R-###
channel: instagram|facebook|tiktok|street|whatsapp|b2b|other
segment_primary: <controlled segment>
recruitment_source: <controlled source>
discovery_before_concept: yes|no|unknown
evidence_type: direct_experience|observation|workflow|behavioral_signal|contradiction
problem_present: yes|no|unclear
evidence_strength: strong|moderate|weak
frequency: 1|2-3|4-5|6+|unknown
severity: 1|2|3|4|5|unknown
consequence: time|money|administrative|access|emotional|none|mixed|unknown
behavioral_signal: none|stated_interest|followup_requested|prototype_requested|referral_made|workflow_review_agreed|pilot_discussion_agreed
contradiction: yes|no
source_summary: <neutral source-grounded summary>
researcher_interpretation: <separate analytical interpretation>
hypotheses: [H-###]
deviation_id: <optional>
status: usable|quarantine|excluded
status_reason: <required when quarantine/excluded>
created_at: <timestamp>
updated_at: <timestamp>
```

## 2. Required invariants

- `evidence_id` is unique.
- `participant_id` is stable across channels.
- `wave_id` must equal `R00-W01` for W01 records.
- `instrument_id` must match the frozen W01 instrument.
- `concept_id` is present only when concept exposure occurred.
- `hypotheses` cannot contain a hypothesis unless the evidence-to-hypothesis rationale is documented.
- `status=usable` requires all mandatory fields and a passed QA gate.
- `status=quarantine` requires a reason.
- `status=excluded` requires a reason.
- `unknown` must never be silently converted to `no`.

## 3. Evidence independence

The register records evidence units, not independent observations. Analysis must calculate independence at participant or organization level as defined by the analysis plan.

## 4. Source/interpretation separation

`source_summary` is factual and source-grounded.

`researcher_interpretation` is analytical.

They must never be merged into one free-text field.

## 5. Version control

The register itself is versioned. A correction creates an auditable update rather than silently replacing history.

For final W01 closure, record:

- register version;
- final commit SHA;
- final dataset/package hash;
- number of records by status;
- number of participants;
- number of organizations;
- number of deviations;
- number of sensitive-data incidents.

## 6. Empty-state requirement

The initial W01 register is intentionally empty. An empty register is valid and preferable to placeholder or synthetic evidence.

No test record may be represented as a real participant.
