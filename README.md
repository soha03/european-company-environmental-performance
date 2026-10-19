
# European Company Environmental Performance

A reproducible analysis of environmental disclosures from selected European energy companies.

## Objectives

- Collect and document published environmental indicators.
- Validate data completeness, units, sources and reporting methods.
- Analyse emissions and electricity-generation trends.
- Compare companies only where definitions and boundaries permit.
- Produce transparent analytical tables and visualisations.

## Tools

Python, pandas, NumPy, SQL, matplotlib, pytest, Git and Power BI.

## Project structure

- `data/raw/`: original extracted observations.
- `data/processed/`: validated and standardised datasets.
- `docs/`: methodology and data dictionary.
- `sql/`: analytical queries.
- `src/`: data-processing and analysis modules.
- `tests/`: automated validation and calculation tests.
- `outputs/`: generated tables, figures and reports.

## Data sources

Primary sources will be official company annual reports and sustainability statements. Each observation will retain a reference to its original source.

## Methodological principles

- Missing values are not treated as zero.
- Scope 2 accounting methods remain separate.
- Reporting boundaries and units are documented.
- Automated validation flags issues for review.
- Comparisons are made only when the underlying measures are sufficiently compatible.
- Results are descriptive unless a suitable method supports stronger conclusions.

## Project status

Initial setup and methodology definition. Data collection, validation, analysis and dashboard development are pending.

## Reproducibility

Installation instructions and analysis commands will be added after the initial pipeline and tests are implemented.

