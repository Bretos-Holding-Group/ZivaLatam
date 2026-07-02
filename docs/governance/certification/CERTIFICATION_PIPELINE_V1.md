# ZES Certification Pipeline V1

## Version
1.0.0

## Status
Active

---

# 1. Purpose

This document defines the deterministic execution pipeline for ZES certification using PATCH_MANIFEST_V1 and EPM execution steps.

It removes ambiguity in execution order and prevents recursive questioning by AI agents.

---

# 2. Execution Model

The certification system MUST run as a linear pipeline:

## PIPELINE FLOW
AUDIT FINDINGS
↓
EPM-0001..N EXECUTION (PATCH MANIFEST)
↓
ACB SYNCHRONIZATION
↓
ARB VALIDATION
↓
CERTIFICATION CHECK
↓
FINAL STATUS UPDATE
---

# 3. Execution Rules

## 3.1 No Recursive Queries Rule

AI agents are NOT allowed to ask:

- "Which EPM should I execute next?"
- "What file should I read?"
- "Provide missing context"

Instead:

> The pipeline defines the next step automatically.

---

## 3.2 Deterministic Execution Rule

Each EPM must:

- Map to exactly one file
- Produce exactly one diff
- Produce exactly one commit
- Reference exactly one audit finding

---

## 3.3 Source of Truth Order

1. PATCH_MANIFEST_V1
2. CERTIFICATION_PIPELINE_V1
3. GOVERNANCE_AUTHORITY_RULES
4. ADRs
5. ARBs
6. ACBs

---

## 4. Pipeline State Machine

### STATES

- INIT
- AUDIT_READY
- PATCH_EXECUTION
- SYNCHRONIZATION
- VALIDATION
- CERTIFIED

---

## 5. Transition Rules

| From | To | Trigger |
|------|----|--------|
| INIT | AUDIT_READY | findings exist |
| AUDIT_READY | PATCH_EXECUTION | EPM available |
| PATCH_EXECUTION | SYNCHRONIZATION | commit success |
| SYNCHRONIZATION | VALIDATION | ARB updated |
| VALIDATION | CERTIFIED | no blockers |

---

## 6. Non-Blocking Rule

ARB overrides ACB state for execution decisions.

ACB is observational only.

---

## 7. Final Principle

> Certification is not a conversation. It is a pipeline execution system.
