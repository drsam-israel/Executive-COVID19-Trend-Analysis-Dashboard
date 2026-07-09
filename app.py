import streamlit as st
import plotly.express as px

from config.settings import APP_TITLE, APP_SUBTITLE, APP_INSTITUTION
from config.theme import GLOBAL_CSS
from components.footer import render_footer
from components.page_header import render_page_header
from components.section import open_section, close_section
from components.metric_card import render_metric_card
from components.insight_box import render_insight
from components.sidebar import render_enterprise_sidebar
from utils.data_loader import prepare_datasets
from components.sidebar import render_enterprise_sidebar

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="ðŸŒ",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

render_enterprise_sidebar()

covid, daily, latest, country_latest, who_summary = prepare_datasets()

latest_date = daily["Date"].max()
latest_row = daily[daily["Date"] == latest_date].iloc[0]

st.sidebar.title("Indian Institute of Technology (IIT) & Intellipaat")
st.sidebar.markdown("### Advanced Certification in Data Science and AI")
st.sidebar.markdown("---")
st.sidebar.info("Executive COVID-19 Trend Analysis & Forecasting Dashboard")

render_page_header(
    "Executive COVID-19 Trend Analysis & Forecasting Dashboard",
    "Advanced Certification in Data Science and AI | Capstone Project | Indian Institute of Technology (IIT) & Intellipaat",
)

open_section("Executive Command Center")

col1, col2, col3, col4 = st.columns(4)

with col1:
    render_metric_card(
        "Confirmed Cases",
        f"{int(latest_row['Confirmed']):,}",
        f"As of {latest_date.date()}",
        "blue",
    )

with col2:
    render_metric_card(
        "Recovered Cases",
        f"{int(latest_row['Recovered']):,}",
        "Cumulative recoveries",
        "green",
    )

with col3:
    render_metric_card(
        "Deaths",
        f"{int(latest_row['Deaths']):,}",
        "Cumulative deaths",
        "red",
    )

with col4:
    render_metric_card(
        "Active Cases",
        f"{int(latest_row['Active']):,}",
        "Current active burden",
        "orange",
    )

close_section()


open_section("Global Trend Overview")

fig = px.line(
    daily,
    x="Date",
    y=["Confirmed", "Recovered", "Deaths", "Active"],
    title="Global COVID-19 Trend Over Time",
)

fig.update_layout(
    template="plotly_white",
    xaxis_title="Date",
    yaxis_title="Cases",
    legend_title="Metric",
    height=540,
)

st.plotly_chart(fig, use_container_width=True)

close_section()


left, right = st.columns(2)

with left:
    open_section("WHO Regional Snapshot")

    fig_region = px.bar(
        who_summary.sort_values("Confirmed", ascending=False),
        x="Confirmed",
        y="WHO Region",
        orientation="h",
        text="Confirmed",
        color="Confirmed",
        title="Confirmed Cases by WHO Region",
    )

    fig_region.update_traces(texttemplate="%{text:,}")

    fig_region.update_layout(
        template="plotly_white",
        yaxis={"categoryorder": "total ascending"},
        height=430,
    )

    st.plotly_chart(fig_region, use_container_width=True)

    close_section()

with right:
    open_section("Top Countries Snapshot")

    top_countries = country_latest.sort_values("Confirmed", ascending=False).head(10)

    fig_country = px.bar(
        top_countries,
        x="Confirmed",
        y="Country/Region",
        orientation="h",
        text="Confirmed",
        color="Confirmed",
        title="Top 10 Countries by Confirmed Cases",
    )

    fig_country.update_traces(texttemplate="%{text:,}")

    fig_country.update_layout(
        template="plotly_white",
        yaxis={"categoryorder": "total ascending"},
        height=430,
    )

    st.plotly_chart(fig_country, use_container_width=True)

    close_section()


open_section("Project Overview")

render_insight(
    """
    This dashboard transforms COVID-19 surveillance data into executive-level intelligence using
    Python, Pandas, Plotly, Streamlit, and Prophet forecasting. It supports global trend analysis,
    country-level intelligence, WHO regional analytics, model performance evaluation, and short-term
    time-series forecasting.
    """
)

close_section()

render_footer()
