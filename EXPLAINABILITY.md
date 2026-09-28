# GitAPISentry Explainability Specification

This document provides a transparent, verifiable architectural breakdown of how **GitAPISentry** operates, processes input, makes decisions, and enforces security boundaries.

---

## 1. Input Data and Data Sources Used

GitAPISentry consumes OpenAPI v3.0 and v3.1 specification files, Git commit diffs, JSON Schema payload definitions, and microservice route manifests. These data sources include endpoint paths, HTTP operation definitions, request body parameter constraints, and response status schemas. The agent ingests these inputs in raw JSON and YAML format and parses them into structured API abstract syntax trees for downstream contract analysis. Version release manifests and backward compatibility rules are also monitored as sensitive data sources to ensure client integration stability is strictly maintained.

---

## 2. How It Decides and Reasoning Process

The decision making process follows a deterministic, five-stage analytical pipeline designed to eliminate ambiguity and hallucination. When an API specification update is received, the agent first evaluates endpoint changes using the breaking-change-detector tool to identify removed routes, altered payload types, or newly required parameters. Next, the reasoning engine invokes the semver-drift-calculator tool to verify that proposed version numbers match detected change severity according to Semantic Versioning specifications. Furthermore, endpoint formatting is validated using the schema-syntax-validator tool. Finally, the agent correlates all schema differences against predefined API governance policies to issue a conclusive verdict of APPROVED, BLOCKED, or NEEDS_REVIEW alongside an automated compatibility report.

---

## 3. Constraints, Limitations, and Known Issues

GitAPISentry operates under strict operational constraints to prevent false positives and non-deterministic behavior across different agent frameworks. GitAPISentry operates under strict operational constraints to prevent breaking client integrations and undocumented API drift across microservices. The agent is deliberately limited to static contract and schema diffing and cannot monitor dynamic runtime network latency or backend database performance. Another known issue and limitation is that subtle semantic behavior alterations without schema changes may require secondary human review rather than autonomous blocking. Furthermore, the agent enforces a low temperature constraint of 0.1 to maintain strict predictability across all supported export frameworks.
