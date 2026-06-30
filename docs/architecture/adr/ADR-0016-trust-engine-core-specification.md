# ADR-0016: Trust Engine Core Specification (TECS)

## Status

Accepted

---

## Context

Ziva Latam has defined:

- Domain Contracts (ADR-0011)
- First Implementation Contract (ADR-0015)
- Execution Model (ADR-0010)

However, there is still no explicit specification of:

> how evidence becomes trust

Without a strict core specification:

- badge generation may become inconsistent
- rules may drift during implementation
- deterministic behavior may be lost
- MVP validation may fail

A strict Trust Engine Core Specification is required.

---

## Decision

Ziva Latam defines a **deterministic rule-based Trust Engine Core**.

This system:

- does NOT use scoring
- does NOT use AI/ML
- does NOT use probabilistic inference
- operates only on explicit rule evaluation

---

# Core Principle

> Trust is not calculated. Trust is validated.

---

# Input Model

Trust Engine receives:

```
List<Evidence>
```

From ADR-0011:

- income
- payments
- purchases
- contracts
- identity documents

---

# Processing Pipeline

## Step 1 — Evidence Normalization

All evidence is standardized into canonical form:

- type classification confirmed
- timestamp validated
- amount normalized
- source identified

---

## Step 2 — Rule Evaluation Layer

Each evidence is evaluated against deterministic rules.

---

# Core Rules Definition

## Rule R1 — Identity Verification

IF:
- at least 1 valid identity_document exists
- verificationStatus = "validated"

THEN:
- grant "Identity Verified" badge

---

## Rule R2 — Income Verification

IF:
- ≥ 2 income evidences exist
- income evidences span ≥ 60 days

THEN:
- grant "Income Verified" badge

---

## Rule R3 — Stable Income

IF:
- income events occur in ≥ 3 distinct months
- variance between incomes is within acceptable threshold (±40%)

THEN:
- grant "Stable Income" badge

---

## Rule R4 — Consistent Payments

IF:
- ≥ 3 payment evidences exist
- no missing intervals greater than 45 days

THEN:
- grant "Consistent Payments" badge

---

## Rule R5 — Active Financial History

IF:
- combined evidence count ≥ 10
- evidence types include ≥ 3 categories

THEN:
- grant "Active Financial History" badge

---

## Rule R6 — Low Documentation Risk

IF:
- ≥ 80% of evidences are validated
- no rejected identity documents exist

THEN:
- grant "Low Documentation Risk" badge

---

## Rule R7 — High Evidence Coverage

IF:
- evidence spans income + payments + purchases
- timeline ≥ 90 days

THEN:
- grant "High Evidence Coverage" badge

---

# Output Model

Trust Engine produces:

```
List<Badge>
```

Each badge must follow ADR-0011 structure:

- type
- status
- evidence references
- explanation

---

# System Constraints

## 1. Determinism

Same input MUST produce same output.

---

## 2. Statelessness

No stored memory between evaluations.

---

## 3. No Inference Layer

System cannot:

- guess missing data
- interpolate behavior
- infer financial status beyond rules

---

## 4. No External Dependencies

Trust Engine must operate:

- without database
- without APIs
- without external services

---

# Edge Cases Handling

## Missing Evidence

- no badge is granted
- system returns empty evaluation

---

## Partial Data

- only applicable rules are evaluated
- no assumptions are made

---

## Conflicting Evidence

- rejected evidence is ignored
- only validated data is processed

---

# Alternatives Considered

## 1. Machine Learning-based trust scoring

Rejected because:

- violates determinism requirement
- introduces opacity
- reduces auditability

---

## 2. Weighted scoring system

Rejected because:

- reintroduces implicit scoring
- conflicts with badge-based model
- increases complexity unnecessarily

---

## 3. Rule + ML hybrid system

Rejected for MVP because:

- not explainable enough
- breaks strict governance model
- premature optimization

---

# Consequences

## Positive

- fully explainable system behavior
- auditable trust generation
- deterministic outputs
- strong compliance foundation
- predictable B2B integration layer

---

## Negative

- less flexible than ML systems
- requires explicit rule updates for new logic
- may not capture complex financial nuance initially

---

# Impact on System

This ADR defines:

- first real intelligence layer of Ziva Latam
- exact behavior of Trust Engine core
- foundation of badge system
- strict rule-based financial validation logic

---

## Core Principle

> If it cannot be explained in rules, it does not exist in Ziva Trust Engine.

---

## Status

Accepted
