# ADR-0010: Minimum Executable System Layout (MXL)

## Status

Accepted

---

## Context

Ziva Latam has a fully defined architecture, domain separation, and MVP scope.

However, there is currently no defined **minimum executable system** that allows:

- validating end-to-end flows
- testing trust generation logic
- simulating evidence ingestion
- verifying badge generation
- proving system viability before tech stack selection

A minimal execution layer is required.

---

## Decision

Ziva Latam will define a **Minimum Executable System Layout (MXL)** that represents the smallest possible runnable version of the system.

This layout is independent of any technology stack.

---

## Core Principle

> The system must be able to simulate a full trust lifecycle before choosing production technology.

---

## Minimum Executable Flow

The system must support the following flow:

```text
User Input (Manual Evidence)
        ↓
Evidence Validation (Basic Rules)
        ↓
Trust Engine (Rule-Based Logic)
        ↓
Badge Generation
        ↓
Financial Trust Profile (FTP)
        ↓
B2B API Simulation Output
```

---

## Required System Components (Logical Only)

### 1. Input Handler

- Accepts structured manual evidence
- Simulates user submission
- No external dependencies required

---

### 2. Evidence Processor

- Validates input format
- Normalizes data into internal structure
- Prepares data for Trust Engine

---

### 3. Trust Engine Core

- Rule-based badge generation
- Deterministic logic only
- No external integrations

---

### 4. Profile Builder

- Aggregates badges into FTP structure
- Generates final trust representation

---

### 5. API Simulation Layer

- Simulates B2B response format
- No real network exposure required initially
- Used for validation of output contract

---

## Execution Constraint

This system must be runnable in:

- local development environment
- minimal runtime setup
- zero external dependencies (initial phase)

---

## Data Flow Constraint

At no point in the MXL:

- identity data is exposed externally
- raw evidence leaves system boundaries
- trust logic depends on external APIs
- scoring systems are introduced

---

## Why This Exists

This layer ensures:

- validation before technology selection
- reduction of architectural risk
- early detection of design flaws
- independence from infrastructure decisions

---

## Alternatives Considered

### 1. Selecting Tech Stack First

Rejected because:

- locks implementation prematurely
- biases architecture toward tools instead of design
- reduces flexibility

---

### 2. Skipping Executable Layer

Rejected because:

- architecture remains theoretical
- no way to validate trust model behavior
- increases risk of late-stage redesign

---

### 3. Full Infrastructure Setup Immediately

Rejected because:

- unnecessary complexity
- premature optimization
- misalignment with MVP scope

---

## Consequences

### Positive

- enables system validation before implementation
- decouples architecture from technology
- reduces early development risk
- ensures MVP correctness before scaling

---

### Negative

- requires abstraction discipline
- delayed tech stack decisions
- initial lack of production realism

---

## Impact on System

This ADR defines:

- how the MVP will be executed logically
- the minimum structure required for implementation
- the validation layer before real development
- the boundary between design and implementation

---

## Core Principle

> If the system cannot run conceptually, it should not be built technically.

---

## Status

Accepted
