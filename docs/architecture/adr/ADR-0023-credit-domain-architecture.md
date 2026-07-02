# ADR-0023 — Credit Domain Architecture & Financial Flow Model

## Status
Accepted

## Domain
Financial System Architecture / Credit Layer

## Related
ADR-0011, ADR-0016, ADR-0022, ADR-0021, ACB-0003

---

# 1. Context

The ZES system includes a conceptual Credit Domain referenced in:

- src/contracts
- system architecture diagrams
- Intelligence Domain dependencies

However, no formal architectural definition previously existed for:

> what "Credit" means inside ZES

This created ambiguity between:

- trust scoring
- financial risk interpretation
- lending logic
- behavioral scoring

---

# 2. Problem

Without formal Credit Domain definition:

- Intelligence Domain may overstep into financial decisioning
- Trust Engine outputs may be misinterpreted as credit decisions
- system risk boundaries become undefined
- regulatory classification becomes unclear

---

# 3. Decision

ZES defines the Credit Domain as:

> A non-custodial financial interpretation layer that translates trust signals into risk-aware credit signals without executing financial transactions.

---

# 4. Core Principle

> Credit in ZES is interpretation, not custody.

---

# 5. Responsibilities

Credit Domain is responsible ONLY for:

- risk scoring interpretation
- credit capacity estimation (non-binding)
- behavioral financial projection
- aggregation of Trust Engine outputs
- credit signal generation for external systems

---

# 6. Strict Non-Responsibilities

Credit Domain MUST NOT:

- hold or transfer funds
- execute payments
- act as a bank
- modify trust engine logic
- perform identity verification
- override kernel execution flow

---

# 7. Input Dependencies

Credit Domain MAY consume:

- Trust Engine outputs
- Evidence data (via contracts only)
- Historical behavior signals

Credit Domain MUST NOT consume:

- raw identity systems
- kernel execution state
- external banking APIs directly

---

# 8. Output Contract

Credit Domain outputs are split into internal and external representations:

## CreditSignalInternal

Used only within Trust/Credit boundary.

```typescript
interface CreditSignalInternal {
  userId: string;

  creditScore: number; // 0–1000 normalized scale

  riskLevel: "low" | "medium" | "high";

  creditCapacityEstimate: number;

  confidence: number;

  derivedFrom: string[];
}
````

---

## CreditSignalExternal

Used for Intelligence Domain and external systems.

```typescript
interface CreditSignalExternal {
  creditScore: number; // 0–1000 normalized scale

  riskLevel: "low" | "medium" | "high";

  creditCapacityEstimate: number;

  confidence: number;

  derivedFrom: string[];
}
```

---

# 9. System Position

```
Evidence → Trust → Credit → Intelligence
```

Credit is a **translation layer**, not a decision authority.

---

# 10. Regulatory Positioning

Credit Domain is defined as:

* non-banking
* non-custodial
* advisory layer only

It does not qualify as:

* lender
* financial institution
* payment processor

---

# 11. Determinism Rules

Credit outputs MUST be:

* reproducible
* deterministic
* explainable
* traceable to inputs

No stochastic scoring allowed.

---

# 12. Alternatives Considered

### 1. Full lending engine

Rejected due to regulatory exposure

### 2. Embedded banking model

Rejected due to custody implications

### 3. Pure Trust Engine extension

Rejected due to scope overload and lack of separation

---

# 13. Consequences

## Positive

* clear financial abstraction layer
* regulatory-safe architecture boundary
* improved modularity
* separation of trust vs credit logic

## Negative

* slower product iteration
* stricter scoring constraints
* additional abstraction overhead

---

# 14. Outcome

The Credit Domain becomes:

> a deterministic financial interpretation layer that does not control money, only risk representation.

---

> Credit does not decide. It interprets.

````
