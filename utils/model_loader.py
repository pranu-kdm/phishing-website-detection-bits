
import json
from pathlib import Path

import joblib
import streamlit as st


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Models directory
MODELS_DIR = BASE_DIR / "models"


@st.cache_data
def load_metadata():
    """Load model metadata from metadata.json."""

    metadata_path = MODELS_DIR / "metadata.json"

    with open(metadata_path, "r") as file:
        metadata = json.load(file)

    return metadata


@st.cache_resource
def load_models():
    """Load all trained machine learning models."""

    model_files = {
        "Logistic Regression": "logistic_regression.joblib",
        "Decision Tree": "decision_tree.joblib",
        "KNN": "knn.joblib",
        "Gaussian Naive Bayes": "gaussian_naive_bayes.joblib",
        "SVM": "svm.joblib",
    }

    models = {}

    for model_name, file_name in model_files.items():
        model_path = MODELS_DIR / file_name

        models[model_name] = joblib.load(model_path)

    return models
