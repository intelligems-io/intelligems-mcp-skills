---
name: client-performance-review
description: Use when preparing a monthly or quarterly Intelligems performance review for an agency client, customer, account, or stakeholder meeting.
license: MIT
---

# Client Performance Review

Use this skill to turn completed and active Intelligems tests into a meeting-ready performance review.

## Steps

1. Resolve organization, review period, and audience for the review.
2. Search for completed tests in the period with `search_experiences` or `search_experiments` using `status: "ended"`.
3. Include running tests only if the user asks or they materially affect the review.
4. Analyze each completed test with `get_experience`, `get_experience_metrics_config`, and `analyze_experience`.
5. Pull segment breakdowns only for tests where they change the story.
6. Summarize revenue, profit, and learning impact separately.

## Review Structure

Return:

1. Executive summary.
2. Completed tests: winners, losers, inconclusive tests.
3. Estimated revenue or profit impact where supported by data.
4. Strategic learnings by theme.
5. Tests that should be implemented, repeated, extended, or retired.
6. Recommended next tests.
7. Appendix with organization, dates, experience IDs, and caveats.

## Quality Bar

- Explain what happened, why it matters, and what the client should do next.
- Keep the narrative honest if the data is inconclusive.
- Do not hide tests with negative results. Convert them into learnings when possible.

## Data Safety

Use only the user's authenticated MCP or API context. Do not save raw responses, exports, graph URLs, order data, customer data, or private store identifiers to the repository. Summarize findings and include experience IDs only when needed for the user's workflow.
