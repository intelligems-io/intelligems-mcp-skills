---
name: testing-strategy-health-check
description: Use when a user wants to evaluate the health of an Intelligems testing program, including velocity, win rate, test mix, learnings, and coverage gaps.
license: MIT
---

# Testing Strategy Health Check

Use this skill to assess whether an Intelligems testing program is producing useful learning and profit.

## Steps

1. Resolve organization and analysis period.
2. Pull completed, active, paused, and pending tests as needed with `search_experiences` or `search_experiments`.
3. Categorize tests by type, theme, funnel area, metric, and status.
4. Analyze outcomes for completed tests.
5. Identify bottlenecks: too few launches, too many inconclusive tests, narrow test mix, missing profit metrics, or unimplemented winners.

## Scorecard

Use a simple scorecard:

- Velocity: tests launched and completed per period.
- Quality: percent with clear hypothesis and metric fit.
- Win rate: winners, losers, inconclusive.
- Profit orientation: how often profit metrics are used.
- Coverage: pages, audiences, offers, pricing, content, and personalization.
- Follow-through: winners implemented and learnings reused.

## Output

Return:

1. Health grade with rationale.
2. Scorecard.
3. Biggest constraints.
4. Recommended operating changes.
5. Next tests or process improvements.
6. Source appendix.

Be candid. A healthy program can have losses if it is learning quickly and avoiding profit traps.

## Data Safety

Use only the user's authenticated MCP or API context. Do not save raw responses, exports, graph URLs, order data, customer data, or private store identifiers to the repository. Summarize findings and include experience IDs only when needed for the user's workflow.
