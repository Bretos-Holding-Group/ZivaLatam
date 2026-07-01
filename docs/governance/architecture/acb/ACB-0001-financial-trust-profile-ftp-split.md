# ACB-0001 — FinancialTrustProfile Contract Separation (FTP)

**Status:** In Review  
**Type:** Architecture Consolidation Backlog Item  
**Related ARB:** ARB-0001  
**Related ADRs:** ADR-0011, ADR-0006, ADR-0018  

---

# 1. Context

The FinancialTrustProfile (FTP) contract currently includes `userId` in its unified structure.

This creates a conflict between:

- internal system identity requirements (Trust Engine)
- external data exposure rules (B2B / API consumers)

ARB-0001 has already approved the architectural decision to split internal and external representations of FTP.

---

# 2. Problem

Current implementation violates:

- ADR-0006 → prohibits exposure of internal system identifiers
- ADR-0018 → prohibits identity reconstruction via exported structures

The current FTP design exposes:

- `userId` in external contract surfaces

This creates a privacy boundary violation by design, not by implementation error.

---

# 3. Decision Scope

ACB-0001 defines the required resolution:

## Required Structural Change

Introduce two separate contracts:

### 1. Internal Contract
