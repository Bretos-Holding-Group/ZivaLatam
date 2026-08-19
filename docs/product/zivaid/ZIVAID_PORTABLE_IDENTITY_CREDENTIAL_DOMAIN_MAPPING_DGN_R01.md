# ZivaID — Portable Identity & Credential Domain Mapping DGN-R01

**Status:** PROPOSED / NON-AUTHORITATIVE
**Product:** ZivaID
**Parent baseline:** `ZIVAID_CONCEPTUAL_FOUNDATION_v0.2.md`
**Purpose:** Descendant conceptual mapping
**Scope:** Information domains, credential roles, issuer boundaries, verifier access, disclosure limits, default-protection boundaries and a reserved future trust-mark capability.

## 1. Purpose

This mapping organizes the kinds of information ZivaID may eventually represent without granting ZivaID authority over facts determined by external issuers.

ZivaID may receive, preserve provenance for, correlate under controlled conditions, verify according to available methods, and present authorized evidence or derived assertions. It does not originate external authority, create legal status, certify facts it cannot establish, or replace an issuer's verification process.

## 2. Core disclosure rule

No domain is globally visible merely because it is associated with the same ZivaID.

Each request must be evaluated against:

- requester identity;
- credential/domain requested;
- stated purpose;
- applicable authority or legal basis;
- scope;
- jurisdiction;
- validity/freshness;
- verification strength;
- applicable user authorization or other lawful access basis;
- minimum information necessary.

Preferred order of disclosure:

1. derived assertion;
2. attribute-level response;
3. limited credential presentation;
4. underlying evidence only when specifically justified and permitted.

## 3. Domain map

| Domain | Examples | Typical issuer/source | Typical verifier/consumer | Preferred disclosure |
|---|---|---|---|---|
| Foundational identity | identity attributes, identity document | competent civil/identity authority | regulated or authorized service | minimum required identity attributes |
| Migration & residence | residence status, work authorization | competent migration authority | employer or authorized service | status/eligibility before document copy |
| Employment | employment relationship, role, income evidence | employer or competent institution | authorized financial/housing/service consumer | existence/status before full employment record |
| Financial & banking | account relationship, balances, transaction-derived evidence | financial institution or authorized source | authorized financial/service context | threshold/derived proof before raw balances |
| Credit | credit-history existence, issuer-specific credit evidence | competent credit/reporting source | authorized credit decision-maker | requirement-relevant proof; no universal score exposure |
| Housing | residence evidence, tenancy/history | landlord, registry, housing provider or competent source | authorized housing/financial consumer | eligibility/status before full history or address |
| Social security & insurance | affiliation, coverage, benefit status | competent public/private issuer | authorized service | coverage/eligibility assertion before detailed record |
| Education & professional | degree, enrollment, license/certification | institution or competent authority | employer or authorized verifier | credential validity before full academic record |
| Health | prescription, clinically relevant credential | competent health issuer | authorized clinical/pharmacy context | minimum clinically relevant assertion |
| Business & representation | organization identity, role, representation | registry, organization or competent authority | authorized business/service | representation validity before unrelated corporate data |

The list is extensible and does not authorize processing of any category merely because it appears here.

## 4. Issuer and verifier boundaries

### Issuer

The issuer or competent source remains responsible for the authority and meaning of the underlying credential, status or assertion.

### ZivaID

ZivaID is an infrastructure participant. Depending on the credential and permitted verification method, it may record, preserve provenance, validate structural consistency, verify against an available source, correlate evidence under controlled conditions, manage authorized presentation and communicate verification strength.

### Verifier/consumer

A verifier receives only an authorized presentation for a defined purpose. Receiving one credential does not grant access to other domains.

## 5. Disclosure levels

### Level A — Derived assertion

Examples: `ELIGIBLE`, `REQUIREMENT_SATISFIED`, `AGE_OVER_THRESHOLD`.

Default preference where sufficient.

### Level B — Minimal attributes

