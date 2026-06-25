---
name: profit-trap-detection
description: Use when a user wants to find Intelligems tests where conversion rate improved but revenue per visitor, gross profit, or another profit metric declined.
license: MIT
---

# Profit Trap Detection

Use this skill to catch harmful winners before they are implemented.

## Steps

1. Resolve organization and date range.
2. Search ended and active experiments relevant to the request.
3. For each test, fetch overview metrics with `analyze_experience`.
4. Compare conversion rate, RPV, GPV, AOV, net revenue, and confidence where available.
5. Investigate audience breakdowns if the aggregate result hides a segment problem.

## Profit Trap Definition

Flag a test when:

- Conversion rate increases but RPV decreases.
- Conversion rate increases but GPV or margin proxy decreases.
- Order volume increases but AOV drops enough to reduce value.
- A discount, offer, or shipping change wins on orders but loses on profit.
- A strong segment winner masks broad underperformance.

## Output

Return:

1. Clear list of confirmed, likely, and possible profit traps.
2. Metric evidence for each trap.
3. Recommended action: do not implement, segment rollout, extend test, or investigate margin inputs.
4. Missing data that would change confidence.
5. Appendix with source tool calls and experience IDs.

Never call a result safe if profit metrics are missing. Mark it as "conversion-only evidence" instead.

## Data Safety

Use only the user's authenticated MCP or API context. Do not save raw responses, exports, graph URLs, order data, customer data, or private store identifiers to the repository. Summarize findings and include experience IDs only when needed for the user's workflow.
