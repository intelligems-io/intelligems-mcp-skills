---
name: weekly-test-pulse
description: Use when a brand operator or agency asks for a quick weekly status report on running Intelligems tests and recommended next actions.
license: MIT
---

# Weekly Test Pulse

Use this skill for a concise status report on tests that are currently running.

## Steps

1. Resolve the organization. If ambiguous, use `list_organizations` and ask for the target.
2. Find running tests with `search_experiments` or `search_experiences` using `status: "started"`.
3. For each running test, fetch details with `get_experience` and metrics with `analyze_experience`.
4. Use `get_experience_metrics_config` when you need the correct analytics view type or primary metric.
5. Group tests into: likely winner, likely loser, inconclusive, needs more data, and needs attention.

## Watchouts

- Do not recommend ending a test solely from early conversion lift.
- Check RPV, GPV, net revenue, AOV, and confidence when available.
- Call out tests with low traffic, uneven traffic allocation, missing profit metrics, or suspicious segment concentration.
- If a lifecycle action is needed, recommend it but do not run `experience_action` without explicit approval.

## Data Safety

Use only the user's authenticated MCP or API context. Do not save raw responses, exports, graph URLs, order data, customer data, or private store identifiers to the repository. Summarize findings and include experience IDs only when needed for the user's workflow.

## Output

Return:

1. One-paragraph pulse summary.
2. Table of running tests with status, leading variation, metric direction, confidence, and recommendation.
3. Risks or anomalies.
4. Exact next actions for the coming week.
5. Source appendix with organization, date range, and tool calls.
