# ADR-0009: Coding Standards & Repository Structure

## Status

Accepted

---

## Context

Ziva Latam is transitioning from architecture design to real implementation.

Without strict coding standards and repository structure rules:

- code will become inconsistent
- modules will drift from architecture
- onboarding developers will be difficult
- maintenance cost will increase over time
- ADR-defined architecture will not be correctly implemented

A strict engineering implementation layer is required.

---

## Decision

Ziva Latam will enforce a unified coding standard and repository structure that all implementation must follow.

All code must align with the Ziva Engineering System (ZES) architecture and ADR decisions.

---

## Repository Structure (Canonical)

```text
ZivaLatam/
│
├── docs/
│   ├── engineering/
│   ├── product/
│   └── architecture/
│       └── adr/
│
├── src/
│   ├── identity/
│   ├── evidence/
│   ├── trust/
│   ├── api/
│   ├── orchestration/
│   └── shared/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── scripts/
│
├── config/
│
└── README.md
```

---

## Module Responsibilities

### identity/

- User identity management
- Authentication logic
- Identity Vault access layer

---

### evidence/

- Evidence ingestion logic
- Validation pipelines
- Data normalization

---

### trust/

- Trust Engine implementation
- Badge generation logic
- Rule evaluation system

---

### api/

- B2B API exposure layer
- Request/response formatting
- Access control enforcement

---

### orchestration/

- Workflow coordination
- Cross-module communication
- Event handling (future-ready)

---

### shared/

- Common utilities
- Types and interfaces
- Reusable logic components

---

## Coding Standards

### 1. Naming Conventions

- Files: `kebab-case`
- Functions: `camelCase`
- Classes: `PascalCase`
- Modules: `lowercase folders`

---

### 2. Architecture Compliance

Code MUST:

- respect ADR-defined boundaries
- avoid cross-domain direct access
- use defined module interfaces only
- never bypass Trust Engine rules

---

### 3. Separation of Concerns

Each module must:

- have a single responsibility
- avoid internal coupling with other domains
- expose controlled interfaces only

---

### 4. No Business Logic Leakage

Business logic must NOT:

- appear in API layer
- be embedded in identity layer
- bypass trust engine rules

All business logic relevant to trust must live in `trust/`.

---

### 5. Dependency Rules

Allowed dependencies:

- identity → shared
- evidence → shared
- trust → evidence, shared
- api → trust, shared
- orchestration → all modules

Forbidden:

- circular dependencies
- direct identity ↔ trust coupling
- API layer direct access to evidence storage

---

## Testing Requirements

All modules must include:

- unit tests for core logic
- integration tests for cross-module behavior
- e2e tests for critical flows

No untested core logic is allowed in production.

---

## Architectural Enforcement Principle

> Code must reflect architecture exactly. Not approximately.

---

## Alternatives Considered

### 1. Flexible Repository Structure

Rejected because:

- leads to long-term inconsistency
- increases onboarding cost
- breaks architectural traceability

---

### 2. Micro-team autonomy structure

Rejected because:

- encourages divergence in implementation
- reduces system coherence
- breaks ADR compliance enforcement

---

### 3. No enforced standards (organic growth)

Rejected because:

- guaranteed architectural drift
- unmaintainable system over time
- loss of system integrity

---

## Consequences

### Positive

- predictable codebase structure
- easier onboarding
- strong alignment with ADR architecture
- scalable long-term maintainability
- reduced technical debt accumulation

---

### Negative

- initial rigidity in development
- slower early iteration speed
- higher discipline requirement from developers
- reduced informal flexibility

---

## Impact on System

This ADR defines:

- physical structure of GitHub repository
- implementation constraints for all modules
- developer onboarding rules
- long-term maintainability guarantees
- mapping between architecture and code

---

## Core Principle

> Architecture is meaningless unless code enforces it.
