# ADR-0003: Privacy & Identity Separation Model

## Status

Accepted

---

## Context

Ziva Latam processes highly sensitive information, including:

- Personal identity data
- Financial documents
- Transactional behavior
- Income evidence
- Payment history

Storing and processing this data without strict separation introduces risks:

- Privacy breaches
- Data correlation attacks
- Unauthorized profiling
- Regulatory non-compliance risks
- Increased impact of data leaks

A strict separation model is required to reduce exposure and increase system resilience.

---

## Decision

Ziva Latam will implement a strict separation between:

### 1. Identity Layer

Contains:

- User personal information
- Verification attributes
- Legal identifiers (if applicable)
- Authentication data

This layer is:

- Highly restricted
- Encrypted at rest
- Access-controlled at the highest privilege level

---

### 2. Evidence Layer

Contains:

- Financial documents
- Transaction records
- Income proofs
- Payment behavior data
- External financial integrations (future)

This layer does NOT contain direct identity information.

---

### 3. Linkage Layer (Internal Mapping)

A system-generated internal identifier (UUID) is used to connect:

- Identity data
- Financial evidence
- Trust signals

This mapping is:

- Non-exposed externally
- Cryptographically protected
- Access-restricted
- Not reversible without authorization layer

---

## Core Principle

> Identity and financial behavior must never be stored or processed as a single unified dataset.

---

## Data Model Separation

### Identity Vault

- Stores personal identity data
- Encrypted and access-restricted
- Isolated from analytical systems

---

### Evidence Store

- Stores financial inputs and proofs
- Used for trust computation
- Does not expose personal identifiers directly

---

### Trust Engine

- Consumes evidence only
- Produces badges and signals
- Has no direct access to raw identity data

---

## Privacy Design Principles

### 1. Data Minimization
Only necessary data is stored per system layer.

---

### 2. Isolation
Identity and financial evidence are never directly accessible together.

---

### 3. Controlled Linking
All correlations between identity and evidence occur through internal system IDs.

---

### 4. Exposure Reduction
External systems (B2B) never access identity data.

They only access:

- Trust badges
- Aggregated signals
- Permissioned summaries

---

## Alternatives Considered

### 1. Unified User Profile Model

Rejected because:

- high risk of data exposure
- weak separation of concerns
- increased regulatory and breach impact

---

### 2. Partial Separation (soft boundaries)

Rejected because:

- still allows correlation attacks
- increases architectural ambiguity
- does not guarantee privacy isolation

---

### 3. No Separation (monolithic data model)

Rejected because:

- unacceptable privacy risk
- non-compliant with modern data protection principles
- incompatible with trust-based architecture

---

## Consequences

### Positive

- Strong privacy guarantees by design
- Reduced breach impact surface
- Better regulatory alignment
- Cleaner system architecture
- Enables safer B2B integrations

---

### Negative

- Increased architectural complexity
- Requires strict enforcement discipline
- Harder debugging across layers
- More careful system design required

---

## Impact on Architecture

This decision directly affects:

- Identity Layer design
- Evidence Layer design
- Trust Engine boundaries
- API exposure model
- Security architecture
- Data governance rules

---

## Related Domains

- Architecture
- Engineering
- Governance
- Product

---

## Notes

This ADR establishes one of the core principles of Ziva Latam:

The system does not "know everything" about the user in one place.

It intentionally separates knowledge to protect privacy and reduce risk.

---

## Status

Accepted
