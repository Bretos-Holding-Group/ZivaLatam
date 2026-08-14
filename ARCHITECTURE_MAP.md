---
title: Ziva Latam Architecture Map
document_id: ZIVA_ARCHITECTURE_MAP
version: 0.1.0
status: Draft
document_type: Repository Architecture Map
governance_level: Product
owner: Ziva Latam Engineering
approval_authority: Ziva Engineering Authority within delegated scope
created: 2026-08-14
last_updated: 2026-08-14
effective_date: null
classification: Internal
language: en
repository: ZivaLatam

governed_by:
  - BHG_REPOSITORY_AUTHORITY_SEQUENCE
depends_on: []
related_to:
  - BHG-GOV-CAM-001
  - BHG-Ecosystem-Foundation
  - ZIVA_ENGINEERING_CHARTER
---

# Ziva Latam Architecture Map

## 1. Purpose

This document defines the repository architecture of Ziva Latam and its position in the BHG cross-repository authority sequence.

It is a local architecture contract. It does not create BHG-wide governance authority.

## 2. Authority position

ZivaLatam is a product and engineering specialization repository.

Its local authority sequence is:

```text
BHG Constitution
    ↓
BHG foundational architecture / applicable Foundation contracts
    ↓
BHG Governance policies and standards
    ↓
Ziva Engineering Charter and local governance
    ↓
Ziva architecture / ADRs / domain contracts
    ↓
Implementation
    ↓
Tests / operational evidence
```

The local Engineering Charter is the highest authority **inside the delegated Ziva engineering scope**. It is not an independent constitutional root.

## 3. Materialized architecture

The repository currently contains, among other implementation-supporting areas:

```text
config/
docs/
  00_ENGINEERING_CHARTER.md
  architecture/
    adr/
    blueprints/
    decisions/
  governance/
    architecture/
```

The existing ADR and architecture corpus remains historical/current working material and is subject to normalization against the authority sequence.

## 4. Domain boundaries

Ziva architecture may define:

- product and system architecture;
- domain contracts;
- trust and security architecture;
- engineering decisions;
- implementation architecture;
- Ziva-specific operational rules.

It must not redefine:

- BHG constitutional authority;
- BHG-wide document metadata semantics;
- BHG-wide relationship semantics;
- enterprise governance approval mechanics;
- Foundation institutional architecture outside delegated Ziva scope.

## 5. New-document gate

Before creating a new Ziva normative, architecture or engineering document:

1. identify the document's local domain;
2. identify the applicable BHG superior contract;
3. verify that the subject has no existing canonical owner;
4. classify the document as policy, standard, architecture, ADR, contract, procedure or implementation artifact;
5. use canonical metadata and relationship vocabulary;
6. declare the local specialization boundary;
7. create the change on a non-main branch;
8. validate authority, dependencies, references and consistency;
9. preserve the decision and change history.

## 6. ADR rule

An ADR records a decision within the Ziva delegated engineering scope. An ADR does not become a superior governance artifact merely because it is accepted.

Where an ADR conflicts with an applicable BHG policy or standard, the higher applicable authority prevails and the ADR must be revised or formally escalated.

## 7. Documentation-first rule

No implementation work shall be treated as authoritative until the governing documentation and applicable architecture contracts have been resolved.

Unresolved normative ambiguity is a blocker for downstream implementation when the implementation depends on that ambiguity.

## 8. Status

```text
status: DRAFT
canonical: false
effective: false
automation_ready: false
```
