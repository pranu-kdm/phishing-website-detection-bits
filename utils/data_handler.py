
import pandas as pd
from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# LOAD DEFAULT DATASET
# ============================================================

def load_default_dataset():

    file_path = BASE_DIR / "test_data.csv"

    return pd.read_csv(file_path)


# ============================================================
# CREATE SAMPLE DATASET
# ============================================================

def create_sample_dataset():

    file_path = BASE_DIR / "test_data.csv"

    if file_path.exists():
        return pd.read_csv(file_path)

    return None


# ============================================================
# VALIDATE DATASET
# ============================================================

def validate_dataset(data, required_columns):

    # Check required columns
    missing_columns = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        return (
            False,
            f"Missing required columns: {missing_columns}"
        )

    # Convert columns to numeric
    try:
        data[required_columns] = data[required_columns].apply(
            pd.to_numeric,
            errors="raise"
        )

    except Exception:
        return (
            False,
            "All feature columns and target column must contain numeric values."
        )

    # Check missing values
    if data[required_columns].isnull().sum().sum() > 0:
        return (
            False,
            "Dataset contains missing values."
        )

    # Check target values
    if not set(data["is_phishing"].unique()).issubset({0, 1}):
        return (
            False,
            "Target column must contain only 0 and 1."
        )

    # Check both classes are present
    if data["is_phishing"].nunique() != 2:
        return (
            False,
            "Dataset must contain both legitimate and phishing records."
        )

    return True, "Dataset validation successful."
