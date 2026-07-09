import pandas as pd
import streamlit as st
from config.settings import DATA_PATH


@st.cache_data
def load_raw_data():
    df = pd.read_csv(DATA_PATH)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Province/State"] = df["Province/State"].fillna("Unknown")
    return df


@st.cache_data
def prepare_datasets():
    covid = load_raw_data()

    covid["Active_Original"] = covid["Active"]
    covid["Active"] = covid["Active"].clip(lower=0)

    daily = (
        covid.groupby("Date")[["Confirmed", "Deaths", "Recovered", "Active"]]
        .sum()
        .reset_index()
    )

    latest_date = covid["Date"].max()
    latest = covid[covid["Date"] == latest_date].copy()

    country_latest = (
        latest.groupby(["Country/Region", "WHO Region"], as_index=False)
        .agg(
            {
                "Confirmed": "sum",
                "Deaths": "sum",
                "Recovered": "sum",
                "Active": "sum",
            }
        )
    )

    country_latest["Case Fatality Rate (%)"] = (
        country_latest["Deaths"] / country_latest["Confirmed"] * 100
    ).round(2)

    country_latest["Case Recovery Rate (%)"] = (
        country_latest["Recovered"] / country_latest["Confirmed"] * 100
    ).round(2)

    country_latest["Active Case Rate (%)"] = (
        country_latest["Active"] / country_latest["Confirmed"] * 100
    ).round(2)

    who_summary = (
        country_latest.groupby("WHO Region", as_index=False)
        .agg(
            {
                "Confirmed": "sum",
                "Deaths": "sum",
                "Recovered": "sum",
                "Active": "sum",
            }
        )
    )

    return covid, daily, latest, country_latest, who_summary