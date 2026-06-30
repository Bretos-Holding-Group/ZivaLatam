# ADR-0008: MVP Scope Definition

## Status

Accepted

---

## Context

Ziva Latam has a complete foundational architecture:

- Trust Model (badge-based)
- Privacy separation model
- Evidence ingestion system
- Trust Engine processing model
- B2B API exposure model
- System blueprint (service architecture)

However, without a strict MVP scope, the system risks:

- uncontrolled feature expansion
- premature complexity (ZivaPay, automation layers, etc.)
- delayed validation of core value proposition
- resource overload given real-world constraints

A strict MVP boundary is required.

---

## Decision

Ziva Latam MVP will focus exclusively on validating the **Financial Trust Profile (FTP)** system using manual evidence ingestion and deterministic trust generation.

---

## In-Scope (MVP)

### 1. User Registration (Basic Identity)

- Email or minimal identity capture
- Internal user ID generation
- Identity Vault creation (minimal implementation)

---

### 2. Manual Evidence Submission

- Upload of financial documents
- Manual input of income/payment information
- Basic structured evidence forms

No external integrations in MVP.

---

### 3. Evidence Validation (Basic)

- Format validation
- Basic consistency checks
- Manual or semi-automated review capability

---

### 4. Trust Engine (Rule-Based)

- Deterministic badge generation
- No numerical scoring
- Badge assignment based on evidence patterns

---

### 5. Financial Trust Profile (FTP)

- Aggregation of badges
- Structured trust output
- Explainable trust state per user

---

### 6. Basic B2B API

- Read-only trust profile exposure
- Badge-based responses only
- No identity or raw data exposure

---

## Out-of-Scope (Explicitly Deferred)

### 1. ZivaPay

- payment infrastructure
- transaction processing
- real-time financial streams

---

### 2. ZivaOS

- full automation layer
- financial event orchestration system
- advanced integrations

---

### 3. Automatic Bank Integrations

- no banking APIs
- no fintech connectors
- no external financial data ingestion

---

### 4. AI-Based Decisioning

- no machine learning trust scoring
- no predictive financial models
- no black-box inference systems

---

### 5. Advanced Analytics Layer

- no dashboards for external users
- no predictive risk engines
- no behavioral scoring systems

---

## Core MVP Principle

> The MVP exists only to validate whether structured financial evidence can reliably produce trust signals useful for external systems.

---

## Success Criteria

MVP is considered successful if:

- users can submit financial evidence manually
- Trust Engine generates consistent badges
- B2B API can consume trust profiles
- external interpretation of trust is understandable
- system remains explainable end-to-end

---

## Design Constraints

- No scoring system allowed
- No hidden weighting systems allowed
- No AI-driven trust decisions
- No external integrations in MVP
- No expansion beyond defined scope without ADR

---

## Alternatives Considered

### 1. Full Feature MVP (including ZivaPay concepts)

Rejected because:

- too complex for validation phase
- delays core trust model testing
- introduces unnecessary infrastructure risk

---

### 2. AI-Driven MVP

Rejected because:

- reduces explainability
- increases uncertainty in outputs
- contradicts deterministic trust requirement

---

### 3. Open Scope MVP

Rejected because:

- guarantees scope creep
- makes delivery unpredictable
- breaks engineering discipline

---

## Consequences

### Positive

- sharp focus on core value proposition
- faster path to validation
- reduced complexity and risk
- aligned execution with real constraints
- strong foundation for iterative expansion

---

### Negative

- limited initial feature set
- manual processes required
- slower early user experience
- no automation in first iteration

---

## Impact on System

This ADR defines:

- first production target of Ziva Latam
- engineering backlog constraints
- product roadmap boundaries
- architecture enforcement rules for MVP phase

---

## Core Principle

> If a feature does not validate financial trust generation, it does not belong in MVP.

---

## Status

Accepted
