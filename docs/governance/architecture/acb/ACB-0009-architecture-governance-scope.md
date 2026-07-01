# ACB-0009 — Architecture Governance & Certification Scope Alignment

## Status
In Review

---

## Context

The ZES system has evolved into a multi-domain architecture with:

- Kernel Layer
- Contracts Layer
- Evidence Domain
- Trust Domain
- Credit Domain
- Intelligence Domain

During system evolution, multiple inconsistencies emerged between:

- implementation structure (`src/`)
- ADR governance layer
- certification requirements
- backlog tracking (ACB system)

---

## Problem

The system currently suffers from:

- architecture drift between implementation and governance
- undefined boundary between ADR scope and ACB scope
- certification dependency ambiguity
- lack of unified scope control layer

This results in:

> unclear authority over what is "in scope" for certification vs implementation

---

## Decision

A formal **Architecture Governance & Certification Scope Alignment layer (ACB-0009)** is introduced.

This ACB defines the governance boundary between:

- architectural decisions (ADR)
- implementation tracking (src/)
- certification prerequisites (Foundation Certification)

---

## Scope Definition

This ACB governs:

### 1. Certification Scope Control
Defines what is required for:

- Foundation Certification execution
- audit readiness
- system validation gates

---

### 2. Architecture Completeness Rules

Ensures:

- every implementation has ADR mapping
- no orphaned domains in `src/`
- no undocumented dependencies

---

### 3. Backlog Governance

Formalizes:

- ACB lifecycle rules
- dependency ordering
- resolution criteria

---

## Certification Dependency Rules

Foundation Certification MUST NOT execute unless:

- all critical ACB items are either:
  - resolved OR
  - explicitly deferred via ADR update

---

## Relationship to ADR System

This ACB does NOT define architecture.

It governs:

- consistency of architecture
- certification readiness
- structural integrity checks

---

## System Impact

After ACB-0009:

- ADR layer remains pure architectural truth
- ACB layer becomes governance + alignment layer
- certification becomes formally gated process
- system traceability is enforced end-to-end

---

## Outcome

- Eliminates ambiguity between implementation and governance
- Establishes certification control boundary
- Enables audit-grade system structure

---
