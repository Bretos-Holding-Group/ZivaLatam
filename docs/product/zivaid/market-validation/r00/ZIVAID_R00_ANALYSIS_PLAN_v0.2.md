# ZivaID R00 — Preregistered Analysis Plan v0.2

**Status:** Controlled amendment — pre-execution
**Parent baseline:** `ZIVAID_MARKET_VALIDATION_R00_v0.1.md`
**Purpose:** Freeze how evidence will be interpreted before controlled collection begins.

## 1. Core rule

The analysis plan is part of the experiment. Researchers must not choose thresholds, segment definitions, exclusions or success criteria after seeing the results.

R00 is exploratory research. No threshold in this document constitutes statistical significance, population prevalence, product-market fit or a commercial certification.

## 2. Evidence layers

Every material finding must be classified separately as:

1. **Problem evidence** — the participant experienced the underlying problem.
2. **Severity evidence** — the problem produced measurable or meaningful friction.
3. **Solution evidence** — the proposed ZivaID characteristics are attractive.
4. **Behavioral evidence** — the participant or organization takes or commits to an action.
5. **Market evidence** — the combined evidence justifies a subsequent commercial experiment.

Downstream evidence cannot repair a failed foundational problem finding.

## 3. Pre-registered hypothesis rules

### H-001 — Repeated verification

Classify **Supported** only if at least 15 independent participants provide a concrete recent example of repeated submission or verification, and the pattern appears in at least two recruitment channels or two materially different participant contexts.

Classify **Not supported** if at least 15 independent participants are probed adequately and fewer than 5 provide a concrete recent example, provided the sample is not dominated by one narrow context.

Otherwise use **Mixed** or **Untested**.

### H-002 — Meaningful cost

For participants reporting H-001, record severity on a 1–5 scale and the concrete consequence. Treat a median severity of 3 or higher plus at least 10 concrete consequence reports as sufficient evidence to classify the problem as materially consequential for the sampled participants. This does not establish population prevalence.

### H-003 — Minimum disclosure value

Require both: (a) a concrete disclosure concern from at least 10 independent participants before or during the concept test, and (b) at least 5 participants who independently identify a minimum-disclosure use case as useful. If concern appears only after the researcher introduces it, classify the finding as solution-induced rather than pre-existing problem evidence.

### H-004 — Reusable credentials

Treat as supported only when at least 10 independent participants or organizations identify a concrete recurring verification context where reuse would reduce meaningful work, and at least 5 show a behavioral signal stronger than generic enthusiasm. Separate user and organization evidence.

### H-005 — Trust barrier

Rank objections from spontaneous discovery separately from prompted concept-test objections. A barrier may be classified as material when it appears spontaneously in at least 10 independent records or is repeatedly identified as a top-two concern after concept exposure. Do not merge spontaneous and prompted counts.

### H-006 — Dominant use case

A use case is a candidate wedge when it has the highest observed concentration among independent participants and is supported by at least 10 concrete problem records across at least two channels. If no use case reaches this condition, report fragmentation rather than forcing a winner.

### H-007 — Organizational demand

Require at least 8 independent organizations or distinct organizational process owners for an exploratory organizational pattern. A stronger signal requires at least 3 organizations willing to continue to a workflow review or pilot discussion. No customer commitment is implied by an interview statement alone.

### H-008 — Willingness to test

Separate stated willingness from behavior. `Would try` is weak-to-moderate evidence. `Provides contact for follow-up`, `requests a prototype`, `introduces a relevant person`, or `agrees to a defined pilot conversation` is behavioral evidence. No percentage alone certifies demand.

### H-009 — Data control / sovereignty

Record spontaneous concerns separately from prompted concerns. Classify the requirement as material for the sampled group when at least 10 independent participants identify control, portability, secondary use, profiling, surveillance or access boundaries as a condition of trust.

### H-010 — Initial wedge vs broad vision

Compare specific use-case choices against generic interest in the broad identity concept. A narrow wedge is preferred when a concrete use case repeatedly produces stronger problem evidence and stronger behavioral intent than the broad proposition.

## 4. Independence rules

The unit of corroboration is the independent participant, organization or distinct process owner, not the number of statements. Multiple records from one participant do not increase independent sample size.

Copied comments, coordinated referrals from the same immediate group, duplicate reports of one event and repeated observations of the same organizational workflow are not independent corroboration.

## 5. Missingness and invalid records

A record is **usable** only when channel, participant ID, problem status and enough context to interpret the evidence are present.

Records with leading questions, fabricated responses, duplicate participants, unclear provenance or prohibited sensitive source material must be quarantined from analysis rather than silently deleted.

Missing answers remain missing. Do not convert `unknown` into `no`.

## 6. Segment analysis

Primary segment is assigned before analysis using the participant's declared context. Secondary attributes may be retained only when necessary.

Never reassign a participant to a segment because that makes a hypothesis stronger. Segment changes after collection require a traceable amendment.

## 7. Contradictory evidence

Every hypothesis table must contain:

- supporting evidence IDs;
- contradictory evidence IDs;
- neutral/unclear evidence count;
- recruitment and sampling limitations;
- final provisional classification.

Contradictory evidence is not an error. It is required output.

## 8. Analysis sequence

```text
Raw research record
      ↓
Quality / provenance check
      ↓
Usable evidence set
      ↓
Problem evidence
      ↓
Severity / frequency
      ↓
Contradiction review
      ↓
Concept evidence
      ↓
Behavioral evidence
      ↓
Segment/channel comparison
      ↓
Hypothesis classification
      ↓
Decision recommendation
```

Do not reverse this sequence by deciding the preferred product direction first.

## 9. Allowed re-structuring during R00

The research may be narrowed or amended when evidence shows that the original framing is too broad, a segment is irrelevant, a question causes systematic bias, or a new recurring problem is materially more important.

Any amendment must record:

- amendment ID;
- reason;
- evidence available before the change;
- exact rule/question changed;
- effective date;
- whether it applies prospectively or retrospectively;
- effect on comparability with prior data.

No amendment may erase the prior version.

## 10. Decision matrix

| Finding | Required interpretation |
|---|---|
| Strong problem + weak solution intent | Preserve problem; redesign solution |
| Strong problem + concentrated use case | Narrow wedge |
| Weak problem + strong concept enthusiasm | Reject enthusiasm as insufficient; revisit problem |
| Strong user problem + strong organization problem | Candidate two-sided wedge; investigate workflow economics |
| Strong problem + major trust barrier | Rework trust architecture before commercialization |
| Fragmented problems with no dominant wedge | Do not force a single MVP use case |
| Weak or infrequent problem across adequate probing | Stop or replace current hypothesis |

## 11. Certification boundary

R00 v0.2 can certify only the integrity and traceability of the research process and the provisional evidence classifications. It cannot certify market size, legal compliance, security, product-market fit or commercial success.
