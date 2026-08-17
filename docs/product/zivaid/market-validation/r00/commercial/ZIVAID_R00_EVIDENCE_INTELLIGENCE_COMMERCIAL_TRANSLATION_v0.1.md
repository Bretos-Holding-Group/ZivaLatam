# ZivaID R00 — Evidence Intelligence & Commercial Translation v0.1

**Status:** Draft — controlled pre-commercial layer

## Purpose
Translate admissible evidence into traceable problem, segment, use-case, value and commercial hypotheses without treating interpretation as proof of demand.

## Pipeline

`Evidence → Problem → Segment → Use Case → User/Buyer/Payer → Value Proposition → Commercial Hypothesis → Experiment`

## Mandatory distinctions
- evidence is not interpretation;
- problem evidence is not solution validation;
- stated interest is not adoption;
- adoption is not willingness to pay;
- user is not necessarily buyer;
- buyer is not necessarily payer.

## Commercial opportunity record

```yaml
commercial_id: COMM-R00-###
evidence_ids: [EVID-R00-###]
problem_id: PROB-R00-###
segment_id: SEG-R00-###
use_case_id: USE-R00-###
user: <role>
buyer: <role>
payer: <role>
value_proposition: <controlled statement>
commercial_model: <hypothesis>
commercial_stage: exploratory|qualified|experiment_ready|validated|rejected
confidence: low|medium|high
assumptions: [ASM-###]
contradictions: [EVID-R00-###]
```

## Rules
1. Every commercial hypothesis must trace to admissible evidence.
2. Contradictory evidence remains visible.
3. One participant cannot create independent commercial demand evidence by repetition.
4. No monetary willingness-to-pay claim may be inferred from positive sentiment.
5. A commercial opportunity remains a hypothesis until real behavior supports it.
6. Changes to a commercial hypothesis are versioned and traceable.

## Output
The layer produces prioritized commercial hypotheses for the Solution Evolution and Commercial Validation layers. It does not authorize sales by itself.
