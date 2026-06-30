# ADR-0004: Evidence Ingestion Model

## Status

Accepted

---

## Context

Ziva Latam relies on financial evidence to generate trust signals and badges.

However, financial data does not exist natively inside the system. It must be:

- collected
- validated
- normalized
- stored
- processed into trust signals

A clear ingestion model is required to ensure:

- consistency of data
- scalability of inputs
- reliability of trust outputs
- gradual system evolution from manual to automated ingestion

---

## Decision

Ziva Latam will implement a **multi-stage Evidence Ingestion Model** starting with manual input and progressively evolving into automated financial integrations.

---

## Ingestion Stages

### Stage 1: Manual Evidence Input (MVP Phase)

Users can submit financial evidence manually.

Supported inputs:

- Uploaded documents (receipts, invoices, contracts)
- Payment confirmations
- Income declarations
- Screenshots or digital proofs
- Structured form inputs

All inputs are:

- validated manually or semi-automatically
- stored as raw evidence
- linked to internal user ID (not identity layer directly exposed)

---

### Stage 2: Semi-Automated Integration

System begins integrating with external financial platforms such as:

- Payment processors (e.g., MercadoPago-like systems)
- Banking data aggregators (future)
- Payroll systems (future)

At this stage:

- data is partially structured
- validation rules are standardized
- ingestion pipelines are introduced

---

### Stage 3: Full API-Based Ingestion

Ziva introduces native APIs (e.g. ZivaPay, ZivaOS integrations) allowing:

- real-time transaction ingestion
- automated income verification
- continuous financial behavior tracking

---

## Evidence Validation Pipeline

All incoming evidence must pass through:

### 1. Format Validation
Ensures data is structurally valid.

---

### 2. Authenticity Checks
Basic fraud detection and consistency validation.

---

### 3. Normalization
Standardizes data into internal formats.

---

### 4. Storage Routing
Routes evidence into Evidence Layer (not Identity Layer).

---

### 5. Trust Engine Processing
Evidence is consumed by Trust Engine to generate:

- badges
- behavioral signals
- trust indicators

---

## Core Principle

> Evidence is never trusted by default. It must be validated before it becomes part of the trust system.

---

## Design Principles

### 1. Progressive Automation
System starts manual and evolves toward full automation.

---

### 2. Source Flexibility
Evidence can originate from multiple input channels.

---

### 3. Validation First
No evidence is usable without passing validation pipeline.

---

### 4. Decoupling
Ingestion is independent from trust computation.

---

### 5. Extensibility
New data sources can be added without modifying core architecture.

---

## Alternatives Considered

### 1. Fully Automated Ingestion from Day 1

Rejected because:

- requires integrations not yet available
- increases complexity prematurely
- blocks MVP validation
- introduces unnecessary infrastructure risk

---

### 2. Manual-Only System

Rejected because:

- does not scale
- limits product evolution
- increases user friction over time

---

### 3. Unstructured Data Intake

Rejected because:

- reduces trust accuracy
- complicates validation
- increases fraud risk

---

## Consequences

### Positive

- enables MVP with minimal infrastructure
- allows gradual system evolution
- reduces early technical risk
- supports flexible onboarding of users
- aligns with real-world constraints (low-resource environments)

---

### Negative

- manual validation overhead in early stages
- slower trust generation initially
- requires future migration to automated systems

---

## Impact on Architecture

This ADR affects:

- Evidence Layer design
- Trust Engine processing pipeline
- Future API Gateway design
- ZivaPay integration roadmap
- Data normalization standards

---

## Evolution Path

This model is explicitly designed to evolve into:

- ZivaPay ingestion APIs
- ZivaOS financial connectors
- Real-time financial event streaming system

---

## Related Domains

- Architecture
- Engineering
- Product
- Governance

---

## Status

Accepted
