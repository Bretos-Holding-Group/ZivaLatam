# ADR-0018: Security & Data Protection Model (SDPM)

## Status

Accepted

---

## Context

Ziva Latam processes highly sensitive financial and identity-related data:

- identity documents
- income records
- payment history
- financial behavior patterns
- contractual evidence

Without strict separation and protection:

- identity leakage becomes possible through correlation
- financial data can be re-identified
- B2B exposure may reveal personal information
- regulatory compliance becomes impossible

A strict security architecture is required from the foundation.

---

## Decision

Ziva Latam defines a **Security & Data Protection Model (SDPM)** based on strict separation between identity and financial evidence.

---

# Core Architecture Principle

> Identity and financial behavior must never coexist in the same exposed data surface.

---

# System Components

## 1. Identity Vault (IV)

The Identity Vault stores all direct personal identifiers.

### Contains:

- full name
- national ID (RUN or equivalent)
- email
- phone number
- address
- authentication credentials

### Properties:

- encrypted at rest
- strictly access-controlled
- never exposed to B2B layer
- never included in analytics

---

## 2. Financial Evidence Layer (FEL)

Stores only behavioral financial data.

### Contains:

- income events
- payments
- purchases
- contracts
- financial interactions

### Properties:

- linked only via internal UUID
- no direct identifiers
- anonymized by design
- safe for internal processing only

---

## 3. Internal User ID (UUID Layer)

Acts as the **only bridge** between Identity Vault and Financial Evidence.

```
Identity Vault → UUID → Financial Evidence
```

### Rules:

- UUID is non-reversible
- UUID cannot derive identity
- UUID is internal-only reference

---

## 4. Trust Engine Output Layer

Produces:

- badges
- Financial Trust Profile (FTP)

### Properties:

- contains NO identity data
- contains NO raw evidence
- contains ONLY derived signals

---

## 5. B2B Exposure Layer

External companies receive:

- anonymized FTP
- badge-based trust signals

### Strict Rules:

- no identity exposure
- no raw financial events
- no traceable personal metadata
- only aggregated trust indicators

---

# Data Separation Model

```
[ Identity Vault ]
        ↓ (encrypted mapping)
     [ UUID ]
        ↓
[ Financial Evidence Layer ]
        ↓
[ Trust Engine ]
        ↓
[ FTP Output ]
        ↓
[ B2B API (Anonymized) ]
```

---

# Anonymization Rules

## Rule A1 — No Identity Leakage

No B2B response may include:

- name
- email
- phone
- document numbers
- direct identifiers

---

## Rule A2 — Structural Obfuscation

Financial data exposed externally MUST:

- be aggregated
- be categorized
- avoid raw transaction detail

---

## Rule A3 — Irreversible Mapping

It must be computationally impossible to:

- reconstruct identity from evidence alone
- derive personal identity from badge patterns
- reverse-engineer UUID mapping externally

---

# Access Control Rules

## Internal System Access

Only Trust Engine and core services may access:

- Identity Vault (restricted layer)
- Financial Evidence Layer (full access internally)

---

## External Access

B2B clients may access ONLY:

- Financial Trust Profile
- Badge set
- High-level trust signals

---

# Security Principles

## 1. Zero Trust Internal Architecture

Every service must validate access independently.

---

## 2. Least Privilege Access

Each module accesses only what it needs:

- Trust Engine → evidence only
- API → outputs only
- Identity → isolated layer

---

## 3. Fail-Secure Design

Any failure must:

- deny access by default
- not expose data
- not degrade into unsafe mode

---

## 4. Data Minimization

Only necessary data is stored, processed, or exposed.

---

# Threat Model

## Threat 1 — Data Breach

Mitigation:

- separation of Identity Vault and Evidence Layer
- encryption + UUID decoupling

---

## Threat 2 — Re-identification Attack

Mitigation:

- anonymized outputs only
- no raw financial traces externally

---

## Threat 3 — Internal Misuse

Mitigation:

- strict module isolation
- least privilege access model

---

# Alternatives Considered

## 1. Unified database model

Rejected because:

- identity and behavior correlation risk
- high breach impact

---

## 2. Partial anonymization only at API layer

Rejected because:

- identity can still leak internally
- insufficient protection model

---

## 3. No formal separation model

Rejected because:

- unacceptable risk for financial product
- non-compliance with trust requirements

---

# Consequences

## Positive

- strong privacy-first architecture
- enterprise-grade data separation
- compliance-ready design
- reduced breach impact surface
- scalable trust infrastructure

---

## Negative

- higher system complexity
- additional abstraction layers
- more strict development discipline required
- increased initial implementation overhead

---

# Impact on System

This ADR defines:

- full identity isolation architecture
- security model for financial data
- B2B privacy guarantees
- internal system trust boundaries

---

## Core Principle

> Trust cannot exist without privacy. Privacy cannot exist without separation.

---

## Status

Accepted
