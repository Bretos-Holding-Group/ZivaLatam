# ZivaID — Version History

**Document status:** Controlled conceptual history
**Product:** ZivaID
**Brand / ecosystem:** Ziva / ZivaLatam
**Holding:** Breto's Holding Group (BHG)
**Governance chain:** ZivaID → ZivaLatam → BHG
**Supreme internal authority:** BHG Constitution

## Governance relationship

This history is subordinate to the governance hierarchy applicable to ZivaID:

```text
ZivaID
  ↑
ZivaLatam
  ↑
Breto's Holding Group (BHG)
  ↑
BHG Constitution — supreme internal governing authority
```

Version history may record product evolution but may not itself alter, bypass or supersede higher-level governance. A product-version change that affects authority, governance boundaries, delegation or constitutional alignment requires explicit governance review at the appropriate higher layer.

Applicable law and binding external obligations remain superior to internal corporate governance.

## v0.1 — Historical conceptual baseline

**Status:** Recorded from the approved conversational conceptual artifact; not independently verified at the time of repository registration.

v0.1 established the initial conceptual model of ZivaID as an interoperable identity, credential, trust, authorization and verification infrastructure.

It established the initial principles of:

- data sovereignty;
- non-appropriation of participant data;
- portability;
- interoperability;
- domain separation;
- contextual access;
- minimum disclosure;
- consent and temporary permissions;
- person and organization identity;
- credential provenance and trust;
- health-domain restrictions;
- auditability;
- non-surveillance;
- anti-lock-in.

The repository registration also records the product relationship as ZivaID → ZivaLatam → BHG. This governance relationship is a controlling context for subsequent product evolution and does not constitute independent certification of v0.1.

v0.1 is preserved as a historical artifact and must not be silently rewritten to incorporate later decisions.

## v0.2 — Product and ecosystem clarification

v0.2 preserves the v0.1 conceptual baseline and adds or clarifies:

1. **Product identity:** ZivaID is a product of ZivaLatam.
2. **Brand/ecosystem:** Ziva / ZivaLatam.
3. **Corporate hierarchy:** BHG → ZivaLatam → ZivaID/ZivaPay/ZivaOS/future products.
4. **Governance inheritance:** ZivaID is subordinate to ZivaLatam governance; ZivaLatam is subordinate to BHG governance and the BHG Constitution as the supreme internal governing authority.
5. **Non-override rule:** product documentation and engineering may not silently weaken, bypass or contradict higher-level BHG/ZivaLatam directives.
6. **Jurisdictional structure:** country-specific ZivaLatam legal/operational entities are not separate ZivaID products.
7. **No regionalized ZivaID products:** there is no conceptual product family such as ZivaID Chile, ZivaID Perú or ZivaID Colombia.
8. **Universal identity:** one ZivaID may authenticate a participant across compatible ZivaLatam services.
9. **Identity provider role:** ZivaID is intended to provide the reusable identity layer for compatible services.
10. **Authentication/authorization separation:** successful login does not grant universal data access.
11. **Credential reusability:** valid credentials may reduce repetitive onboarding and recertification where lawful and appropriate.
12. **Service-scoped requests:** each service requests only the credentials required for its own context and purpose.
13. **Policy evaluation:** ZivaID should determine what may be presented rather than exposing an unrestricted identity record.
14. **Progressive trust:** trust should be based on evidence, provenance, issuer authority, freshness and status.
15. **Financial ecosystem example:** ZivaPay may reuse eligible credentials for its own onboarding and assessment, while retaining responsibility for its financial decisions and regulatory obligations.
16. **Portability clarification:** portability is across compatible jurisdictions/infrastructure, not migration between country-specific ZivaID products.
17. **Individual and business identity:** both people and organizations are first-class conceptual participants.
18. **Health boundary:** health examples remain conceptual and require separate legal, regulatory, security and clinical validation before implementation.

## Verification and merge closure

**v0.2 verification status:** Independently verified in the second-round review associated with PR #2.

**PR:** #2 — `docs(product): establish ZivaID conceptual foundation v0.1 and v0.2`

**Base SHA:** `fb986b276552a38e9016442301358700e554d4f8`

**Verified head SHA:** `7b5cb5944807aa2de7852abd5d0b0caa916366ef`

**Merge commit:** `aa7a89e6dd7015e9972e0955a0209eb812fc59e9`

**Merge state:** merged into `main`.

This closure records documentary and governance verification of the conceptual baseline. It does not constitute legal, regulatory, security, clinical, financial or market certification.

## Versioning rule

Historical versions must remain immutable in substance. Future conceptual changes require a new version and an explicit change record. No version may silently overwrite an earlier baseline.

If a historical artifact requires repository normalization for governance metadata or traceability, that normalization must be explicitly recorded and must not retroactively insert later product decisions into the historical substantive content.

## Verification rule

Repository registration, authoring review, pre-verification review and independent verification are separate states. A version may be recorded in Git without being certified. Certification requires an explicit verification result after the documented version has passed its review stage.

## Governance-change rule

Any proposed ZivaID change that could alter the product's relationship with ZivaLatam, BHG, the BHG Constitution, delegated authority or governance boundaries must be treated as a governance change in addition to a product change. It must be escalated to the appropriate authority and recorded with explicit lineage before becoming effective.
