# ZivaID R00 — Data Dictionary and Evidence QA v0.2

**Status:** Controlled template — pre-execution
**Purpose:** Keep research data consistent enough for analysis without creating a personal-data repository.

## 1. Core entities

### Participant

`P-###` — pseudonymous research participant. One person must retain one ID across the R00 wave.

### Evidence

`EVID-R00-###` — one traceable evidence record supporting or contradicting one or more hypotheses.

### Organization

`ORG-R00-###` — pseudonymous organization reference for B2B research. Never use the organization name unless attribution has been explicitly approved.

## 2. Controlled fields

| Field | Allowed values / rule |
|---|---|
| channel | instagram / facebook / tiktok / street / whatsapp / b2b / other |
| problem_present | yes / no / unclear |
| evidence_type | direct_experience / observation / quote_summary / workflow / behavioral_signal |
| evidence_strength | strong / moderate / weak |
| frequency | 1 / 2-3 / 4-5 / 6+ / unknown |
| severity | 1–5 / unknown |
| consequence | time / money / administrative / access / emotional / none / mixed / unknown |
| concept_exposure | no / yes |
| concept_reaction | negative / neutral / positive / mixed / unclear |
| behavioral_commitment | none / followup / prototype / referral / workflow_review / pilot_discussion |
| contradiction | yes / no |
| record_status | usable / quarantine / excluded |

## 3. Separation rules

Never combine these fields:

- participant statement vs researcher interpretation;
- problem evidence vs solution reaction;
- stated intent vs behavioral action;
- social engagement vs research evidence;
- one participant's repeated reports vs independent participants;
- organization workflow evidence vs user preference evidence.

## 4. Quality states

### Usable

Provenance is clear, the interview sequence is valid, the record contains enough context and no prohibited source material is stored.

### Quarantine

Potentially useful but a quality problem must be resolved before analysis.

Examples: duplicate identity, uncertain sequence, unclear provenance, missing critical context.

### Excluded

Cannot be used as evidence.

Examples: fabricated entry, duplicate copy of another record, prohibited sensitive source record, or evidence generated after a material protocol violation.

Excluded records remain in an audit log with the reason; they are not silently deleted.

## 5. Severity scale

Use the participant's own consequence as the anchor:

1 — negligible inconvenience
2 — noticeable but easy to absorb
3 — meaningful additional effort, delay or frustration
4 — major delay, cost, failed step or substantial disruption
5 — severe consequence such as lost access/opportunity or repeated serious disruption

If the participant cannot reasonably rate severity, record `unknown` rather than guessing.

## 6. Evidence-strength rule

**Strong:** concrete recent incident, repeated pattern across independent participants, observable behavior, organizational workflow evidence or defined pilot/workflow commitment.

**Moderate:** specific participant experience or recurring qualitative pattern without strong behavioral evidence.

**Weak:** generic opinion, hypothetical answer, compliment, like, vague agreement or enthusiasm without a concrete problem.

## 7. Provenance requirement

Every material conclusion must trace:

`Conclusion → hypothesis → evidence IDs → participant/organization IDs → channel → protocol version`

If the chain breaks, the conclusion must be downgraded or excluded.

## 8. Privacy requirement

The dataset must not contain:

- RUTs;
- passport numbers;
- identity document images;
- medical records;
- financial account numbers;
- migration case numbers;
- passwords or authentication codes;
- exact home addresses;
- unnecessary names or contact details.

Optional follow-up contact data must remain in a separate mechanism and must never be copied into the evidence register.

## 9. Pre-analysis QA checklist

- [ ] Duplicate participants checked.
- [ ] Duplicate evidence checked.
- [ ] Channel recorded.
- [ ] Recruitment source recorded.
- [ ] Discovery/concept sequence checked.
- [ ] Contradictions preserved.
- [ ] Missing values preserved as unknown.
- [ ] Sensitive source material excluded.
- [ ] Segment assignment consistent.
- [ ] Protocol version recorded.
- [ ] Researcher interpretation separated from source observation.

## 10. Audit rule

No analyst may alter a source observation to make it fit a hypothesis. Corrections to transcription or classification must preserve the original record and explain the correction.
