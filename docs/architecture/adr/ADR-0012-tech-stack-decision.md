# ADR-0012: Tech Stack Decision

## Status

Accepted

---

## Context

Ziva Latam has defined:

- Architecture (System Blueprint)
- Contracts (Domain Specification)
- MVP scope (strict boundaries)
- Execution model (MXL)

However, the system cannot be implemented without selecting a concrete technology stack that satisfies:

- free usage constraints
- mobile development compatibility
- GitHub-based workflow
- simple deployment pipeline
- scalability toward fintech infrastructure

---

## Decision

Ziva Latam will use a **TypeScript-first full-stack JavaScript ecosystem** for the MVP.

This stack is selected based on simplicity, ecosystem maturity, and compatibility with low-resource development environments.

---

## Core Tech Stack

### 1. Language

**TypeScript**

Reason:

- strict typing aligns with Domain Contracts
- reduces runtime errors
- widely supported in free tooling
- strong ecosystem for backend + frontend

---

### 2. Backend Runtime

**Node.js**

Reason:

- lightweight
- widely supported
- easy deployment
- works in serverless environments

---

### 3. API Framework

**Fastify (preferred) or Express (fallback)**

Reason:

- minimal overhead
- easy to structure modular services
- compatible with MXL design

---

### 4. Database

**PostgreSQL**

Reason:

- strong relational model for evidence + trust systems
- supports complex queries
- free tiers available (Supabase / Neon)

Recommended provider:

- Supabase (primary option)

---

### 5. Authentication / Identity Layer

**Supabase Auth (initial MVP)**

Reason:

- free tier available
- reduces infrastructure complexity
- integrates well with PostgreSQL

---

### 6. Deployment

**Vercel (API + frontend)**

Reason:

- free tier
- GitHub integration
- simple CI/CD
- mobile-friendly workflow

---

### 7. File Storage (Evidence Uploads)

**Supabase Storage**

Reason:

- handles document uploads
- integrates with DB
- no custom infra needed for MVP

---

### 8. Development Environment

- GitHub (source control)
- GitHub Codespaces (optional)
- Mobile editing via GitHub app / browser
- Optional: Cursor / VSCode later

---

## System Architecture Mapping

| Layer | Technology |
|------|-----------|
| Identity | Supabase Auth |
| Evidence Storage | PostgreSQL + Supabase Storage |
| Trust Engine | Node.js (TypeScript modules) |
| API Layer | Fastify / Express |
| Deployment | Vercel |
| Database | PostgreSQL |

---

## Core Principle

> Technology must serve architecture, not define it.

---

## Constraints Alignment

This stack satisfies:

- mobile-first development (GitHub + web tools)
- zero-cost MVP execution
- minimal infrastructure overhead
- scalability path toward fintech-grade systems
- compatibility with ADR-defined modular architecture

---

## Alternatives Considered

### 1. Python-based backend

Rejected because:

- weaker integration with Vercel
- more complex deployment pipeline
- less unified full-stack ecosystem for MVP

---

### 2. Java / Spring Boot

Rejected because:

- heavy infrastructure requirements
- not suitable for rapid MVP iteration
- high complexity for solo development

---

### 3. Microservices from day 1

Rejected because:

- violates MVP scope constraints
- unnecessary operational overhead
- increases deployment complexity

---

## Consequences

### Positive

- fast MVP implementation path
- minimal infrastructure cost
- strong developer ecosystem support
- easy GitHub-based workflow
- scalable toward production systems

---

### Negative

- reliance on JavaScript ecosystem limitations
- requires discipline to avoid monolithic spaghetti code
- performance not optimized for high-scale fintech yet
- future refactor may be required for enterprise scaling

---

## Impact on System

This ADR defines:

- implementation language
- runtime environment
- database strategy
- deployment pipeline
- concrete execution path for MXL (ADR-0010)

---

## Core Principle

> Architecture defines the system. Stack only enables it.
