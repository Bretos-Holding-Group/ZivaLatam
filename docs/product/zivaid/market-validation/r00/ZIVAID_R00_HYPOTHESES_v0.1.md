# ZivaID R00 — Hypotheses v0.1

**Status:** Draft — pre-execution  
**Parent:** `ZIVAID_MARKET_VALIDATION_R00_v0.1.md`

## H-001 — Repeated verification problem

**Hypothesis:** A meaningful share of target participants repeatedly provide identity or supporting documents/information that they have already provided elsewhere.

**Evidence sought:** recent concrete examples, frequency, institutions involved and impact.

**Disconfirming signal:** most participants report little or no repetition, or repetition is considered trivial.

## H-002 — The problem has meaningful cost

**Hypothesis:** Repeated verification creates enough time, financial, operational or emotional friction to motivate a change.

**Evidence sought:** delays, failed applications, travel, printing, administrative effort, lost opportunities or other concrete costs.

**Disconfirming signal:** participants recognize repetition but do not consider it materially costly.

## H-003 — Minimum disclosure has user value

**Hypothesis:** People value proving a specific requirement without exposing unrelated information.

**Evidence sought:** reactions to concrete examples such as age eligibility or prescription verification.

**Disconfirming signal:** participants prefer unrestricted disclosure or do not perceive unnecessary disclosure as a problem.

## H-004 — Reusable credentials have value

**Hypothesis:** Users and organizations see value in a credential that can be reused when it remains valid, relevant and authorized.

**Evidence sought:** concrete current verification pain, reactions to reusable credentials, and organizational workflow implications.

**Disconfirming signal:** users prefer repeated manual verification or organizations reject reusable evidence as operationally impractical.

## H-005 — Trust is a material adoption barrier

**Hypothesis:** Trust, privacy, security, control and institutional legitimacy are among the strongest barriers to adoption.

**Evidence sought:** spontaneous objections before prompting and ranked concerns after the concept test.

**Disconfirming signal:** trust concerns are consistently minor compared with other barriers.

## H-006 — One initial use case will dominate

**Hypothesis:** Demand will concentrate around one or a small number of use cases rather than being equally distributed across all identity domains.

**Evidence sought:** participant-selected first-use scenarios and organization process pain points.

**Disconfirming signal:** no use case shows meaningful concentration or the problem is too fragmented to support an initial wedge.

## H-007 — Organizational verification demand exists

**Hypothesis:** Some businesses or institutions have a measurable operational problem caused by repeatedly collecting, checking or storing evidence from users.

**Evidence sought:** current workflow, manual steps, turnaround time, error/rejection rate, compliance burden and willingness to discuss a pilot.

**Disconfirming signal:** organizations report that current verification is satisfactory or that a reusable credential layer would not reduce meaningful cost/risk.

## H-008 — Users will accept a ZivaID-like concept

**Hypothesis:** After describing the concept neutrally, a meaningful subset of participants will express willingness to test it.

**Important:** willingness statements are weaker than behavioral commitment.

**Stronger signal:** voluntary follow-up, referral, prototype request or pilot participation.

## H-009 — Data sovereignty is a prerequisite

**Hypothesis:** Users will expect control, portability and clear limits on secondary use before trusting a cross-service identity system.

**Evidence sought:** objections concerning ownership, portability, profiling, surveillance and cross-domain access.

**Disconfirming signal:** users consistently treat these concerns as irrelevant.

## H-010 — The broad ZivaID proposition may be too large for an initial market wedge

**Hypothesis:** The full multi-domain vision is less compelling than a narrow initial use case.

**Evidence sought:** comparison of first-use preferences and willingness to test individual workflows.

**Disconfirming signal:** participants consistently value the broad identity layer itself without needing a specific use case.

## Operationalization lock

The terms **meaningful share**, **meaningful cost**, **meaningful concentration** and **meaningful subset** are not statistical claims in v0.1. However, their interpretation must not be chosen after the results are known.

Before the first controlled R00 evidence is collected, the research team must record an analysis rule for each hypothesis specifying:

1. the evidence types that can support the hypothesis;
2. the minimum independence required for corroboration;
3. the relevant segment or population scope;
4. how contradictory evidence will affect classification;
5. whether a quantitative threshold is being used and, if so, its exact value.

If no quantitative threshold is appropriate, the pre-registered rule must use qualitative triangulation criteria and must state what combination of evidence would be sufficient, insufficient or contradictory.

Once evidence collection begins, the analysis rule may not be changed to obtain a preferred outcome. Any necessary change must be versioned as a protocol amendment and applied prospectively, with the prior rule retained in the record.

The final R00 report must disclose the pre-registered rule and any approved amendments before presenting the classification.

## Hypothesis dependency

The hypotheses are not independent claims of market demand. They form a progression:

```text
H-001 / H-002
problem + severity
        ↓
H-003 / H-004
solution characteristics
        ↓
H-005 / H-009
trust + control constraints
        ↓
H-006 / H-010
initial market wedge
        ↓
H-007 / H-008
organizational + user behavioral intent
```

A positive result for a downstream hypothesis cannot compensate for a failed foundational problem hypothesis.

## Falsification rule

A hypothesis must not be marked "validated" merely because no contradiction was observed. Each hypothesis should receive one of:

- **Supported** — evidence currently favors it.
- **Mixed** — evidence is ambiguous or segment-dependent.
- **Not supported** — evidence currently favors rejection.
- **Untested** — insufficient evidence.

R00 conclusions remain provisional and must identify sample limitations.

## Evidence minimum for classification

Before a hypothesis is classified **Supported**, the analysis must identify:

- the relevant independent evidence IDs;
- the participant/organization segments represented;
- at least one concrete experience or behavioral signal where applicable;
- contradictory evidence reviewed;
- recruitment and sampling limitations;
- why the evidence is sufficient under the pre-registered analysis rule.

No hypothesis is considered "validated" by raw count alone.