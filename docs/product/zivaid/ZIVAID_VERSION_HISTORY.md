# ZivaID — Version History

**Document status:** Controlled conceptual history
**Product:** ZivaID
**Brand / ecosystem:** Ziva / ZivaLatam
**Holding:** Breto's Holding Group (BHG)

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

v0.1 is preserved as a historical artifact and must not be silently rewritten to incorporate later decisions.

## v0.2 — Product and ecosystem clarification

v0.2 preserves the v0.1 conceptual baseline and adds or clarifies:

1. **Product identity:** ZivaID is a product of ZivaLatam.
2. **Brand/ecosystem:** Ziva / ZivaLatam.
3. **Corporate hierarchy:** BHG → ZivaLatam → ZivaID/ZivaPay/ZivaOS/future products.
4. **Jurisdictional structure:** country-specific ZivaLatam legal/operational entities are not separate ZivaID products.
5. **No regionalized ZivaID products:** there is no conceptual product family such as ZivaID Chile, ZivaID Perú or ZivaID Colombia.
6. **Universal identity:** one ZivaID may authenticate a participant across compatible ZivaLatam services.
7. **Identity provider role:** ZivaID is intended to provide the reusable identity layer for compatible services.
8. **Authentication/authorization separation:** successful login does not grant universal data access.
9. **Credential reusability:** valid credentials may reduce repetitive onboarding and recertification where lawful and appropriate.
10. **Service-scoped requests:** each service requests only the credentials required for its own context and purpose.
11. **Policy evaluation:** ZivaID should determine what may be presented rather than exposing an unrestricted identity record.
12. **Progressive trust:** trust should be based on evidence, provenance, issuer authority, freshness and status.
13. **Financial ecosystem example:** ZivaPay may reuse eligible credentials for its own onboarding and assessment, while retaining responsibility for its financial decisions and regulatory obligations.
14. **Portability clarification:** portability is across compatible jurisdictions/infrastructure, not migration between country-specific ZivaID products.
15. **Individual and business identity:** both people and organizations are first-class conceptual participants.
16. **Health boundary:** health examples remain conceptual and require separate legal, regulatory, security and clinical validation before implementation.

## Versioning rule

Historical versions must remain immutable. Future conceptual changes require a new version and an explicit change record. No version may silently overwrite an earlier baseline.

## Verification rule

Repository registration, authoring review and independent verification are separate states. A version may be recorded in Git without being certified. Certification requires an explicit verification result after the documented version has passed its review stage.
