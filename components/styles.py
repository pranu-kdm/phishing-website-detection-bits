
import streamlit as st


# ============================================================
# CUSTOM CSS
# ============================================================

def apply_custom_styles():

    st.markdown(
        """
        <style>

        /* =========================================
           MAIN APP BACKGROUND
        ========================================= */

        .stApp {
            background: linear-gradient(
                135deg,
                #eaf2ff 0%,
                #f4f7ff 50%,
                #e8efff 100%
            ) !important;
        }


        /* =========================================
           MAIN CONTENT
        ========================================= */

        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }


        /* =========================================
           HEADER
        ========================================= */

        .hero {
            background: linear-gradient(
                135deg,
                #102f60 0%,
                #24599a 55%,
                #477fc4 100%
            ) !important;

            padding: 28px !important;
            border-radius: 18px !important;
            color: #ffffff !important;
            margin-bottom: 25px !important;
            box-shadow: 0 5px 15px rgba(16, 47, 96, 0.15) !important;
        }

        .hero h1 {
            color: #ffffff !important;
            font-size: 2.2rem !important;
            font-weight: 700 !important;
            margin-bottom: 10px !important;
        }

        .hero p {
            color: #eaf2ff !important;
            font-size: 1rem !important;
            margin-bottom: 5px !important;
        }


        /* =========================================
           SIDEBAR BACKGROUND
        ========================================= */

        section[data-testid="stSidebar"] {
            background: linear-gradient(
                180deg,
                #102f60 0%,
                #214f89 55%,
                #3569ad 100%
            ) !important;
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"],
        section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] p,
        section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] span {
            color: #ffffff !important;
        }


        /* =========================================
           METRIC CARDS
        ========================================= */

        div[data-testid="stMetric"] {
            background: linear-gradient(
                135deg,
                #ffffff 0%,
                #e8f0ff 100%
            ) !important;

            border: 1px solid #d5e2f7 !important;
            padding: 10px !important;
            border-radius: 12px !important;
            height: 115px;
            box-shadow: 0 3px 10px rgba(16, 47, 96, 0.06);
        }

        div[data-testid="stMetricLabel"] {
            color: #31547f !important;
            font-weight: 600 !important;
        }

        div[data-testid="stMetricValue"] {
            color: #102f60 !important;
            font-weight: 700 !important;
        }


        /* =========================================
           FILE UPLOADER CONTAINER
        ========================================= */

        section[data-testid="stSidebar"] [data-testid="stFileUploader"] {
            background: rgba(255, 255, 255, 0.08) !important;
            border-radius: 10px !important;
        }

        section[data-testid="stSidebar"] [data-testid="stFileUploader"] section {
            background: rgba(255, 255, 255, 0.12) !important;
            border: 1px dashed #d5e2f7 !important;
            border-radius: 10px !important;
        }

        /* Upload instructions */

        section[data-testid="stSidebar"] [data-testid="stFileUploader"] section span,
        section[data-testid="stSidebar"] [data-testid="stFileUploader"] section small,
        section[data-testid="stSidebar"] [data-testid="stFileUploader"] section p {
            color: #ffffff !important;
        }


        /* =========================================
           BROWSE FILE BUTTON
        ========================================= */

        section[data-testid="stSidebar"] [data-testid="stFileUploader"] button {
            background: #ffffff !important;
            color: #17345f !important;
            border: 1px solid #d5e2f7 !important;
            border-radius: 8px !important;
        }

        section[data-testid="stSidebar"] [data-testid="stFileUploader"] button span,
        section[data-testid="stSidebar"] [data-testid="stFileUploader"] button p {
            color: #17345f !important;
        }


        /* =========================================
           UPLOADED FILE NAME
        ========================================= */

        section[data-testid="stSidebar"] [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"] {
            background: #ffffff !important;
            border-radius: 8px !important;
        }

        section[data-testid="stSidebar"] [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"] * {
            color: #17345f !important;
        }


        /* =========================================
           REMOVE UPLOADED FILE BUTTON
        ========================================= */

        section[data-testid="stSidebar"] [data-testid="stFileUploaderDeleteBtn"] {
            background: #ffffff !important;
            color: #17345f !important;
        }


        /* =========================================
           GENERAL BUTTONS
        ========================================= */

        .stButton button,
        .stDownloadButton button {
            background: linear-gradient(
                135deg,
                #173f75,
                #3569ad
            ) !important;

            color: #ffffff !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
        }

        .stButton button:hover,
        .stDownloadButton button:hover {
            background: linear-gradient(
                135deg,
                #102f60,
                #24599a
            ) !important;

            color: #ffffff !important;
            border: none !important;
        }


        /* =========================================
           DATAFRAMES AND TABLES
        ========================================= */

        div[data-testid="stDataFrame"] {
            border: 1px solid #d5e2f7 !important;
            border-radius: 10px !important;
            overflow: hidden !important;
        }

        div[data-testid="stDataFrame"] [role="columnheader"],
        div[data-testid="stDataFrame"] [role="gridcell"] {
            color: #17345f !important;
        }

        div[data-testid="stTable"] {
            color: #17345f !important;
        }


        /* =========================================
           SELECT BOX
        ========================================= */

        div[data-baseweb="select"] > div {
            border-radius: 8px !important;
            border-color: #c7d8f1 !important;
        }


        /* =========================================
           SECTION HEADINGS
        ========================================= */

        .main h1,
        .main h2,
        .main h3 {
            color: #17345f;
        }

        /* Keep header text white */
        .hero h1,
        .hero p {
            color: #ffffff !important;
        }


        /* =========================================
           FOOTER
        ========================================= */

        .footer {
            background: linear-gradient(
                135deg,
                #102f60 0%,
                #24599a 100%
            ) !important;

            color: #ffffff !important;
            text-align: center !important;
            padding: 18px !important;
            border-radius: 12px !important;
            margin-top: 35px !important;
        }

        .footer p {
            color: #ffffff !important;
            margin: 0 !important;
            font-size: 0.9rem !important;
        }


        /* =========================================
           RESPONSIVE DESIGN
        ========================================= */

        @media (max-width: 768px) {

            .hero {
                padding: 20px !important;
            }

            .hero h1 {
                font-size: 1.7rem !important;
            }

            div[data-testid="stMetric"] {
                height: auto;
            }

        }

        /* FINAL HEADER AND FOOTER OVERRIDE */

        .stApp .hero {
            background: linear-gradient(
                135deg,
                #102f60 0%,
                #24599a 55%,
                #477fc4 100%
            ) !important;
            padding: 28px !important;
            border-radius: 18px !important;
            margin-bottom: 25px !important;
        }

        .stApp .hero h1 {
            color: #ffffff !important;
        }

        .stApp .hero p {
            color: #eaf2ff !important;
        }

        .stApp .footer {
            background: linear-gradient(
                135deg,
                #102f60 0%,
                #24599a 100%
            ) !important;
            color: #ffffff !important;
            text-align: center !important;
            padding: 18px !important;
            border-radius: 12px !important;
            margin-top: 35px !important;
        }

        .stApp .footer p {
            color: #ffffff !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# HEADER
# ============================================================

def render_header():

    st.html("""
        <div class="hero">
            <h1>🛡️ Phishing Website Detection</h1>

            <p>Developed using Python, Scikit-learn and Streamlit</p>

            <p>Dataset: UCI Phishing Websites Dataset</p>

            <p>Machine Learning Assignment 2</p>
        </div>
    """)


# ============================================================
# FOOTER
# ============================================================

def render_footer():

    st.html("""
        <div class="footer">
            <p>
                Phishing Website Detection |
                Machine Learning Assignment 2
            </p>
        </div>
    """)