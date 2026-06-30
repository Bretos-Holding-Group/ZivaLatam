# ADR-0006: B2B API Exposure Model

## Status

Accepted

---

## Context

Ziva Latam generates structured financial trust signals (badges) derived from user evidence.

These signals are valuable for external institutions such as:

- lenders
- fintech platforms
- employers
- rental services
- financial aggregators

However, exposing raw financial or identity data introduces significant risks:

- privacy violations
- regulatory exposure
- identity correlation attacks
- data misuse by third parties

A strict B2B exposure model is required.

---

## Decision

Ziva Latam will expose ONLY structured trust signals to B2B systems through secure APIs.

The system will NOT expose:

- raw identity data
- financial documents
- transaction-level details
- source evidence
- direct user identifiers

---

## B2B Data Model

External systems will consume a **Financial Trust Profile (FTP)** in a structured format containing:

### Allowed Outputs

- Trust Badges
  - Identity Verified
  - Income Verified
  - Stable Income
  - Consistent Payments
  - Active Financial History
  - Low Documentation Risk
  - High Evidence Coverage

- Aggregated Trust Signals
  - category-level confidence indicators
  - non-sensitive behavioral summaries

- Verification Status
  - whether identity is verified
  - whether income signals exist
  - whether evidence coverage is sufficient

---

## Forbidden Outputs

The API MUST NEVER expose:

- user identity data (name, ID, contact details)
- raw financial documents
- transaction history
- source-level evidence
- internal system identifiers
- linking keys between identity and evidence

---

## API Design Principle

> B2B systems must be able to trust the signal without ever seeing the source.

---

## Exposure Architecture

### Internal Flow

Identity Layer  
↓  
Evidence Layer  
↓  
Trust Engine  
↓  
B2B API Gateway  
↓  
External Systems

---

### Key Rule

The B2B layer sits above the Trust Engine and is strictly read-only.

It cannot:

- modify user data
- access identity layer
- access raw evidence layer
- influence trust computation

---

## Privacy Enforcement Model

All B2B responses are:

- anonymized
- aggregated
- non-reversible
- context-limited

No response should allow reconstruction of a user's identity.

---

## API Response Structure (Conceptual)

Example output:

```json
{
  "trust_profile": {
    "badges": [
      "Identity Verified",
      "Stable Income",
      "Consistent Payments"
    ],
    "trust_signals": {
      "income_stability": "high",
      "payment_reliability": "medium"
    },
    "verification_status": {
      "identity": true,
      "income": true,
      "coverage": "partial"
    }
  }
}
```

---

## Alternatives Considered

### 1. Full Data Exposure API

Rejected because:

- violates privacy principles
- increases regulatory risk
- exposes sensitive financial behavior
- contradicts identity-evidence separation model

---

### 2. Identity-Permitted B2B Access

Rejected because:

- allows correlation attacks
- increases breach impact
- breaks anonymization guarantees

---

### 3. Score-Based API Output

Rejected because:

- reintroduces opaque scoring systems
- reduces explainability
- conflicts with badge-based trust model

---

## Consequences

### Positive

- strong privacy guarantees for users
- safe enterprise integrations
- regulatory alignment potential
- clean separation of concerns
- scalable B2B adoption model

---

### Negative

- reduced granularity for external systems
- requires trust in Ziva’s internal evaluation
- more complex API abstraction layer
- limits external custom analytics

---

## Impact on Architecture

This ADR defines:

- B2B API Gateway structure
- Trust Engine output formatting
- privacy enforcement layer
- external integration model
- system boundary between internal and external domains

---

## Core Principle

> External systems consume trust, not data.
