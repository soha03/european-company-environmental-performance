
import pandas as pd

from src.validate_data import validate_records, validate_schema


def valid_record():
    return {
        "company": "Example Energy",
        "reporting_year": 2024,
        "indicator": "scope_1_emissions",
        "value": 1000.0,
        "unit": "tCO2e",
        "method": "reported",
        "source_document": "Sustainability Report 2024",
        "source_url": "https://example.com/report.pdf",
        "source_page": 42,
        "data_status": "reported",
    }


def test_valid_record_has_no_errors():
    data = pd.DataFrame([valid_record()])
    assert validate_records(data) == []


def test_missing_required_column_is_detected():
    data = pd.DataFrame([valid_record()]).drop(columns=["unit"])
    errors = validate_schema(data)
    assert any("unit" in error for error in errors)


def test_missing_source_is_detected():
    record = valid_record()
    record["source_url"] = None

    errors = validate_records(pd.DataFrame([record]))
    assert any("source_url" in error for error in errors)


def test_invalid_emissions_unit_is_detected():
    record = valid_record()
    record["unit"] = "kg"

    errors = validate_records(pd.DataFrame([record]))
    assert any("Invalid unit" in error for error in errors)


def test_duplicate_observations_are_detected():
    record = valid_record()
    data = pd.DataFrame([record, record])

    errors = validate_records(data)
    assert any("Duplicate" in error for error in errors)
