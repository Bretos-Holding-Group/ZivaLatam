# ADR-0015: First Implementation Contract (FIC)

## Status

Accepted

---

## Context

Ziva Latam has reached a stage where:

- architecture is fully defined
- domain contracts are strict
- execution model (MXL) exists
- validation system is in place
- tech stack has been selected
- bootstrap protocol is defined

However, there is still a critical gap:

> There is no controlled definition of how the first real code is written.

Without this contract:

- first implementation may violate architecture
- Trust Engine could drift from ADR definition
- domain contracts may be bypassed
- MVP boundaries may be broken at first commit

A strict First Implementation Contract is required.

---

## Decision

Ziva Latam defines a **First Implementation Contract (FIC)** that governs the creation of the initial executable module: the Trust Engine Core.

---

# Scope of First Implementation

## Allowed First Module

Only the following module may be implemented first:

/src/trust/core/

---

## Purpose

The first implementation must ONLY:

- simulate badge generation logic
- implement rule-based evaluation (no scoring)
- consume mocked Evidence Contracts
- output structured Badge Contracts
- remain fully deterministic

---

## Forbidden in First Implementation

The following are strictly forbidden:

- database integration
- API layer implementation
- identity logic
- external integrations
- AI/ML logic
- scoring systems
- persistence logic
- authentication systems

---

# Implementation Rules

## 1. Contract Compliance

All code MUST strictly follow:

- ADR-0011 (Domain Contracts)

No deviation allowed.

---

## 2. MXL Alignment

Implementation MUST reflect:

- Evidence → Trust Engine → Badge output flow
- No missing or additional layers
- No shortcut logic

---

## 3. Deterministic Logic Only

Trust Engine must:

- produce identical output for identical input
- avoid randomness
- avoid external state dependency

---

## 4. Stateless Core Requirement

First implementation must be:

- pure logic
- no side effects
- no persistence layer

---

## 5. Output Contract Enforcement

Output MUST match:

- Badge Contract (ADR-0011)
- Financial Trust Profile structure (conceptually)

---

# First Implementation Structure

```
/src/trust/core/
  ├── evaluateEvidence.ts
  ├── generateBadges.ts
  ├── trustEngine.ts
  └── types.ts
```

---

## Core Flow

```text
Mock Evidence Input
        ↓
evaluateEvidence()
        ↓
generateBadges()
        ↓
Trust Engine Core
        ↓
Badge Output (ADR-0011 compliant)
```

---

## Validation Rules

First implementation is valid ONLY if:

- no external dependencies are used
- no database connections exist
- output matches Badge Contract
- logic is fully deterministic
- no identity data is accessed
- no API layer is introduced

---

## Failure Conditions

Implementation is invalid if:

- scoring system appears
- ML/AI logic is introduced
- API routes are created
- persistence is added prematurely
- contracts are violated
- MXL flow is bypassed

---

## Core Principle

> The first line of code must prove that the architecture is real, not theoretical.

---

## Alternatives Considered

### 1. Full system implementation from start

Rejected because:

- breaks controlled validation
- introduces uncontrolled complexity
- violates MVP discipline

---

### 2. API-first implementation

Rejected because:

- bypasses Trust Engine core validation
- couples system too early to external interfaces

---

### 3. Database-first implementation

Rejected because:

- introduces persistence before logic validation
- risks architectural inversion

---

## Consequences

### Positive

- controlled system initialization
- deterministic Trust Engine foundation
- strict compliance with architecture
- safe expansion path for future modules
- reduced risk of early system corruption

---

### Negative

- no real product interface yet
- limited early usability
- strict constraints on first development phase
- slower perceived progress

---

## Impact on System

This ADR defines:

- exact first code entry point
- structure of Trust Engine initial implementation
- enforcement of contract-driven development
- boundary between architecture and execution

---

## Core Principle

> The first implementation defines the culture of the entire system.
