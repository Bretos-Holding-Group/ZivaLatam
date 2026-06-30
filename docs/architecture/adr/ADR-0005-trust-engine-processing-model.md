# ADR-0005: Trust Engine Processing Model

## Status

Accepted

---

## Context

Ziva Latam converts financial evidence into trust signals used by B2B systems.

However, traditional systems rely on:

- numerical credit scoring
- opaque risk models
- non-explainable AI decisions

This approach is incompatible with Ziva’s principles of:

- transparency
- auditability
- inclusion
- explainability

A deterministic and explainable Trust Engine is required.

---

## Decision

Ziva Latam will implement a **rule-based Trust Engine** that transforms validated financial evidence into structured trust badges.

The system will NOT use:

- numerical credit scores
- hidden weighting systems
- black-box AI decisioning for trust generation

---

## Trust Engine Model

The Trust Engine operates in three stages:

---

### 1. Evidence Evaluation

Incoming evidence is evaluated based on:

- type (income, payment, identity, etc.)
- consistency over time
- frequency patterns
- completeness
- verification level

No aggregation into a single score occurs.

---

### 2. Rule-Based Interpretation

Each evidence pattern maps to explicit rules.

Example:

- If income is detected across multiple months → Stable Income badge
- If identity is verified via valid documents → Identity Verified badge
- If payments are consistently on time → Consistent Payments badge

Rules are:

- deterministic
- versioned
- auditable
- stored in system registry

---

### 3. Badge Generation

The output of the Trust Engine is a set of structured badges:

- Identity Verified
- Income Verified
- Stable Income
- Consistent Payments
- Active Financial History
- Low Documentation Risk
- High Evidence Coverage

Each badge is:

- independently computed
- explainable
- revocable if evidence changes
- traceable to source data

---

## Core Principle

> The system does not calculate trust. It derives trust signals from observable evidence.

---

## Explainability Requirement

Every badge must be able to answer:

- Why was this assigned?
- What evidence supports it?
- What rule triggered it?
- When was it last updated?

If a badge cannot be explained → it is invalid.

---

## Alternatives Considered

### 1. Numerical Scoring Engine

Rejected because:

- opaque decision-making
- non-auditable logic
- introduces hidden weighting systems
- contradicts transparency requirements

---

### 2. Machine Learning Trust Model

Rejected because:

- non-deterministic outputs
- difficult to explain decisions
- hard to audit individual outcomes
- incompatible with regulatory transparency expectations

---

### 3. Hybrid Score + Rules System

Rejected because:

- reintroduces hidden scoring logic
- creates inconsistency between outputs
- reduces explainability

---

## Consequences

### Positive

- full transparency of trust generation
- deterministic and auditable outputs
- easier regulatory alignment
- strong alignment with financial inclusion goals
- predictable system behavior

---

### Negative

- requires careful rule design
- more manual governance of badge definitions
- less flexible than AI-based scoring systems
- requires structured evolution of rules over time

---

## Impact on Architecture

This ADR directly defines:

- Trust Layer internal logic
- Badge system behavior
- Evidence-to-trust pipeline
- API output structure for B2B clients
- Governance of trust rules (future policy layer)

---

## Evolution Path

Future evolution may include:

- rule optimization systems
- AI-assisted rule suggestions (not decision-making)
- dynamic rule versioning
- sector-specific trust profiles

However:

> Final decision authority will always remain rule-based and deterministic.

---

## Related Domains

- Architecture
- Engineering
- Product
- Governance
