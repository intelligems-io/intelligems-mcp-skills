---
name: profit-growth-audit
description: Use when a user asks for a profit-focused Intelligems audit that ranks test wins, profit traps, and implementation opportunities from MCP or API data.
license: MIT
---

# Profit Growth Audit

Use this skill to produce a profit-focused audit of Intelligems testing data.

The official public source for this artifact is:

```text
https://github.com/intelligems-io/profit-growth-audit
```

## Workflow

1. Load MCP context if the session has Intelligems MCP access.
2. Confirm organization, date range, and whether the user wants running tests, ended tests, or both.
3. Discover relevant experiences with `search_experiences` or `search_experiments`.
4. For each candidate, fetch configuration and metric context with `get_experience`, `get_experience_metrics_config`, and `analyze_experience`.
5. Pull audience views only when they help explain the profit outcome.
6. Rank opportunities by profit impact, confidence, and implementation readiness.

## What To Look For

- Winners with meaningful RPV, GPV, or net revenue lift.
- "Conversion winners" that reduce RPV, GPV, or net revenue.
- Tests that are directionally promising but underpowered.
- Winners not yet implemented.
- Segment-specific opportunities that are stronger than aggregate results.
- Tests that should be extended, ended, or followed up.

## Output

Return:

1. Executive summary.
2. Ranked profit opportunities.
3. Profit traps or warnings.
4. Segment findings.
5. Recommended next actions.
6. Source appendix with organization, date range, experience IDs, tool calls, and missing data.

Do not call a test a profit win unless profit-oriented metrics support it. If only conversion rate is available, label the finding as incomplete and ask for the missing metric path.

## Data Safety

Use only the user's authenticated MCP or API context. Do not save raw responses, exports, graph URLs, order data, customer data, or private store identifiers to the repository. Summarize findings and include experience IDs only when needed for the user's workflow.

## References

Load `references/profit-growth-framework.md` when you need the audit rubric.
