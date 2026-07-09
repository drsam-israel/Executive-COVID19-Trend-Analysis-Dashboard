import streamlit as st
import plotly.express as px

from config.theme import GLOBAL_CSS
from components.footer import render_footer
from components.page_header import render_page_header
from components.section import open_section, close_section
from components.insight_box import render_insight
from utils.data_loader import prepare_datasets


st.set_page_config(
    page_title="Executive Insights",
    page_icon="📌",
    layout="wide",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

covid, daily, latest, country_latest, who_summary = prepare_datasets()

latest_date = daily["Date"].max()
latest_row = daily[daily["Date"] == latest_date].iloc[0]

top_country = country_latest.sort_values("Confirmed", ascending=False).iloc[0]
top_region = who_summary.sort_values("Confirmed", ascending=False).iloc[0]

global_cfr = (latest_row["Deaths"] / latest_row["Confirmed"] * 100).round(2)
global_recovery_rate = (latest_row["Recovered"] / latest_row["Confirmed"] * 100).round(2)
global_active_rate = (latest_row["Active"] / latest_row["Confirmed"] * 100).round(2)

render_page_header(
    "Executive Insights",
    "Strategic interpretation of global, regional, and country-level COVID-19 analytics.",
)

open_section("Executive Summary")

render_insight(
    f"""
    As of <strong>{latest_date.date()}</strong>, the global COVID-19 dataset shows
    <strong>{int(latest_row["Confirmed"]):,}</strong> confirmed cases,
    <strong>{int(latest_row["Recovered"]):,}</strong> recoveries,
    <strong>{int(latest_row["Deaths"]):,}</strong> deaths, and
    <strong>{int(latest_row["Active"]):,}</strong> active cases.
    The global case fatality rate is <strong>{global_cfr}%</strong>, while the recovery rate is
    <strong>{global_recovery_rate}%</strong>.
    """
)

close_section()

c1, c2, c3 = st.columns(3)

with c1:
    render_insight(
        f"""
        <strong>Global Burden Insight</strong><br><br>
        Confirmed cases increased across the reporting period. The country with the highest confirmed burden is
        <strong>{top_country["Country/Region"]}</strong>, with
        <strong>{int(top_country["Confirmed"]):,}</strong> confirmed cases.
        """
    )

with c2:
    render_insight(
        f"""
        <strong>Regional Intelligence</strong><br><br>
        The WHO region with the highest confirmed case burden is
        <strong>{top_region["WHO Region"]}</strong>, reporting
        <strong>{int(top_region["Confirmed"]):,}</strong> confirmed cases.
        """
    )

with c3:
    render_insight(
        f"""
        <strong>Outcome Performance</strong><br><br>
        The global recovery rate of <strong>{global_recovery_rate}%</strong> and active case rate of
        <strong>{global_active_rate}%</strong> highlight the need to monitor both resolved cases and ongoing healthcare burden.
        """
    )

open_section("Strategic Recommendations")

render_insight(
    """
    <strong>1. Strengthen regional surveillance:</strong> Regions with high confirmed case burden should prioritize
    early warning systems, testing capacity, and near-real-time reporting.<br><br>

    <strong>2. Monitor active-case pressure:</strong> Active cases remain a key signal for healthcare resource allocation,
    including hospital beds, workforce planning, oxygen supply, and critical care capacity.<br><br>

    <strong>3. Use forecasting for preparedness:</strong> Short-term time-series forecasts should support operational planning,
    surge preparedness, and public health intervention timing.<br><br>

    <strong>4. Combine epidemiological metrics with context:</strong> Case fatality and recovery rates should be interpreted
    alongside testing capacity, demographics, reporting delays, healthcare access, and policy interventions.
    """
)

close_section()

open_section("Top Countries by Confirmed Burden")

top_10 = country_latest.sort_values("Confirmed", ascending=False).head(10)

fig = px.bar(
    top_10,
    x="Confirmed",
    y="Country/Region",
    orientation="h",
    color="Confirmed",
    text="Confirmed",
    title="Top 10 Countries by Confirmed Cases",
)

fig.update_layout(
    template="plotly_white",
    yaxis={"categoryorder": "total ascending"},
    height=450,
)

fig.update_traces(texttemplate="%{text:,}")

st.plotly_chart(fig, use_container_width=True)

close_section()

render_footer()