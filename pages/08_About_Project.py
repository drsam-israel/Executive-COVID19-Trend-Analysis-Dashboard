import streamlit as st

from config.theme import GLOBAL_CSS
from components.footer import render_footer
from components.page_header import render_page_header
from components.section import open_section, close_section
from components.metric_card import render_metric_card
from components.insight_box import render_insight
from utils.data_loader import prepare_datasets


st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

covid, daily, latest, country_latest, who_summary = prepare_datasets()

render_page_header(
    "About Project",
    "Executive COVID-19 Trend Analysis & Forecasting Dashboard | Advanced Certification in Data Science and AI Capstone Project.",
)

open_section("Project Identity")

render_insight(
    """
    <strong>Project Title:</strong> Executive COVID-19 Trend Analysis & Forecasting Dashboard<br>
    <strong>Program:</strong> Advanced Certification in Data Science and AI | Capstone Project<br>
    <strong>Institutional Branding:</strong> Indian Institute of Technology (IIT) & Intellipaat<br>
    <strong>Developer:</strong> Dr. Samuel Israel<br><br>

    This project applies Python, data science, interactive visualization, and time-series forecasting
    to analyze COVID-19 trends and transform pandemic surveillance data into executive-level intelligence.
    """
)

close_section()


open_section("Dataset Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    render_metric_card(
        "Rows",
        f"{covid.shape[0]:,}",
        "Total records",
        "blue",
    )

with c2:
    render_metric_card(
        "Countries",
        f"{country_latest['Country/Region'].nunique()}",
        "Reporting countries",
        "green",
    )

with c3:
    render_metric_card(
        "WHO Regions",
        f"{who_summary['WHO Region'].nunique()}",
        "Global regions",
        "purple",
    )

with c4:
    render_metric_card(
        "Daily Observations",
        f"{daily['Date'].nunique()}",
        "Date range coverage",
        "orange",
    )

close_section()


open_section("Project Objectives")

render_insight(
    """
    <strong>1.</strong> Load, inspect, clean, and prepare COVID-19 surveillance data.<br>
    <strong>2.</strong> Analyze global, country-level, and WHO regional COVID-19 trends.<br>
    <strong>3.</strong> Create interactive visualizations using Plotly and Streamlit.<br>
    <strong>4.</strong> Calculate epidemiological indicators including case fatality rate, recovery rate, and active-case rate.<br>
    <strong>5.</strong> Build a seven-day time-series forecasting model using Prophet.<br>
    <strong>6.</strong> Communicate findings through an executive dashboard suitable for decision-makers.
    """
)

close_section()


open_section("Technology Stack")

render_insight(
    """
    <strong>Programming Language:</strong> Python<br>
    <strong>Application Framework:</strong> Streamlit<br>
    <strong>Data Processing:</strong> Pandas, NumPy<br>
    <strong>Visualization:</strong> Plotly Express, Plotly Graph Objects<br>
    <strong>Forecasting:</strong> Prophet<br>
    <strong>Model Evaluation:</strong> Scikit-learn<br>
    <strong>Version Control:</strong> Git and GitHub<br>
    <strong>Deployment Target:</strong> Streamlit Community Cloud
    """
)

close_section()


open_section("Final Positioning")

render_insight(
    """
    This project is designed not only as a certification capstone submission, but also as a professional
    portfolio project demonstrating end-to-end data science capability: data preprocessing, exploratory
    analytics, dashboard development, epidemiological interpretation, forecasting, model evaluation,
    and executive communication.
    """
)

close_section()

render_footer()