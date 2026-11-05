import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc, confusion_matrix


# ============================================================
# CLASS DISTRIBUTION CHART
# ============================================================

def create_class_distribution_chart(
    legitimate_count,
    phishing_count
):
    fig, ax = plt.subplots(figsize=(5, 3.2))

    ax.bar(
        ["Legitimate", "Phishing"],
        [legitimate_count, phishing_count],
        width=0.5
    )

    ax.set_ylabel("Number of Records")
    ax.set_title("Class Distribution")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.2
    )

    plt.tight_layout()

    return fig


# ============================================================
# MODEL COMPARISON CHART
# ============================================================

def create_model_comparison_chart(
    chart_values,
    selected_metric
):
    fig, ax = plt.subplots(figsize=(9, 4))

    ax.barh(
        chart_values.index,
        chart_values.values,
        height=0.45
    )

    ax.set_xlabel(selected_metric)
    ax.set_title(f"Model Comparison - {selected_metric}")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    ax.grid(
        axis="x",
        linestyle="--",
        alpha=0.25
    )

    plt.tight_layout()

    return fig


# ============================================================
# CONFUSION MATRIX
# ============================================================

def create_confusion_matrix_chart(
    y_test,
    predictions
):
    cm = confusion_matrix(
        y_test,
        predictions,
        labels=[0, 1]
    )

    fig, ax = plt.subplots(
        figsize=(4.8, 3.8),
        dpi=100
    )

    ax.imshow(
        cm,
        interpolation="nearest",
        cmap="GnBu"
    )

    ax.set_title("Confusion Matrix")
    ax.set_xlabel("Predicted Label")
    ax.set_ylabel("Actual Label")

    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])

    ax.set_xticklabels(["Legitimate", "Phishing"])
    ax.set_yticklabels(["Legitimate", "Phishing"])

    threshold = cm.max() / 2 if cm.max() > 0 else 0

    for i in range(2):
        for j in range(2):
            ax.text(
                j,
                i,
                str(cm[i, j]),
                ha="center",
                va="center",
                color="white" if cm[i, j] > threshold else "#17345f",
                fontsize=12,
                fontweight="bold"
            )

    plt.tight_layout()

    return fig


# ============================================================
# ROC CURVE COMPARISON
# ============================================================

def create_roc_curve_chart(
    all_results,
    y_test
):
    fig, ax = plt.subplots(figsize=(8, 5))

    for model_name, result in all_results.items():

        fpr, tpr, thresholds = roc_curve(
            y_test,
            result["scores"]
        )

        roc_auc = auc(fpr, tpr)

        ax.plot(
            fpr,
            tpr,
            linewidth=1.8,
            label=f"{model_name} (AUC = {roc_auc:.4f})"
        )

    ax.plot(
        [0, 1],
        [0, 1],
        linestyle="--",
        linewidth=1,
        label="Random Classifier"
    )

    ax.set_title("ROC Curve Comparison")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")

    ax.legend(
        loc="lower right",
        fontsize=8
    )

    ax.grid(alpha=0.2)

    plt.tight_layout()

    return fig