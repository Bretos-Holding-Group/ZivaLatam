# ADR-0021: First Implementation Test Dataset Specification (FITDS)

## Status

Accepted

---

## Context

Ziva Latam has defined:

- Trust Engine Core Specification (ADR-0016)
- Test Strategy & Validation Framework (ADR-0017)
- Security & Data Protection Model (ADR-0018)
- First Implementation Execution Protocol (ADR-0020)

However, there is no formal definition of:

> what valid test data looks like for the system

Without a standardized dataset specification:

- tests may be inconsistent
- outputs may not be reproducible
- rule validation may drift across environments
- scenario testing may lose realism

A deterministic test dataset model is required.

---

## Decision

Ziva Latam defines a **First Implementation Test Dataset Specification (FITDS)**.

This specification defines synthetic, reproducible financial datasets
for Trust Engine validation.

---

# Core Principle

> If the data is not reproducible, the system is not valid.

---

# Dataset Structure

All test datasets MUST follow this structure:

```
TestUserDataset
 ├── IdentityData (optional, for internal mapping only)
 ├── EvidenceData
 ├── Timeline
 ├── ExpectedBadges
```

---

# 1. IdentityData (Internal Only)

Used ONLY for mapping in test environments.

### Contains:

- user_id (UUID)
- anonymized identity reference

### Rules:

- never used in Trust Engine logic
- never exposed to output layer
- used only for simulation consistency

---

# 2. EvidenceData

Core of the dataset.

### Allowed evidence types:

- income_event
- payment_event
- purchase_event
- contract_event
- identity_document_event

---

### Required Fields:

Each evidence MUST include:

- type
- timestamp
- amount (if applicable)
- source
- validation_status

---

# 3. Timeline

Defines chronological structure.

Rules:

- must span minimum 90 days for full scenario tests
- must support multi-month income simulation
- must allow gaps for payment consistency tests

---

# 4. ExpectedBadges

Defines deterministic expected output.

Example:

```
ExpectedBadges:
  - Identity Verified
  - Income Verified
  - Stable Income
  - Consistent Payments
```

Rules:

- must be explicitly declared
- no inferred expectations allowed
- must align with ADR-0016 rules

---

# Dataset Categories

## Category A — Stable User

Characteristics:

- regular income
- consistent payments
- long-term evidence stability

Expected outcome:

- high badge coverage

---

## Category B — Irregular Income User

Characteristics:

- variable income
- inconsistent months
- partial payment history

Expected outcome:

- partial badge set

---

## Category C — New User

Characteristics:

- minimal evidence
- short timeline
- limited validation data

Expected outcome:

- identity only or minimal badges

---

## Category D — High Trust User

Characteristics:

- multi-source income
- long timeline (>180 days)
- high evidence density

Expected outcome:

- full badge set

---

# Determinism Rules

All datasets MUST ensure:

- identical input produces identical Trust Engine output
- no randomness in generation
- no external dependencies
- version-controlled dataset files

---

# File Format

All datasets MUST be stored as:

```
/tests/fixtures/financial/
```

Format:

- JSON (preferred)
- strictly typed schema
- versioned per scenario

Example:

```
stable-user-v1.json
irregular-user-v1.json
new-user-v1.json
high-trust-user-v1.json
```

---

# Validation Rules

Dataset is valid ONLY if:

- all evidence types are schema-compliant
- timeline is coherent
- expected badges are explicitly defined
- scenarios are reproducible
- no real personal data exists

---

# Failure Conditions

Dataset is invalid if:

- real user data is used
- timestamps are inconsistent
- expected outputs are missing
- randomness is introduced
- schema is partially defined

---

# Alternatives Considered

## 1. Real-world anonymized data

Rejected because:

- re-identification risk
- non-deterministic behavior
- compliance complexity

---

## 2. AI-generated synthetic data on runtime

Rejected because:

- non-reproducible
- violates deterministic requirement
- introduces hidden variability

---

## 3. Manual ad-hoc test data

Rejected because:

- inconsistent structure
- lacks scalability
- no version control discipline

---

# Consequences

## Positive

- fully reproducible test system
- deterministic validation of Trust Engine
- scalable scenario coverage
- strong compliance foundation
- predictable system evolution

---

## Negative

- initial manual dataset design effort
- requires strict dataset discipline
- additional versioning overhead
- slower test iteration at early stages

---

# Impact on System

This ADR defines:

- how Trust Engine will be tested in real conditions
- how financial behavior is simulated safely
- how system correctness is validated continuously
- how production confidence is achieved before launch

---

## Core Principle

> A financial system is only as reliable as its test data.

---

## Status

Accepted
