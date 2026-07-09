import streamlit as st
import plotly.express as px
import numpy as np

from config.theme import GLOBAL_CSS
from components.footer import render_footer
from components.page_header import render_page_header
from components.section import open_section, close_section
from components.metric_card import render_metric_card
from utils.data_loader import prepare_datasets


st.set_page_config(
    page_title="WHO Regional Analytics",
    page_icon="🌐",
    layout="wide",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

covid, daily, latest, country_latest, who_summary = prepare_datasets()

who_summary["Case Fatality Rate (%)"] = np.where(
    who_summary["Confirmed"] > 0,
    who_summary["Deaths"] / who_summary["Confirmed"] * 100,
    0,
).round(2)

who_summary["Case Recovery Rate (%)"] = np.where(
    who_summary["Confirmed"] > 0,
    who_summary["Recovered"] / who_summary["Confirmed"] * 100,
    0,
).round(2)

who_summary["Active Case Rate (%)"] = np.where(
    who_summary["Confirmed"] > 0,
    who_summary["Active"] / who_summary["Confirmed"] * 100,
    0,
).round(2)

top_left, top_right = st.columns([3, 1])

with top_left:
    render_page_header(
        "WHO Regional Analytics",
        "Analyze COVID-19 burden, recovery, fatality, and active-case patterns across WHO regions.",
    )

with top_right:
    selected_region = st.selectbox(
        "Select WHO Region",
        sorted(who_summary["WHO Region"].unique()),
    )

region_row = who_summary[who_summary["WHO Region"] == selected_region].iloc[0]


open_section("WHO Regional Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    render_metric_card(
        "WHO Regions",
        f"{who_summary['WHO Region'].nunique()}",
        "Reporting regional groups",
        "blue",
    )

with c2:
    render_metric_card(
        "Confirmed Cases",
        f"{int(who_summary['Confirmed'].sum()):,}",
        "Global confirmed burden",
        "green",
    )

with c3:
    render_metric_card(
        "Deaths",
        f"{int(who_summary['Deaths'].sum()):,}",
        "Global mortality burden",
        "red",
    )

with c4:
    render_metric_card(
        "Active Cases",
        f"{int(who_summary['Active'].sum()):,}",
        "Current global active burden",
        "orange",
    )

close_section()


open_section(f"{selected_region} Regional Intelligence")

r1, r2, r3, r4 = st.columns(4)

with r1:
    render_metric_card(
        "Confirmed Cases",
        f"{int(region_row['Confirmed']):,}",
        "Total confirmed cases",
        "blue",
    )

with r2:
    render_metric_card(
        "Recovered Cases",
        f"{int(region_row['Recovered']):,}",
        "Total recovered cases",
        "green",
    )

with r3:
    render_metric_card(
        "Deaths",
        f"{int(region_row['Deaths']):,}",
        "Total deaths",
        "red",
    )

with r4:
    render_metric_card(
        "Recovery Rate",
        f"{region_row['Case Recovery Rate (%)']}%",
        "Recoveries as share of confirmed cases",
        "teal",
    )

close_section()


chart1, chart2 = st.columns(2)

with chart1:
    st.markdown("### Regional Case Burden")

    fig_confirmed = px.bar(
        who_summary.sort_values("Confirmed", ascending=False),
        x="Confirmed",
        y="WHO Region",
        orientation="h",
        color="Confirmed",
        text="Confirmed",
        title="Confirmed COVID-19 Cases by WHO Region",
    )

    fig_confirmed.update_layout(
        template="plotly_white",
        showlegend=False,
        height=450,
        yaxis={"categoryorder": "total ascending"},
    )

    fig_confirmed.update_traces(texttemplate="%{text:,}")
    st.plotly_chart(fig_confirmed, use_container_width=True)

with chart2:
    st.markdown("### Regional Outcome Comparison")

    fig_grouped = px.bar(
        who_summary.sort_values("Confirmed", ascending=False),
        x="WHO Region",
        y=["Recovered", "Deaths", "Active"],
        barmode="group",
        title="WHO Regional Outcome Comparison",
    )

    fig_grouped.update_layout(
        template="plotly_white",
        xaxis_title="WHO Region",
        yaxis_title="Cases",
        legend_title="Metric",
        height=450,
    )

    st.plotly_chart(fig_grouped, use_container_width=True)


open_section("Regional Epidemiological Indicators")

fig_rates = px.bar(
    who_summary,
    x="WHO Region",
    y=[
        "Case Fatality Rate (%)",
        "Case Recovery Rate (%)",
        "Active Case Rate (%)",
    ],
    barmode="group",
    title="WHO Regional Fatality, Recovery, and Active Case Rates",
)

fig_rates.update_layout(
    template="plotly_white",
    xaxis_title="WHO Region",
    yaxis_title="Rate (%)",
    legend_title="Indicator",
    height=480,
)

st.plotly_chart(fig_rates, use_container_width=True)

close_section()


open_section("WHO Regional Heatmap")

fig_heatmap = px.imshow(
    who_summary[
        [
            "Confirmed",
            "Deaths",
            "Recovered",
            "Active",
            "Case Fatality Rate (%)",
            "Case Recovery Rate (%)",
            "Active Case Rate (%)",
        ]
    ],
    x=[
        "Confirmed",
        "Deaths",
        "Recovered",
        "Active",
        "CFR (%)",
        "Recovery (%)",
        "Active (%)",
    ],
    y=who_summary["WHO Region"],
    text_auto=True,
    aspect="auto",
    title="WHO Regional COVID-19 Indicator Heatmap",
)

fig_heatmap.update_layout(template="plotly_white", height=520)

st.plotly_chart(fig_heatmap, use_container_width=True)

close_section()


st.markdown("### WHO Regional Data Table")

st.dataframe(
    who_summary.sort_values("Confirmed", ascending=False),
    use_container_width=True,
)

render_footer()