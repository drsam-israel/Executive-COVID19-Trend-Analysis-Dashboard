import streamlit as st
import plotly.express as px

from config.theme import GLOBAL_CSS
from components.footer import render_footer
from components.page_header import render_page_header
from components.section import open_section, close_section
from components.metric_card import render_metric_card
from utils.data_loader import prepare_datasets


st.set_page_config(
    page_title="Country Intelligence",
    page_icon="🌐",
    layout="wide",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

covid, daily, latest, country_latest, who_summary = prepare_datasets()

top_left, top_right = st.columns([3, 1])

with top_left:
    render_page_header(
        "Country Intelligence",
        "Explore country-level COVID-19 burden and key epidemiological indicators.",
    )

with top_right:
    selected_country = st.selectbox(
        "Select a Country",
        sorted(country_latest["Country/Region"].unique()),
    )

country_row = country_latest[
    country_latest["Country/Region"] == selected_country
].iloc[0]


open_section("COVID-19 Case Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    render_metric_card(
        "Confirmed Cases",
        f"{int(country_row['Confirmed']):,}",
        "Total confirmed cases",
        "blue",
    )

with c2:
    render_metric_card(
        "Recovered Cases",
        f"{int(country_row['Recovered']):,}",
        "Total recovered cases",
        "green",
    )

with c3:
    render_metric_card(
        "Deaths",
        f"{int(country_row['Deaths']):,}",
        "Total deaths",
        "red",
    )

with c4:
    render_metric_card(
        "Active Cases",
        f"{int(country_row['Active']):,}",
        "Current active cases",
        "orange",
    )

close_section()


open_section("Epidemiological Indicators")

i1, i2, i3 = st.columns(3)

with i1:
    render_metric_card(
        "Case Fatality Rate",
        f"{country_row['Case Fatality Rate (%)']}%",
        "Deaths as percentage of confirmed cases",
        "purple",
    )

with i2:
    render_metric_card(
        "Case Recovery Rate",
        f"{country_row['Case Recovery Rate (%)']}%",
        "Recoveries as percentage of confirmed cases",
        "teal",
    )

with i3:
    render_metric_card(
        "Active Case Rate",
        f"{country_row['Active Case Rate (%)']}%",
        "Active cases as percentage of confirmed cases",
        "blue",
    )

close_section()


chart1, chart2 = st.columns(2)

with chart1:
    st.markdown("### Top 10 Countries by Confirmed Cases")

    top_confirmed = country_latest.sort_values(
        by="Confirmed",
        ascending=False,
    ).head(10)

    fig_confirmed = px.bar(
        top_confirmed,
        x="Confirmed",
        y="Country/Region",
        orientation="h",
        color="Confirmed",
        text="Confirmed",
        title="Top 10 Countries by Confirmed COVID-19 Cases",
    )

    fig_confirmed.update_layout(
        template="plotly_white",
        yaxis={"categoryorder": "total ascending"},
        height=450,
    )

    fig_confirmed.update_traces(texttemplate="%{text:,}")
    st.plotly_chart(fig_confirmed, use_container_width=True)

with chart2:
    st.markdown("### Top 10 Countries by Deaths")

    top_deaths = country_latest.sort_values(
        by="Deaths",
        ascending=False,
    ).head(10)

    fig_deaths = px.bar(
        top_deaths,
        x="Deaths",
        y="Country/Region",
        orientation="h",
        color="Deaths",
        text="Deaths",
        title="Top 10 Countries by COVID-19 Deaths",
    )

    fig_deaths.update_layout(
        template="plotly_white",
        yaxis={"categoryorder": "total ascending"},
        height=450,
    )

    fig_deaths.update_traces(texttemplate="%{text:,}")
    st.plotly_chart(fig_deaths, use_container_width=True)


open_section("Global Distribution of Confirmed Cases")

fig_map = px.choropleth(
    country_latest,
    locations="Country/Region",
    locationmode="country names",
    color="Confirmed",
    hover_name="Country/Region",
    hover_data=[
        "Confirmed",
        "Deaths",
        "Recovered",
        "Active",
        "Case Fatality Rate (%)",
        "Case Recovery Rate (%)",
    ],
    color_continuous_scale="Reds",
    title="Global Distribution of Confirmed COVID-19 Cases",
)

fig_map.update_layout(template="plotly_white", height=520)
st.plotly_chart(fig_map, use_container_width=True)

close_section()


open_section("Country-Level Data")

st.dataframe(
    country_latest.sort_values(by="Confirmed", ascending=False),
    use_container_width=True,
)

close_section()

render_footer()