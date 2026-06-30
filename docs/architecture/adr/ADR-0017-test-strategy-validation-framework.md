# ADR-0017: Test Strategy & Validation Framework (TSVF)

## Status

Accepted

---

## Context

Ziva Latam has defined:

- Domain Contracts (ADR-0011)
- Trust Engine Core Specification (ADR-0016)
- First Implementation Contract (ADR-0015)
- Execution Model (ADR-0010)

However, there is currently no formal system to:

- validate Trust Engine rules
- ensure deterministic behavior
- prevent regression in badge generation logic
- verify contract compliance in execution

Without a test framework:

- system correctness cannot be guaranteed
- rule changes may break existing behavior silently
- financial trust outputs may become inconsistent

A strict validation framework is required.

---

## Decision

Ziva Latam defines a **Deterministic Test Strategy & Validation Framework (TSVF)**.

This framework ensures all system behavior is:

- testable
- reproducible
- deterministic
- contract-compliant

---

# Core Principle

> If it cannot be tested, it cannot exist in production.

---

# Testing Layers

## Layer 1 — Unit Tests (Rule Level)

Each Trust Engine rule MUST have isolated tests.

### Example coverage:

- R1 Identity Verification
- R2 Income Verification
- R3 Stable Income
- R4 Consistent Payments
- R5 Active Financial History
- R6 Low Documentation Risk
- R7 High Evidence Coverage

---

### Unit Test Rules

Each rule test MUST verify:

- input evidence set
- expected badge output
- deterministic result
- edge case handling

---

## Layer 2 — Contract Tests (ADR-0011 Compliance)

These tests ensure:

- Evidence matches schema
- Badge output matches contract
- FTP structure is valid
- no field violations exist

---

## Layer 3 — Integration Tests (Trust Pipeline)

Validates full flow:

```
Evidence → Trust Engine → Badge Output
```

Must ensure:

- correct transformation
- no data loss
- no unauthorized mutation
- deterministic output

---

## Layer 4 — Scenario Tests (Real-World Simulation)

Simulates user behavior:

- irregular income
- mixed evidence types
- partial validation states
- long-term financial behavior patterns

Purpose:

> Validate system realism without ML inference

---

## Layer 5 — Regression Tests

Ensures:

- no previously valid badge is removed incorrectly
- rule updates do not break existing behavior
- contract stability across versions

---

# Test Data Model

All tests MUST use:

```
Mock Evidence Sets
```

Defined as:

- synthetic
- reproducible
- version-controlled

No production data allowed.

---

# Determinism Rule

All tests must guarantee:

> Same input = same output (100% consistency)

Any deviation = test failure.

---

# Validation Rules

A test suite is valid ONLY if:

- all ADR-0016 rules are covered
- all badges are tested individually
- full pipeline is tested end-to-end
- edge cases are explicitly included
- contract compliance is verified

---

# Failure Conditions

A system is invalid if:

- rules exist without tests
- outputs are unverified
- contract violations are undetected
- regression coverage is missing

---

# Testing Philosophy

## 1. No Hidden Logic

If logic is not tested explicitly, it is considered non-existent.

---

## 2. No Implicit Behavior

System must not rely on:

- inference
- assumptions
- undocumented rules

---

## 3. Test First Validation Gate

No implementation is valid unless:

- corresponding tests exist
- tests pass deterministically
- contract validation is included

---

# Alternatives Considered

## 1. Traditional QA after development

Rejected because:

- allows regression to accumulate
- delays detection of architectural errors
- reduces system predictability

---

## 2. Manual testing only

Rejected because:

- non-reproducible
- not scalable
- not audit-compliant

---

## 3. No formal test framework

Rejected because:

- makes financial trust system unreliable
- breaks auditability requirements
- invalidates enterprise use case

---

# Consequences

## Positive

- fully auditable system behavior
- deterministic validation pipeline
- regression-free trust engine evolution
- high reliability for financial use cases
- strong enterprise readiness foundation

---

## Negative

- increased initial development overhead
- slower feature iteration cycle
- requires strict discipline in test maintenance
- higher upfront complexity

---

# Impact on System

This ADR defines:

- how correctness is validated in Ziva Latam
- how Trust Engine behavior is verified
- how contract compliance is enforced
- how system evolution is controlled safely

---

## Core Principle

> A financial trust system without deterministic tests is invalid by design.
