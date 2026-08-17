# ZivaID R00-W01 — Solution Evolution & Validation Specification v0.1

**Status:** Draft — controlled pre-commercial layer
**Parent:** R00 evidence system
**Purpose:** Translate validated evidence into controlled solution hypotheses, test changes, and freeze versions before commercial validation.

## 1. Core principle

Validated evidence does not automatically authorize a product decision. It creates a basis for a solution hypothesis.

The system must be able to conclude that the current solution is:

- supported;
- partially supported;
- contradicted;
- incomplete;
- too broad;
- too complex;
- commercially unattractive;
- or not yet testable.

## 2. Separation of authorities

Evidence determines what was observed.

Solution evolution determines how the product hypothesis responds.

Commercial validation determines whether the resulting offer produces real market behavior.

No layer may rewrite the evidence layer to justify a preferred solution.

## 3. Controlled lifecycle

```text
Validated Evidence
      ↓
Problem Definition
      ↓
Solution Hypothesis
      ↓
Solution Decomposition
      ↓
Change Proposal
      ↓
Prototype / Experiment
      ↓
Evaluation
   ┌──┴─────┐
   ▼        ▼
FAIL     SUPPORTED
   │        │
   ▼        ▼
REVISE   FREEZE
   │        │
   └──→    ↓
       Commercial Validation
```

## 4. Solution object

Every material solution hypothesis receives a stable identifier:

`SOL-###`

and a version:

`SOL-###-v0.x`

Minimum fields:

- solution_id;
- version;
- trigger_evidence_ids;
- target_problem;
- target_segment;
- user;
- buyer;
- payer;
- proposed_value;
- workflow;
- functional scope;
- trust/privacy requirements;
- technical constraints;
- regulatory assumptions;
- cost assumptions;
- commercial hypothesis;
- unresolved risks;
- validation status.

## 5. Solution Change Ledger

Every material modification creates a change record:

`SOLCH-###`

Required fields:

- previous solution/version;
- proposed solution/version;
- triggering evidence IDs;
- problem detected;
- exact change;
- rationale;
- expected effect;
- experiment required;
- acceptance/failure condition;
- reviewer;
- decision date;
- resulting version.

No material solution change may be made only in conversation or researcher memory.

## 6. Evidence-to-solution traceability

Every proposed material change must reference evidence or a documented assumption.

Allowed origins:

- validated problem evidence;
- validated contradiction;
- usability evidence;
- trust evidence;
- workflow evidence;
- technical feasibility evidence;
- regulatory constraint;
- commercial experiment evidence.

Unverified assumptions must be explicitly marked `ASSUMPTION` and cannot be represented as evidence.

## 7. What may be changed

The system may modify:

- target segment;
- user/buyer/payer definition;
- value proposition;
- use case;
- workflow;
- feature scope;
- trust model;
- privacy model;
- interaction model;
- integration requirements;
- pricing hypothesis;
- delivery model;
- go-to-market hypothesis.

A change may also remove functionality. Deletion is a valid product decision.

## 8. Experiment gate

A solution version cannot advance toward commercial validation until an experiment defines:

1. target user/buyer;
2. problem being addressed;
3. proposed behavior;
4. minimum prototype or service required;
5. observable success behavior;
6. failure condition;
7. evidence required;
8. maximum scope;
9. stop condition.

## 9. Version freeze

After an experiment starts, the tested solution version is frozen.

Changes during the experiment create a new version and cannot be silently combined with the prior version's results.

Example:

`SOL-001-v0.3` tested in W01-E01

If pricing, workflow or core value proposition changes materially:

`SOL-001-v0.4`

must be treated as a new test condition.

## 10. Correction hierarchy

When evidence contradicts the solution:

1. verify the evidence;
2. verify whether the problem interpretation is correct;
3. identify the failed solution assumption;
4. propose a controlled change;
5. define a new experiment;
6. test the new version.

Never modify the evidence to make the solution appear successful.

## 11. Solution decision states

- `hypothesis` — proposed but untested;
- `prototype` — testable artifact/service exists;
- `tested` — experiment completed;
- `supported` — predefined criteria met;
- `mixed` — evidence is contradictory;
- `rejected` — predefined failure condition met;
- `superseded` — replaced by another version;
- `frozen_for_commercial_test` — approved for commercial validation.

## 12. Commercial readiness gate

A solution may enter commercial validation only when:

- its problem basis is traceable;
- its target segment is explicit;
- user/buyer/payer roles are explicit or intentionally tested;
- material trust/privacy requirements are documented;
- solution version is frozen;
- commercial hypothesis is explicit;
- experiment and success/failure criteria are defined;
- unresolved assumptions are listed;
- required approvals are recorded.

## 13. Anti-bias controls

The team must not:

- change a solution after seeing commercial results and retain the same experiment identity;
- remove negative evidence;
- select only supportive participants for redesign decisions without recording recruitment criteria;
- call feature requests proof of willingness to pay;
- call stated interest a sale;
- use revenue from a materially different solution version as evidence for the prior version.

## 14. Output

The layer produces a controlled:

`Solution Decision Record`

containing:

- evidence basis;
- problem statement;
- current solution version;
- changes considered;
- experiments run;
- outcomes;
- contradictions;
- unresolved assumptions;
- decision;
- next experiment.

The output is the bridge from evidence intelligence to commercial validation. It is not itself a sales result.
