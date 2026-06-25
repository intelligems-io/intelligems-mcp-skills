# Intelligems External API Reference

Sources:

- https://docs.intelligems.io/developer-resources/external-api
- https://static.intelligems.io/api-docs-v25-10-prod.json

Last checked: 2026-06-25.

## Status

The public docs describe the External API as beta.

## Base URL

The OpenAPI spec lists:

```text
https://api.intelligems.io
```

## Authentication

Use the `intelligems-access-token` header. Store the API key in an environment variable and never commit it.

Example placeholder:

```bash
curl --location "https://api.intelligems.io/v25-10-beta/experiences-list" \
  --header "intelligems-access-token: $INTELLIGEMS_ACCESS_TOKEN"
```

## Main Endpoints From Public Docs

- `GET /v25-10-beta/experiences-list` - list experiences with optional filtering and pagination.
- `GET /v25-10-beta/experiences/{experienceId}` - fetch full experience details.
- `POST /v25-10-beta/experiences` - create an experience.
- `PUT /v25-10-beta/experiences/{experienceId}` - replace an existing experience configuration.
- `POST /v25-10-beta/experiences/{experienceId}/actions/{action}` - start, pause, or end an experience.
- `GET /v25-10-beta/analytics/resource/{experienceId}` - deprecated beta compatibility path for experience analytics. Use the POST path for new integrations.
- `POST /v25-10-beta/analytics/resource/{experienceId}` - OpenAPI analytics path for experience analysis requests.
- `POST /v25-10-beta/analytics/sitewide/snapshot` - sitewide KPI snapshot.
- `POST /v25-10-beta/analytics/sitewide/timeseries` - sitewide metric time series.
- `POST /v25-10-beta/analytics/sitewide/order-distribution` - order value and unit mix distribution.
- `POST /v25-10-beta/analytics/sitewide/conversion-funnel` - sitewide conversion funnel.
- `POST /v25-10-beta/analytics/event/snapshot` - custom event snapshot analytics.
- `POST /v25-10-beta/analytics/event/timeseries` - custom event time series analytics.
- `POST /v25-10-beta/analytics/experience/{experienceId}/timeseries` - experience-level time series analytics.
- `POST /v25-10-beta/analytics/experience/{experienceId}/export` - experience export endpoint for order-level or line-item-level CSV data.

## Important OpenAPI Notes

- `GET /experiences-list` supports `limit`, `page`, `status`, and `category`.
- `page` is 1-indexed.
- Valid status values include `pending`, `started`, `ended`, and `paused`.
- Valid category values include `experiment` and `personalization`.
- `GET /experiences/{experienceId}` returns a wrapped response: `{ "experience": { ... } }`.
- The OpenAPI spec says `PUT /experiences/{experienceId}` is a full replacement. Include required fields and nested entity IDs from the original GET response.
- Experience lifecycle actions include `start`, `pause`, and `end`.
- Legacy `GET /analytics/resource/{experienceId}` uses query parameters and 10-digit Unix epoch timestamps in seconds.
- `POST /analytics/experience/{experienceId}/export` returns a presigned CSV download URL that expires after 15 minutes. Treat the URL and downloaded file as private data.
- Profit metrics may be null when cost of goods sold is not configured or only partially covered.

## Filters

Analytics POST endpoints accept a `filters` object in the request body. Useful dimensions include:

- `deviceType`: `any`, `mobile`, or `desktop`.
- `visitorType`: `any`, `new`, or `returning`.
- `countryCodes`: ISO country codes.
- `sourceSitesOrChannels`: traffic source names.
- `landingPageFilters`: path filters with operators like equals, contains, startsWith, endsWith, and negative/null variants.
- `urlParam`: query parameter filtering.
- `userBehavior`: checkout, add-to-cart, product-page, or collection-page behavior.
- Revenue and shipping filters.
- Custom events filters.
- Product filters.
- `onlyProductIds` and `onlyProductHandles` for product-level analysis.

## Data Handling

Do not commit:

- Raw JSON responses from real accounts.
- CSV exports.
- Presigned export URLs.
- Generated graphs from private data.
- Organization IDs, experience IDs, store domains, order IDs, visitor IDs, or customer identifiers from real accounts.

Use synthetic placeholders in examples:

- `YOUR_EXPERIENCE_ID`
- `$INTELLIGEMS_ACCESS_TOKEN`
- `YOUR_ORGANIZATION_ID`

## Rate Limits

The OpenAPI spec documents token-bucket rate limiting and says every response includes:

- `x-ratelimit-limit`
- `x-ratelimit-remaining`
- `x-ratelimit-reset`

Use response headers as authoritative and back off on `429`.

## Errors

Expected status codes include:

- `200` success.
- `400` validation error.
- `401` invalid or missing API key.
- `404` resource not found.
- `429` rate limit exceeded.
- `500` internal server error.

Do not ask users to paste secrets into chat when auth fails. Ask them to configure the environment variable locally.