Only the attributes necessary to satisfy the verified purpose.

### Level C — Credential presentation

Limited credential fields with issuer, status, validity and verification context where justified.

### Level D — Restricted underlying evidence

Document images, raw records or equivalent source evidence. This is exceptional and requires a stronger, documented basis and applicable safeguards.

## 6. Never available by default

The following must not become globally discoverable, searchable or automatically disclosed simply because they are associated with a ZivaID:

- full identity-document copies;
- authentication secrets, passwords, private keys or recovery material;
- full financial transaction history;
- raw bank balances or account identifiers;
- complete credit history or unrestricted scoring data;
- complete medical history;
- precise location history;
- complete migration history;
- complete employment history;
- complete housing history;
- unrestricted cross-domain behavioral profiles;
- private evidence submitted for one purpose reused silently for another;
- any sensitive or legally restricted information requiring additional safeguards.

A future lawful and justified access mechanism does not make any of these categories default-visible.

## 7. Cross-domain correlation boundary

ZivaID must not treat possession of multiple credentials as blanket permission to profile, track or expose the participant across domains.

Correlation requires a defined purpose, appropriate authority, applicable controls and traceability. A service requesting financial evidence does not thereby acquire access to migration, health, housing or unrelated credentials.

## 8. Verification states

Future credential handling may distinguish at minimum:

- user-submitted;
- structurally checked;
- manually reviewed;
- source-verified;
- automated-source-verified;
- expired;
- revoked/invalid when reliably known;
- unknown/insufficient evidence.

These states describe evidence/verification conditions. They do not convert ZivaID into the authority that grants the underlying status.

## 9. Security and integrity baseline

This mapping establishes the following conceptual priorities:

1. least disclosure;
2. purpose limitation;
3. domain separation;
4. provenance preservation;
5. explicit verification strength;
6. access traceability;
7. no universal data access after authentication;
8. no silent cross-purpose reuse;
9. protection of security secrets from presentation flows;
10. escalation to higher governance where product behavior conflicts with applicable constraints.

## 10. Reserved future capability — ZivaID Trust Framework and Trust Mark

A future ZivaID trust capability may be explored, including a ZivaID Trust Framework, explicit verification or quality criteria, and a distinctive ZivaID Trust Mark or Seal.

This capability is reserved as a **future conceptual possibility only**.

Current status:

- **capability:** FUTURE / NOT ACTIVE;
- **current authority:** none is created by this mapping;
- **activation:** requires a separate governance gate and explicit approval;
- **scope:** must be defined before any mark, seal, rating or certification is issued or represented as active.

A future ZivaID Trust Mark must not be represented as a governmental, legal or regulatory certification unless such authority actually exists and is explicitly applicable.

If developed, the trust framework must separately define at minimum:

- what the mark means and does not mean;
- eligibility and evaluation criteria;
- evidence and verification requirements;
- issuer, evaluator and approval responsibilities;
- independence and conflict-of-interest controls where applicable;
- validity period, suspension, revocation and expiry rules;
- auditability and dispute or correction processes;
- permitted and prohibited use of the mark;
- jurisdiction-specific legal and intellectual-property review before launch.

A ZivaID Trust Mark, if ever activated, is distinct from the authority of an external issuer over the underlying fact, credential, authorization or legal status. A mark must communicate only the meaning established by its own approved criteria and must not imply external governmental or regulatory endorsement that does not exist.

Potential intellectual-property protection for a future name, symbol, mark or related system is outside the scope of this mapping and requires separate jurisdiction-specific analysis and approval.

## 11. Scope boundary

This artifact is a proposed descendant mapping. It does not establish a production privacy policy, legal basis, retention schedule, technical security architecture, cryptographic design, database schema, API contract, regulatory approval, authorization to process real sensitive data, or an active ZivaID Trust Mark.

Any promotion into policy, standard, architecture, implementation or trust-mark operation requires separate evidence, review and approval through the applicable governance chain.