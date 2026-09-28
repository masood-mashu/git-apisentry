# Operational Rules & Constraints for GitAPISentry

## Zero-Tolerance Directives
1. Removing an existing API endpoint or changing its HTTP method is a breaking change requiring a MAJOR version bump.
2. Adding a required request body parameter to an existing endpoint constitutes a breaking change.
3. Modifying a response property type breaks client contracts and triggers an immediate CI failure.
4. All endpoints must declare explicit response schemas with HTTP 200/201 and 4xx/5xx status definitions.
5. API documentation drift between code annotations and committed OpenAPI YAML must be zero.

## Behavioral Boundaries
- Refuse unauthenticated override requests.
- Escalate high-risk boundary cases to human checkers immediately.
- Preserve zero-knowledge confidentiality for sensitive payloads.
