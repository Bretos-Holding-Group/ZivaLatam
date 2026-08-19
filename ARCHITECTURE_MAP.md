---
title: Ziva Latam Architecture Map
document_id: ZIVA_ARCHITECTURE_MAP
version: 0.1.0
status: Draft
document_type: Repository Architecture Map
governance_level: Product
owner: Ziva Latam Engineering
approval_authority: Ziva Engineering Authority within delegated scope
created: 2026-08-19
last_updated: 2026-08-19
effective_date: null
classification: Internal
language: en
repository: ZivaLatam

governed_by:
  - BHG_REPOSITORY_AUTHORITY_SEQUENCE
depends_on:
  - BHG-Ecosystem-Foundation
related_to:
  - BHG-GOV-CAM-001
  - ZIVA_ENGINEERING_CHARTER
---

# Ziva Latam Architecture Map

## 1. Purpose

This document defines the repository architecture of Ziva Latam and its position within the applicable BHG authority sequence.

It is a local architecture contract. It does not create BHG-wide governance authority.

## 2. Institutional position

ZivaLatam is currently an independent operational entity and is not a present BHG subsidiary. It is intentionally designed for compatibility with BHG architecture and governance and is classified by the BHG identity model as `INDEPENDENT / FUTURE-INTEGRATION-CANDIDATE`.

Future integration, if pursued, requires a separate formal institutional and legal process. This architecture map does not create ownership, control, subsidiary status, legal subordination, or present BHG governance authority over ZivaLatam.

## 3. Local authority position

Within the delegated Ziva engineering scope, the local authority sequence is:

```text
Applicable BHG Constitution / Governance
    ↓
Applicable BHG Foundation contracts
    ↓
Ziva Engineering Charter and local governance
    ↓
Ziva architecture / ADRs / domain contracts
    ↓
Implementation
    ↓
Tests / operational evidence
```

The Ziva Engineering Charter is the highest authority inside the delegated Ziva engineering documentation scope. It is not an independent constitutional or enterprise governance root.

## 4. Domain boundaries

Ziva architecture may define:

- product and system architecture;
- domain contracts;
- trust and security architecture;
- engineering decisions;
- implementation architecture;
- Ziva-specific operational rules within delegated scope.

It must not redefine:

- BHG constitutional authority;
- BHG-wide document metadata semantics;
- BHG-wide relationship semantics;
- enterprise governance approval mechanics;
- Foundation institutional architecture outside delegated Ziva scope.

## 5. New-document gate

Before creating a new Ziva normative, architecture, or engineering document:

1. identify the document's local domain;
2. identify the applicable superior BHG contract;
3. verify that the subject has no existing canonical owner;
4. classify the document as policy, standard, architecture, ADR, contract, procedure, or implementation artifact;
5. use canonical metadata and relationship vocabulary;
6. declare the local specialization boundary;
7. create the change on a non-main branch;
8. validate authority, dependencies, references, and consistency;
9. preserve the decision and change history.

## 6. ADR rule

An ADR records a decision within the Ziva delegated engineering scope. An ADR does not become a superior governance artifact merely because it is accepted.

Where an ADR conflicts with an applicable BHG policy or standard, the higher applicable authority prevails and the ADR must be revised or formally escalated.

## 7. Documentation-first rule

No implementation work shall be treated as authoritative until the governing documentation and applicable architecture contracts have been resolved.

Unresolved normative ambiguity is a blocker for downstream implementation when implementation depends on that ambiguity.

## 8. Status

```text
status: DRAFT
canonical: false
effective: false
automation_ready: false
```
