---
name: test-roadmap
description: Use when a user wants a prioritized Intelligems testing roadmap based on historical results, untested areas, customer segments, and profit opportunities.
license: MIT
---

# Test Roadmap

Use this skill to create a practical next-test plan.

## Steps

1. Resolve organization, planning horizon, and business goal.
2. Review recent completed tests with `search_experiences` or `search_experiments`.
3. Analyze winners, losers, and inconclusive tests with `analyze_experience`.
4. Look for patterns by test type, theme, audience, offer, price, page, and funnel step.
5. Check current active tests so recommendations do not duplicate work.
6. Prioritize test ideas by expected profit impact, learning value, confidence, effort, and risk.

## Roadmap Format

Return:

1. Strategy summary.
2. Findings from historical tests.
3. Prioritized test backlog.
4. 30/60/90 day roadmap.
5. Measurement plan and primary metrics.
6. Data gaps and assumptions.

Each test idea should include:

- Hypothesis.
- Target audience or page.
- Primary metric.
- Expected impact.
- Required assets or implementation work.
- Risk and guardrail metrics.

Do not suggest mutating live experiences. This skill plans; it does not create or launch tests.

## Data Safety

Use only the user's authenticated MCP or API context. Do not save raw responses, exports, graph URLs, order data, customer data, or private store identifiers to the repository. Summarize findings and include experience IDs only when needed for the user's workflow.
