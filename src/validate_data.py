
"""Validation rules for environmental disclosure observations."""

from __future__ import annotations

import pandas as pd


REQUIRED_COLUMNS = {
    "company",
    "reporting_year",
    "indicator",
    "value",
    "unit",
    "method",
    "source_document",
    "source_url",
    "source_page",
    "data_status",
}

ALLOWED_STATUSES = {
    "reported",
    "estimated",
    "missing",
    "under_review",
}

EXPECTED_UNITS = {
    "scope_1_emissions": {"tCO2e"},
    "scope_2_location_based": {"tCO2e"},
    "scope_2_market_based": {"tCO2e"},
    "electricity_generation": {"MWh"},
    "renewable_electricity_generation": {"MWh"},
    "revenue": {"EUR", "USD", "GBP"},
}

EMISSIONS_INDICATORS = {
    "scope_1_emissions",
    "scope_2_location_based",
    "scope_2_market_based",
}

SOURCE_REQUIRED_STATUSES = {
    "reported",
    "estimated",
    "under_review",
}

DUPLICATE_KEY_COLUMNS = [
    "company",
    "reporting_year",
    "indicator",
    "method",
]


def validate_schema(data: pd.DataFrame) -> list[str]:
    """Check whether the dataset contains all required columns."""
    missing_columns = REQUIRED_COLUMNS - set(data.columns)

    if missing_columns:
        return [
            f"Missing required columns: {sorted(missing_columns)}"
        ]

    return []


def validate_records(data: pd.DataFrame) -> list[str]:
    """Validate environmental disclosure records without modifying them."""
    errors = validate_schema(data)

    if errors:
        return errors

    # Check company names and reporting years.
    company_names = data["company"].astype("string").str.strip()

    if company_names.isna().any() or company_names.eq("").any():
        errors.append("Company name is missing.")

    years = pd.to_numeric(data["reporting_year"], errors="coerce")

    if years.isna().any():
        errors.append("Reporting year must contain numeric values.")
    elif (years % 1 != 0).any():
        errors.append("Reporting year must contain whole numbers.")

    # Check indicator and status fields.
    for field in ["indicator", "method", "unit"]:
        values = data[field].astype("string")

        if values.isna().any() or values.str.strip().eq("").any():
            errors.append(f"{field} contains missing or blank values.")

    invalid_status = ~data["data_status"].isin(ALLOWED_STATUSES)

    if invalid_status.any():
        errors.append("Unrecognised data_status value.")

    # Validate numeric observations.
    values = pd.to_numeric(data["value"], errors="coerce")

    non_numeric = data["value"].notna() & values.isna()

    if non_numeric.any():
        errors.append("The value column contains non-numeric values.")

    non_finite = values.notna() & ~values.map(
        lambda value: pd.isna(value) or abs(value) != float("inf")
    )

    # Explicitly identify infinite values without rejecting ordinary NaNs.
    infinite_values = values.map(
        lambda value: pd.notna(value) and not abs(value) < float("inf")
    )

    if infinite_values.any():
        errors.append("The value column contains infinite values.")

    # A missing observation must have no numeric value.
    missing_status = data["data_status"].eq("missing")

    if (missing_status & data["value"].notna()).any():
        errors.append(
            "Records marked missing must not contain a numeric value."
        )

    # Check units against the declared indicator.
    for indicator, allowed_units in EXPECTED_UNITS.items():
        selected = data["indicator"].eq(indicator)
        invalid_units = selected & ~data["unit"].isin(allowed_units)

        if invalid_units.any():
            errors.append(
                f"Invalid unit for {indicator}; expected "
                f"one of {sorted(allowed_units)}."
            )

    # Negative reported emissions require review.
    emissions_rows = data["indicator"].isin(EMISSIONS_INDICATORS)

    negative_emissions = (
        emissions_rows
        & values.notna()
        & (values < 0)
    )

    if negative_emissions.any():
        errors.append(
            "Negative emissions values require explicit review."
        )

    # Check source traceability.
    source_required = data["data_status"].isin(
        SOURCE_REQUIRED_STATUSES
    )

    for field in ["source_document", "source_url", "source_page"]:
        field_values = data[field].astype("string")

        missing_source = source_required & (
            field_values.isna() | field_values.str.strip().eq("")
        )

        if missing_source.any():
            errors.append(
                f"{field} is missing for an observation requiring a source."
            )

    # Detect duplicate observations.
    duplicate_rows = data.duplicated(
        subset=DUPLICATE_KEY_COLUMNS,
        keep=False,
    )

    if duplicate_rows.any():
        errors.append(
            "Duplicate company-year-indicator-method observations found."
        )

    return errors
