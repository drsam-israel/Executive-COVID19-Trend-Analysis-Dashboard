import streamlit as st
import plotly.express as px

from config.theme import GLOBAL_CSS
from components.footer import render_footer
from components.page_header import render_page_header
from components.section import open_section, close_section
from components.metric_card import render_metric_card
from utils.data_loader import prepare_datasets
from components.insight_box import render_insight
from services.narrative_service import generate_global_narrative

st.set_page_config(
    page_title="Global COVID-19 Analytics",
    page_icon="🌐",
    layout="wide",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

covid, daily, latest, country_latest, who_summary = prepare_datasets()

latest_date = daily["Date"].max()
latest_row = daily[daily["Date"] == latest_date].iloc[0]

render_page_header(
    "Global COVID-19 Analytics",
    "Analyze global COVID-19 trends across confirmed cases, recoveries, deaths, and active cases.",
)

open_section("Global Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    render_metric_card(
        "Confirmed Cases",
        f"{int(latest_row['Confirmed']):,}",
        f"As of {latest_date.date()}",
        "blue",
    )

with c2:
    render_metric_card(
        "Recovered Cases",
        f"{int(latest_row['Recovered']):,}",
        "Cumulative recoveries",
        "green",
    )

with c3:
    render_metric_card(
        "Deaths",
        f"{int(latest_row['Deaths']):,}",
        "Cumulative deaths",
        "red",
    )

with c4:
    render_metric_card(
        "Active Cases",
        f"{int(latest_row['Active']):,}",
        "Current active burden",
        "orange",
    )

close_section()


open_section("Global Daily Trend")

st.markdown("#### Select metrics to visualize")

col_a, col_b, col_c, col_d = st.columns(4)

with col_a:
    confirmed_selected = st.checkbox("Confirmed", value=True)

with col_b:
    recovered_selected = st.checkbox("Recovered", value=True)

with col_c:
    deaths_selected = st.checkbox("Deaths", value=True)

with col_d:
    active_selected = st.checkbox("Active", value=True)

selected_metrics = []

if confirmed_selected:
    selected_metrics.append("Confirmed")

if recovered_selected:
    selected_metrics.append("Recovered")

if deaths_selected:
    selected_metrics.append("Deaths")

if active_selected:
    selected_metrics.append("Active")

if not selected_metrics:
    st.warning("Please select at least one metric to visualize.")
    selected_metrics = ["Confirmed"]

fig = px.line(
    daily,
    x="Date",
    y=selected_metrics,
    title="Global COVID-19 Daily Trend",
)

fig.update_layout(
    template="plotly_white",
    xaxis_title="Date",
    yaxis_title="Cases",
    legend_title="Metric",
    height=520,
)

st.plotly_chart(fig, use_container_width=True)

close_section()


open_section("Individual Trend Analysis")

col1, col2 = st.columns(2)

with col1:
    fig_confirmed = px.line(
        daily,
        x="Date",
        y="Confirmed",
        title="Confirmed Cases Over Time",
    )
    fig_confirmed.update_layout(template="plotly_white", height=420)
    st.plotly_chart(fig_confirmed, use_container_width=True)

with col2:
    fig_recovered = px.line(
        daily,
        x="Date",
        y="Recovered",
        title="Recoveries Over Time",
    )
    fig_recovered.update_layout(template="plotly_white", height=420)
    st.plotly_chart(fig_recovered, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    fig_deaths = px.line(
        daily,
        x="Date",
        y="Deaths",
        title="Deaths Over Time",
    )
    fig_deaths.update_layout(template="plotly_white", height=420)
    st.plotly_chart(fig_deaths, use_container_width=True)

with col4:
    fig_active = px.line(
        daily,
        x="Date",
        y="Active",
        title="Active Cases Over Time",
    )
    fig_active.update_layout(template="plotly_white", height=420)
    st.plotly_chart(fig_active, use_container_width=True)

close_section()


open_section("Global Summary Table")

st.dataframe(
    daily.tail(20),
    use_container_width=True,
)

open_section("Executive Narrative")

render_insight(
    generate_global_narrative(latest_row, latest_date)
)

close_section()

render_footer()