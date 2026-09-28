# Explainability & Governance Statement

## Decision Architecture
GitAPISentry evaluates API contracts through structured tree diffing of OpenAPI schema models. When two spec versions are compared, removed paths and altered property types are flagged as breaking. The agent cross-references the proposed version string (e.g. 1.2.0 vs 2.0.0) against SemVer rules to ensure clients will not encounter unhandled runtime failures.

## Input Data Provenance
Data inputs include OpenAPI v3.x specification files, Git commit diffs, and package version manifests.

## Operational Limits & Non-Goals
GitAPISentry verifies static API contract specifications; it does not measure dynamic network latency or backend database query performance.
