
# Methodology

## Objective

Build a reproducible dataset for analysing the environmental disclosures of selected European energy companies.

## Research questions

1. How complete are the selected companies' environmental disclosures?
2. How do their reported emissions and electricity generation change over time?
3. Which indicators are sufficiently comparable for cross-company analysis?
4. How do reporting boundaries and measurement methods affect interpretation?

## Company sample

Initial candidates:

- EDF
- Enel
- ENGIE
- Iberdrola
- RWE

The final sample will depend on source availability and the comparability of reported indicators.

## Reporting period

2021–2025, subject to availability, consistent definitions and documented reporting changes.

## Data collection

Use company annual reports, sustainability statements and other official disclosures as primary sources. Record the source document, URL, page, reporting year and extraction notes for each observation.

## Data validation

Check:

- Required fields and valid data types.
- Duplicate company-year-indicator-method records.
- Missing values and missing source references.
- Units, plausible values and inconsistent definitions.
- Changes in reporting boundaries and accounting methods.
- Reconciliation with the original published disclosure.

Automated checks identify records for review; they do not automatically establish that a reported value is correct.

## Analysis

Calculate disclosure coverage and year-on-year changes only when the underlying observations are comparable.

Calculate emissions intensity only when the emissions numerator and denominator have compatible organisational and temporal boundaries.

Do not rank companies using an aggregate environmental score in the initial version.

## Interpretation

Distinguish observed changes from explanations for those changes. Changes in reported emissions may reflect operational performance, acquisitions, disposals, methodology changes or reporting-boundary changes.

Correlation alone does not establish causation.

## Reproducibility

Keep raw observations separate from processed data. Version the code, document transformations, test calculation functions and provide instructions for reproducing the outputs.

## Limitations

Company disclosures may differ in coverage, assurance, estimation methods and reporting boundaries. Comparisons will be restricted to indicators that can be interpreted consistently.

