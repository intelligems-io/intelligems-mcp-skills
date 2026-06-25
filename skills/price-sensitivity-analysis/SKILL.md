---
name: price-sensitivity-analysis
description: Use when a user asks what Intelligems test data says about price tolerance, discount response, AOV tradeoffs, or segment-specific price behavior.
license: MIT
---

# Price Sensitivity Analysis

Use this skill to interpret price, discount, shipping, and offer tests.

## Steps

1. Resolve organization, period, and product or offer scope.
2. Search relevant experiences by name, category, or explicit IDs.
3. Analyze overview metrics first: conversion rate, RPV, GPV, AOV, net revenue, confidence.
4. Segment the results by device, visitor type, country, traffic source, and landing page when relevant.
5. Compare results across tests to identify repeatable price tolerance patterns.

## Questions To Answer

- Did price or discount changes increase profit, not just conversion?
- Which segments are most price-sensitive?
- Did higher AOV offset lower conversion, or did lower price dilute value?
- Are discounts training behavior or unlocking incremental demand?
- What guardrails should future price tests use?

## Output

Return:

1. Price sensitivity summary.
2. Evidence table by test and segment.
3. Profit and risk interpretation.
4. Recommendations for pricing, discounting, and follow-up tests.
5. Caveats around sample size, seasonality, and missing margin data.

Do not recommend a permanent pricing change without profit evidence and business-context caveats.

## Data Safety

Use only the user's authenticated MCP or API context. Do not save raw responses, exports, graph URLs, order data, customer data, or private store identifiers to the repository. Summarize findings and include experience IDs only when needed for the user's workflow.
