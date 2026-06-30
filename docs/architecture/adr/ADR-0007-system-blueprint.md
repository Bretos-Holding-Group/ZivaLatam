# ADR-0007: System Blueprint

## Status

Accepted

---

## Context

Ziva Latam has defined:

- a Trust Model (badges instead of scores)
- a Privacy Architecture (identity-evidence separation)
- an Evidence Ingestion Model
- a Trust Engine Processing Model
- a B2B Exposure Model

However, the system lacks a unified structural blueprint that connects all components into a coherent platform.

A high-level system architecture is required to define how all modules interact in practice.

---

## Decision

Ziva Latam will be implemented as a modular, service-oriented system composed of independent but interconnected components.

Each component has a single responsibility and communicates through controlled interfaces.

---

## Core System Modules

### 1. Identity Service

Responsible for:

- user identity registration
- authentication
- identity verification status
- secure identity storage (Identity Vault)

Does NOT handle financial data.

---

### 2. Evidence Service

Responsible for:

- ingestion of financial documents
- validation of evidence
- normalization of inputs
- storage of financial behavior data

Does NOT expose identity information.

---

### 3. Trust Engine Service

Responsible for:

- processing validated evidence
- generating trust badges
- applying deterministic rule engine
- maintaining explainability logs

Does NOT access identity vault directly.

---

### 4. API Gateway (B2B Layer)

Responsible for:

- exposing trust profiles to external systems
- enforcing privacy rules
- filtering sensitive data
- providing structured trust responses

Does NOT expose raw data or internal IDs.

---

### 5. Orchestration Layer

Responsible for:

- coordinating workflows between services
- handling asynchronous processes
- ensuring consistency across modules
- managing system events

---

## End-to-End System Flow

### Step 1: User Input

User submits financial evidence (manual or future integrations)

↓

### Step 2: Evidence Service

Evidence is validated and stored in Evidence Layer

↓

### Step 3: Trust Engine

Evidence is processed into structured trust badges

↓

### Step 4: Trust Profile Assembly

Badges are aggregated into Financial Trust Profile (FTP)

↓

### Step 5: API Gateway

B2B systems request trust profile

↓

### Step 6: External Consumption

External institutions receive anonymized trust signals

---

## Core Architectural Principle

> Each system module must have a single responsibility and no direct access to unauthorized layers.

---

## Data Flow Rules

- Identity data never flows into Trust Engine
- Evidence data never flows into API Gateway unfiltered
- Trust Engine only consumes validated evidence
- API Gateway only consumes trust outputs
- Orchestration layer coordinates but does not store sensitive data

---

## System Design Principles

### 1. Modularity
Each service can evolve independently.

---

### 2. Isolation
No shared direct database access between modules.

---

### 3. Controlled Communication
All interactions happen through defined interfaces.

---

### 4. Auditability
Every transformation from evidence to trust must be traceable.

---

### 5. Stateless Interfaces (where possible)
Services should avoid unnecessary state coupling.

---

## Alternatives Considered

### 1. Monolithic Architecture

Rejected because:

- reduces scalability
- increases coupling between domains
- complicates evolution of trust system

---

### 2. Microservices with shared database

Rejected because:

- breaks isolation principle
- increases risk of cross-module leakage
- reduces security boundaries

---

### 3. Event-driven only architecture

Rejected because:

- increases complexity for MVP stage
- requires infrastructure not yet justified
- difficult to debug in early phases

---

## Consequences

### Positive

- clear separation of concerns
- scalable long-term architecture
- strong security boundaries
- easier onboarding of developers
- aligns with future fintech expansion

---

### Negative

- requires careful service design discipline
- higher initial implementation complexity
- requires strong API contract management
- introduces orchestration overhead

---

## Impact on System

This ADR defines the real structure of:

- backend architecture
- service boundaries
- data flow design
- integration strategy
- scalability roadmap

---

## Core Principle

> Ziva is not a monolith. It is a trust infrastructure composed of isolated, explainable services.
