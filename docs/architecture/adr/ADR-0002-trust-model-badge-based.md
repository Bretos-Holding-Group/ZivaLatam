# ADR-0002: Badge-Based Trust Model

## Status

Accepted

---

## Context

Traditional financial systems rely on numerical credit scores to represent trustworthiness.

While effective in standardized banking systems, this approach presents limitations:

- Lack of transparency for users
- Poor explainability of decisions
- High exclusion of informal or fragmented financial profiles
- Difficulty representing non-traditional financial behavior
- Over-simplification of complex financial identity

Ziva Latam requires a model that is:

- transparent
- explainable
- modular
- extensible
- inclusive of non-traditional financial data

---

## Decision

Ziva Latam will NOT use a numerical credit score.

Instead, it will implement a **Badge-Based Trust Model**.

Trust will be represented using structured, categorical signals ("badges") derived from verified financial evidence and behavioral patterns.

---

## Trust Representation Model

The system will use structured badges such as:

- Identity Verified
- Income Verified
- Stable Income
- Consistent Payments
- Active Financial History
- Low Documentation Risk
- High Evidence Coverage

Each badge represents a specific, explainable dimension of financial trust.

---

## Design Principles

The badge system must satisfy the following constraints:

### 1. Explainability
Every badge must be derivable from observable or verifiable data.

---

### 2. Modularity
Badges are independent signals and can evolve without affecting others.

---

### 3. Composability
Multiple badges together form a Financial Trust Profile (FTP).

---

### 4. Non-Reductionism
No single numerical value summarizes the user's financial identity.

---

### 5. B2B Consumability
External systems consume structured badges, not internal scoring logic.

---

## Alternatives Considered

### 1. Numerical Credit Score System

Rejected because:

- opaque decision-making
- reinforces traditional financial exclusion
- difficult to explain or audit
- reduces multi-dimensional financial behavior into a single metric

---

### 2. Hybrid Score + Badges System

Rejected because:

- introduces hidden weighting complexity
- reintroduces opacity through scoring aggregation
- increases inconsistency between signals and score

---

### 3. Fully AI-Generated Credit Score

Rejected because:

- non-deterministic outputs reduce auditability
- increases regulatory and trust risk
- lacks explainability requirements for financial systems

---

## Consequences

### Positive

- Full transparency of trust signals
- Better inclusion of non-traditional users
- Easier interpretation by B2B systems
- Strong alignment with “trust through evidence” philosophy
- Improved auditability and compliance potential

---

### Negative

- Requires careful design of badge definitions
- More complex than single-score systems for integration
- Requires B2B partners to adapt to new model
- Needs governance for badge evolution over time

---

## Impact on System Architecture

This decision directly affects:

- Trust Layer (core system module)
- API design for B2B consumers
- Evidence processing pipeline
- Identity-to-trust mapping logic

---

## Related Domains

- Product Domain
- Architecture Domain
- Engineering Domain
- Governance Domain

---

## Notes

This ADR defines the core identity of Ziva Latam as a financial trust infrastructure system.

It replaces traditional scoring mechanisms with structured, explainable trust signals.

---

## Status

Accepted
