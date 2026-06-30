# ADR-0020: First Implementation Execution Protocol (FIEP)

## Status

Accepted

---

## Context

Ziva Latam has completed all architectural layers:

- System Architecture (ADRs 0001–0007)
- MVP Scope (ADR-0008)
- Coding Standards (ADR-0009)
- Execution Model (ADR-0010)
- Domain Contracts (ADR-0011)
- Tech Stack (ADR-0012)
- Bootstrap Protocol (ADR-0013)
- Validation System (ADR-0014)
- First Implementation Contract (ADR-0015)
- Trust Engine Specification (ADR-0016)
- Test Framework (ADR-0017)
- Security Model (ADR-0018)
- Repository Initialization Plan (ADR-0019)

However, there is still no strict definition of:

> how the first real executable code is created in a controlled and compliant way

Without this protocol:

- first implementation may drift from architecture
- Trust Engine structure may be inconsistent
- contracts may be partially ignored in code
- testing and execution layers may not align

A strict execution protocol is required.

---

## Decision

Ziva Latam defines a **First Implementation Execution Protocol (FIEP)**.

This protocol governs the exact creation of the first executable module:

```
/src/trust/core/
```

---

# Core Principle

> The first code written defines the discipline of the entire system.

---

# Execution Flow (Mandatory Order)

## STEP 1 — Repository State Verification

Before writing code:

- ADR-0001 → ADR-0019 must exist
- no implementation code must exist
- structure must match ADR-0009
- MXL layer must exist but remain inactive

---

## STEP 2 — Folder Creation (Trust Domain Only)

Create:

```
/src/trust/core/
```

Rules:

- must be empty initially
- no logic allowed at creation stage
- no auxiliary modules allowed outside trust domain

---

## STEP 3 — File Initialization Order

The first implementation MUST follow this exact order:

### 1. types.ts

Defines local type alignment with ADR-0011 contracts.

- must NOT redefine contracts
- must only reference or extend safely

---

### 2. trustEngine.ts

Core orchestrator.

Responsibilities:

- receives validated Evidence input (mocked)
- applies rule evaluation pipeline (ADR-0016)
- returns Badge output (ADR-0011 compliant)

---

### 3. evaluateEvidence.ts

Responsibilities:

- applies deterministic rule evaluation
- no external dependencies
- no persistence
- no side effects

---

### 4. generateBadges.ts

Responsibilities:

- converts rule results into Badge objects
- ensures contract compliance
- ensures deterministic mapping

---

## STEP 4 — Integration Rule

All files MUST:

- follow ADR-0011 contracts strictly
- remain stateless
- avoid external dependencies
- avoid identity exposure

---

## STEP 5 — Mock Input Requirement

First implementation MUST use:

```
Mock Evidence Set
```

Rules:

- synthetic data only
- version-controlled test dataset
- no production data allowed

---

## STEP 6 — First Execution Output

The system must produce:

```
List<Badge>
```

That is:

- deterministic
- reproducible
- contract-compliant

---

## STEP 7 — First Commit Definition

The first valid commit MUST include:

- `/src/trust/core/types.ts`
- `/src/trust/core/evaluateEvidence.ts`
- `/src/trust/core/generateBadges.ts`
- `/src/trust/core/trustEngine.ts`

### Commit message format:

```
feat(trust-engine): initialize deterministic core evaluation system
```

---

## STEP 8 — Validation Gate

Commit is ONLY valid if:

- all files exist in correct order
- no business logic outside trust domain exists
- all outputs match ADR-0011
- execution is deterministic
- no external dependencies are introduced

---

# Hard Constraints

## Constraint 1 — No premature expansion

No additional modules allowed in first implementation.

---

## Constraint 2 — No architectural bypass

Trust Engine MUST NOT:

- access Identity Vault
- access API layer
- access database layer

---

## Constraint 3 — No scoring systems

System must remain:

- rule-based only
- no numeric scoring aggregation
- no probabilistic inference

---

## Constraint 4 — No hidden logic

All logic must be:

- explicit
- testable
- traceable to ADR-0016 rules

---

# Failure Conditions

Implementation is invalid if:

- files are created in wrong order
- contracts are violated
- logic is distributed outside trust domain
- non-deterministic behavior appears
- MXL is bypassed

---

# Alternatives Considered

## 1. Free-form implementation

Rejected because:

- breaks architectural discipline
- introduces unpredictable behavior
- violates contract system

---

## 2. Full system implementation at once

Rejected because:

- removes control over Trust Engine validation
- increases risk of hidden architectural drift

---

## 3. API-first implementation

Rejected because:

- bypasses core logic validation layer
- couples system prematurely to external interfaces

---

# Consequences

## Positive

- deterministic first implementation
- strict adherence to architecture
- controlled system initialization
- high confidence in Trust Engine correctness
- predictable evolution path

---

## Negative

- slower initial coding process
- strict file ordering constraints
- reduced early flexibility
- higher discipline requirement

---

# Impact on System

This ADR defines:

- exact procedure for first real code
- structure of Trust Engine implementation
- enforcement mechanism for architecture compliance
- boundary between design and execution

---

## Core Principle

> The first implementation is not experimentation. It is validation of architecture.

---

## Status

Accepted
