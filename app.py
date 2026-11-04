
# ============================================================
# 1. IMPORTS
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from components.styles import apply_custom_styles, render_header, render_footer

from components.charts import (
    create_class_distribution_chart,
    create_model_comparison_chart,
    create_confusion_matrix_chart,
    create_roc_curve_chart
)

from components.dashboard import create_classification_report

from utils.model_loader import load_metadata, load_models

from utils.data_handler import (
    load_default_dataset,
    create_sample_dataset,
    validate_dataset
)

from utils.evaluation import evaluate_model


# ============================================================
# 2. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Phishing Website Detection",
    page_icon="🛡️",
    layout="wide"
)


# ============================================================
# 3. CUSTOM CSS
# ============================================================

apply_custom_styles()


# ============================================================
# 4. MODEL CONFIGURATION
# ============================================================

MODEL_NAMES = [
    "Logistic Regression",
    "Decision Tree",
    "KNN",
    "Gaussian Naive Bayes",
    "SVM"
]

METRIC_NAMES = [
    "Accuracy",
    "AUC",
    "Precision",
    "Recall",
    "F1 Score",
    "MCC"
]


# ============================================================
# 5. LOAD METADATA
# ============================================================

metadata = load_metadata()

FEATURE_COLUMNS = metadata["features"]

# Internal target column name used by the existing project.
# Uploaded CSV target columns will be renamed to this name.
TARGET_COLUMN = "is_phishing"

REQUIRED_COLUMNS = FEATURE_COLUMNS + [TARGET_COLUMN]


# ============================================================
# 6. LOAD SAVED MODELS
# ============================================================

models = load_models()

if not models:
    st.error(
        "No trained models were found. "
        "Please check the models folder."
    )
    st.stop()


# ============================================================
# 7. GET MODEL SCORES
# ============================================================

# Model scores are calculated inside evaluate_model()
# using predict_proba(), decision_function(), or predict().


# ============================================================
# 8. MODEL EVALUATION
# ============================================================

# Evaluation is performed after the dataset is selected
# and validated.


# ============================================================
# 9. CSV VALIDATION
# ============================================================

# Dataset validation is handled by utils/data_handler.py.


# ============================================================
# 10. LOAD SAMPLE DATASET
# ============================================================

sample_dataset = create_sample_dataset()


# ============================================================
# 11. HEADER
# ============================================================

render_header()


# ============================================================
# 12. LOAD PROJECT FILES
# ============================================================

# Models, metadata, and sample dataset are loaded above.


# ============================================================
# 13. SIDEBAR
# ============================================================

st.sidebar.title("Phishing Detection")

st.sidebar.markdown(
    "Upload a CSV file to evaluate the trained machine learning models."
)

st.sidebar.markdown("---")

