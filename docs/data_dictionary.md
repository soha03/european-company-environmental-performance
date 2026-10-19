
# Data Dictionary

## Purpose

Document the variables used to collect and analyse environmental disclosures from European energy companies.

## Observation unit

One observation represents one environmental or financial indicator for one company and one reporting year, under a specified measurement method and reporting boundary.

## Core fields

| Field | Definition |
|---|---|
| company | Company name |
| reporting_year | Financial reporting year |
| indicator | Standardised indicator name |
| value | Numeric observation; blank if unavailable |
| unit | Measurement unit |
| scope | Emissions scope, where applicable |
| method | Measurement or accounting method |
| boundary | Organisational or operational reporting boundary |
| source_document | Name of the original report |
| source_url | Direct link to the source |
| source_page | Page supporting the observation |
| data_status | Reported, estimated, missing or under_review |
| notes | Relevant qualifications and extraction notes |

## Initial indicators

- scope_1_emissions
- scope_2_location_based
- scope_2_market_based
- electricity_generation
- renewable_electricity_generation
- revenue

## Units

- Greenhouse-gas emissions: tonnes of CO2-equivalent (tCO2e).
- Electricity generation: megawatt-hours (MWh).
- Revenue: original reported currency, recorded explicitly.

## Rules

1. Never replace missing observations with zero.
2. Keep location-based and market-based Scope 2 emissions separate.
3. Record the reporting boundary and measurement method.
4. Preserve the original reported value and unit in the raw data.
5. Convert units only in the processed dataset, retaining the original value.
6. Record the source document and page for every extracted observation.
7. Do not compare indicators with incompatible definitions or boundaries.
8. Distinguish reported values from estimates.
9. Do not treat missing disclosure as evidence of poor environmental performance.
10. Record restatements and methodological changes explicitly.
