import pandas as pd

from sklearn.metrics import classification_report


# ============================================================
# CLASSIFICATION REPORT
# ============================================================

def create_classification_report(
    y_test,
    predictions
):
    report = classification_report(
        y_test,
        predictions,
        target_names=["Legitimate", "Phishing"],
        output_dict=True,
        zero_division=0
    )

    report_df = pd.DataFrame(report).transpose()

    return report_df