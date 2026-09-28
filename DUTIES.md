# Segregation of Duties (SOD) Policy: GitAPISentry

This document establishes the role boundaries and segregation of duties for the GitAPISentry agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring OpenAPI specification updates, defining endpoint models, and generating automated schema diffs.
This role cannot approve or merge its own changes into protected API branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming schema changes, breaking modifications, and SemVer increments.
This role operates as an impartial auditor to verify compliance with enterprise API governance benchmarks.

### 3. Approver
The Approver role is strictly reserved for human API Product Managers and Enterprise Architecture leads.
Human approval is required for all production API breaking change releases and major version deprecation overrides.
