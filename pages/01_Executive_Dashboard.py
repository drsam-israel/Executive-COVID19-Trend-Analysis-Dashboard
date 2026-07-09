import streamlit as st
import plotly.express as px

from config.theme import GLOBAL_CSS
from components.footer import render_footer
from components.page_header import render_page_header
from components.section import open_section, close_section
from components.metric_card import render_metric_card
from utils.data_loader import prepare_datasets


st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="🏠",
    layout="wide",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

covid, daily, latest, country_latest, who_summary = prepare_datasets()

latest_date = daily["Date"].max()
latest_row = daily[daily["Date"] == latest_date].iloc[0]

render_page_header(
    "Executive Dashboard",
    "Executive command center for global COVID-19 intelligence, regional burden, and time-series forecasting readiness.",
)

open_section("Executive KPI Summary")

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
    open_section("WHO Regional Burden")

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
    open_section("Top Countries by Confirmed Cases")

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


open_section("Executive Interpretation")

st.markdown(
    f"""
    The latest global COVID-19 snapshot shows <strong>{int(latest_row['Confirmed']):,}</strong>
    confirmed cases, <strong>{int(latest_row['Recovered']):,}</strong> recoveries,
    <strong>{int(latest_row['Deaths']):,}</strong> deaths, and
    <strong>{int(latest_row['Active']):,}</strong> active cases as of
    <strong>{latest_date.date()}</strong>. This dashboard provides a high-level executive view
    of global disease burden, regional distribution, and country-level impact.
    """,
    unsafe_allow_html=True,
)

close_section()

render_footer()