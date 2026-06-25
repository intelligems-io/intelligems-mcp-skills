---
name: api-integration-builder
description: Use when a user wants to build scripts, dashboards, alerts, or data pipelines with the Intelligems External API and needs source-backed endpoint guidance.
license: MIT
---

# API Integration Builder

Use this skill when building or reviewing code that calls the Intelligems External API.

## First Moves

1. Load `references/external-api.md`.
2. Confirm the integration goal: reporting, monitoring, dashboarding, lifecycle automation, or data export.
3. Confirm whether the task is read-only. Creating, updating, starting, pausing, or ending experiences requires explicit user approval.
4. Use `INTELLIGEMS_ACCESS_TOKEN` or another environment variable. Never hardcode tokens.

## Request Pattern

Base URL:

```text
https://api.intelligems.io
```

Header:

```text
intelligems-access-token: $INTELLIGEMS_ACCESS_TOKEN
```

## Implementation Rules

- Read the OpenAPI spec when endpoint shape matters.
- Handle `400`, `401`, `404`, `429`, and `500`.
- Respect rate-limit headers: `x-ratelimit-limit`, `x-ratelimit-remaining`, and `x-ratelimit-reset`.
- Prefer typed clients or schema validation for production integrations.
- Keep raw API responses out of tracked files unless anonymized.
- Log request IDs, endpoint names, and high-level status, not tokens or private payloads.
- Treat export URLs, generated graphs, raw JSON, order-level CSVs, and line-item CSVs as private data.

## Output For Code Tasks

When producing code, include:

1. Environment variables required.
2. Endpoint list used.
3. Error handling.
4. Rate-limit handling.
5. Validation or test plan.
6. Safety note for any mutating endpoint.
