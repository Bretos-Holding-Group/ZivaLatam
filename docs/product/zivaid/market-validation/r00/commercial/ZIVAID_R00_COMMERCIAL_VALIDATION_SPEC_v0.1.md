# ZivaID R00 — Commercial Validation Specification v0.1

**Status:** Draft — controlled pre-revenue layer

## Purpose
Determine whether an evidence-grounded solution creates real commercial behavior before claiming product-market validation or revenue viability.

## Gate
A solution may enter commercial validation only when it is frozen for the experiment and has a traceable problem, target segment, user, buyer/payer hypothesis, value proposition, experiment definition and success/failure criteria.

## Behavioral ladder

`interest → follow-up → meeting → prototype/pilot → proposal → payment → repeat/payment renewal`

These states are not interchangeable. A weaker state cannot be reported as a stronger one.

## Commercial experiment record

```yaml
commercial_experiment_id: CEXP-R00-###
solution_id: SOL-###
solution_version: SOL-###-v0.x
commercial_id: COMM-R00-###
evidence_ids: [EVID-R00-###]
buyer: <role>
payer: <role>
price_or_commitment: <defined offer>
channel: <controlled channel>
start_date: <date>
end_date: <date>
success_criteria: [criterion]
failure_criteria: [criterion]
result: pending|passed|failed|mixed
commercial_evidence_ids: [CEVID-R00-###]
```

## Controls
1. The offer must correspond to a frozen solution version.
2. Commercial claims must be linked to observed behavior.
3. Free interest cannot be counted as payment.
4. A verbal willingness-to-pay statement is not a payment.
5. Discounts, pilots and unpaid tests must retain their actual economic status.
6. Failed experiments remain recorded.
7. Pricing changes create a new experiment or explicit amendment.
8. Results cannot be edited to meet a success threshold.

## Commercial evidence
Commercial evidence receives its own identifiers and remains linked to the underlying participant/organization and source evidence. Payment or commitment records must be verified independently of the researcher's interpretation.

## Decision states

- `continue`: evidence supports another controlled commercial experiment.
- `iterate`: commercial behavior is insufficient or mixed; modify solution/offer and create a new version.
- `narrow`: focus on a smaller segment/use case.
- `stop`: evidence does not justify further commercial investment under the current hypothesis.

## Prohibited conclusions
R00 cannot claim product-market fit, market size, revenue predictability or statistical representativeness from this layer alone.
