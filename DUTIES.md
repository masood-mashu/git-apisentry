# Separation of Duties for GitAPISentry

## Maker Role: APIEngineer
APIEngineer who introduces schema definitions, endpoints, and microservice payload updates.

## Checker Role: APIGovernanceLead
APIGovernanceLead who audits breaking schema changes, SemVer parity, and backward compatibility.

## Dual-Control Verification Pipeline
1. Parse OpenAPI 3.0/3.1 JSON/YAML specifications across Git branches.
2. Compare path operations, parameters, and response schemas between baseline and candidate specs.
3. Categorize contract differences into Breaking, Additive, or Non-breaking changes.
4. Verify that candidate semantic version numbers strictly match detected change severity.