st.sidebar.subheader("Upload Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

st.sidebar.markdown(
    """
    **CSV Requirements**
    - File format: CSV
    - Must contain all 30 input features
    - Target column can have any name
    - Target values must be 0 or 1
    - Must contain both target classes
    """
)

st.sidebar.markdown("---")

st.sidebar.subheader("Sample Dataset")

if sample_dataset is not None:
    st.sidebar.download_button(
        label="Download Sample Dataset",
        data=sample_dataset.to_csv(index=False).encode("utf-8"),
        file_name="test_data.csv",
        mime="text/csv",
        width="stretch"
    )


# ============================================================
# 14. READ DEFAULT OR UPLOADED DATASET
# ============================================================

if uploaded_file is not None:

    try:
        data = pd.read_csv(uploaded_file)
        dataset_source = "Uploaded Dataset"

    except Exception as error:
        st.error(f"Unable to read uploaded CSV file: {error}")
        st.stop()

else:

    try:
        data = load_default_dataset()
        dataset_source = "Default Test Dataset"

    except Exception as error:
        st.error(f"Unable to load default dataset: {error}")
        st.stop()


# ============================================================
# 15. SELECT TARGET COLUMN
# ============================================================

if uploaded_file is not None:

    # Target column must not be one of the model input features.
    target_options = [
        column for column in data.columns
        if column not in FEATURE_COLUMNS
    ]

    if not target_options:
        st.error(
            "No target column found. "
            "Please include a target column in your CSV."
        )
        st.stop()

    # Automatically select is_phishing when it exists.
    default_target_index = (
        target_options.index("is_phishing")
        if "is_phishing" in target_options
        else 0
    )

    selected_target_column = st.sidebar.selectbox(
        "Select Target Column",
        options=target_options,
        index=default_target_index
    )

    # Prevent a duplicate internal target column.
    if (
        TARGET_COLUMN in data.columns
        and selected_target_column != TARGET_COLUMN
    ):
        st.error(
            f"Your CSV already contains a column named "
            f"'{TARGET_COLUMN}'. Please remove the extra column "
            "or select the correct target column."
        )
        st.stop()

    # Rename the selected target column to the internal name
    # expected by the existing data_handler.py and evaluation code.
    if selected_target_column != TARGET_COLUMN:
        data = data.rename(
            columns={selected_target_column: TARGET_COLUMN}
        )


# ============================================================
# 16. VALIDATE SELECTED DATASET
# ============================================================

is_valid, validation_message = validate_dataset(
    data,
    REQUIRED_COLUMNS
)

if not is_valid:
    st.error(validation_message)
    st.stop()

st.success(f"{dataset_source} loaded successfully.")


# ============================================================
# 17. PREPARE TEST DATA
# ============================================================

X_test = data[FEATURE_COLUMNS]
y_test = data[TARGET_COLUMN]


# ============================================================
# 18. DATASET OVERVIEW AND CLASS DISTRIBUTION
# ============================================================

st.markdown("## Dataset Overview")

left_column, right_column = st.columns([1, 1])

total_records = len(data)
total_features = len(FEATURE_COLUMNS)

legitimate_count = int((y_test == 0).sum())
phishing_count = int((y_test == 1).sum())

with left_column:

    st.metric(
        "Total Records",
        total_records
    )

    st.metric(
        "Input Features",
        total_features
    )

    st.markdown("### Dataset Preview")

    st.dataframe(
        data.head(),
        width="stretch"
    )


with right_column:

    st.markdown("### Class Distribution")

    fig = create_class_distribution_chart(
        legitimate_count,
        phishing_count
    )

    st.pyplot(fig, width="stretch")
    plt.close(fig)


# ============================================================
# 19. EVALUATE ALL MODELS
# ============================================================

all_results = {}

for model_name in MODEL_NAMES:

    if model_name not in models:
        continue

    model = models[model_name]

    predictions, scores, metrics = evaluate_model(
        model,
        X_test,
        y_test
    )

    all_results[model_name] = {
        "predictions": predictions,
        "scores": scores,
        "metrics": metrics
    }


if not all_results:
    st.error("No models were available for evaluation.")
    st.stop()


# ============================================================
# 20. MODEL COMPARISON
# ============================================================

st.markdown("---")
st.markdown("## Model Comparison")

comparison_data = {}

for model_name, result in all_results.items():

    comparison_data[model_name] = result["metrics"]


comparison_df = pd.DataFrame(comparison_data).T

comparison_df = comparison_df[METRIC_NAMES]

st.dataframe(
    comparison_df.style.format("{:.4f}"),
    width="stretch"
)


# ============================================================
# 21. BEST MODEL PER METRIC
# ============================================================

st.markdown("### Best Model Per Metric")

best_model_columns = st.columns(3)

for index, metric in enumerate(METRIC_NAMES):

    best_model = comparison_df[metric].idxmax()
    best_score = comparison_df[metric].max()

    with best_model_columns[index % 3]:

        st.metric(
            label=f"Best {metric}",
            value=best_model,
            delta=f"{best_score:.4f}"
        )


# ============================================================
# 22. MODEL COMPARISON CHART
# ============================================================

st.markdown("---")
st.markdown("### Model Performance Comparison")

selected_metric = st.selectbox(
    "Select Metric",
    METRIC_NAMES
)

chart_values = comparison_df[selected_metric].sort_values()

fig = create_model_comparison_chart(
    chart_values,
    selected_metric
)

st.pyplot(fig, width="stretch")
plt.close(fig)


# ============================================================
# 23. INDIVIDUAL MODEL EVALUATION
# ============================================================

st.markdown("---")
st.markdown("## Individual Model Evaluation")

selected_model = st.selectbox(
    "Select a Model",
    list(all_results.keys())
)

selected_result = all_results[selected_model]

predictions = selected_result["predictions"]
scores = selected_result["scores"]
metrics = selected_result["metrics"]


# ============================================================
# 24. INDIVIDUAL MODEL METRICS
# ============================================================

st.markdown(f"### {selected_model} Performance")

metric_columns = st.columns(3)

for index, metric in enumerate(METRIC_NAMES):

    with metric_columns[index % 3]:

        st.metric(
            label=metric,
            value=f"{metrics[metric]:.4f}"
        )


# ============================================================
# 25. CONFUSION MATRIX
# ============================================================

st.markdown("---")
st.markdown("### Confusion Matrix")

fig = create_confusion_matrix_chart(
    y_test,
    predictions
)

st.pyplot(fig, width="content")
plt.close(fig)


# ============================================================
# 26. CLASSIFICATION REPORT
# ============================================================

st.markdown("### Classification Report")

report_df = create_classification_report(
    y_test,
    predictions
)

st.dataframe(
    report_df.style.format("{:.4f}"),
    width="stretch"
)


# ============================================================
# 27. ROC CURVE COMPARISON
# ============================================================

st.markdown("---")
st.markdown("## ROC Curve Comparison")

fig = create_roc_curve_chart(
    all_results,
    y_test
)

st.pyplot(fig, width="stretch")
plt.close(fig)


# ============================================================
# 28. DOWNLOAD MODEL COMPARISON CSV
# ============================================================

st.markdown("---")
st.markdown("## Download Results")

csv_data = comparison_df.to_csv(
    float_format="%.4f"
).encode("utf-8")

st.download_button(
    label="Download Model Comparison Results",
    data=csv_data,
    file_name="model_comparison_results.csv",
    mime="text/csv",
    width="stretch"
)


# ============================================================
# 29. FOOTER
# ============================================================

render_footer()
