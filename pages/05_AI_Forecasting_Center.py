import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error

from config.theme import GLOBAL_CSS
from components.footer import render_footer
from components.page_header import render_page_header
from components.section import open_section, close_section
from components.metric_card import render_metric_card
from components.insight_box import render_insight
from utils.data_loader import prepare_datasets


st.set_page_config(
    page_title="AI Forecasting Center",
    page_icon="📈",
    layout="wide",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

covid, daily, latest, country_latest, who_summary = prepare_datasets()

forecast_data = daily[["Date", "Confirmed"]].copy()
forecast_data.columns = ["ds", "y"]

model = Prophet(
    yearly_seasonality=False,
    weekly_seasonality=True,
    daily_seasonality=False,
    interval_width=0.95,
)

model.fit(forecast_data)

future = model.make_future_dataframe(periods=7, freq="D")
forecast = model.predict(future)

comparison = forecast.merge(forecast_data, on="ds", how="left")
evaluation = comparison.dropna(subset=["y"])

mae = mean_absolute_error(evaluation["y"], evaluation["yhat"])
rmse = np.sqrt(mean_squared_error(evaluation["y"], evaluation["yhat"]))

latest_actual_date = forecast_data["ds"].max()
latest_actual_cases = int(
    forecast_data.loc[forecast_data["ds"] == latest_actual_date, "y"].values[0]
)

final_forecast = forecast.tail(7).copy()
predicted_7_day_cases = int(final_forecast["yhat"].iloc[-1])
forecast_growth = ((predicted_7_day_cases - latest_actual_cases) / latest_actual_cases) * 100


render_page_header(
    "AI Forecasting Center",
    "Seven-day global COVID-19 confirmed case forecasting using Prophet time-series modeling.",
)


open_section("Forecast Executive Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    render_metric_card(
        "Latest Confirmed Cases",
        f"{latest_actual_cases:,}",
        f"As of {latest_actual_date.date()}",
        "blue",
    )

with c2:
    render_metric_card(
        "Predicted Cases",
        f"{predicted_7_day_cases:,}",
        "Seven-day forecast endpoint",
        "green",
    )

with c3:
    render_metric_card(
        "Forecast Growth",
        f"{forecast_growth:.2f}%",
        "Projected change over seven days",
        "purple",
    )

with c4:
    render_metric_card(
        "Forecast Horizon",
        "7 Days",
        "Daily prediction frequency",
        "orange",
    )

close_section()


open_section("Historical vs Forecasted Confirmed Cases")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=forecast_data["ds"],
        y=forecast_data["y"],
        mode="lines",
        name="Actual Confirmed Cases",
        line=dict(width=3),
    )
)

fig.add_trace(
    go.Scatter(
        x=forecast["ds"],
        y=forecast["yhat"],
        mode="lines",
        name="Forecast",
        line=dict(width=3, dash="dash"),
    )
)

fig.add_trace(
    go.Scatter(
        x=forecast["ds"],
        y=forecast["yhat_upper"],
        mode="lines",
        name="Upper Confidence Interval",
        line=dict(width=0),
        showlegend=False,
    )
)

fig.add_trace(
    go.Scatter(
        x=forecast["ds"],
        y=forecast["yhat_lower"],
        mode="lines",
        name="95% Confidence Interval",
        fill="tonexty",
        line=dict(width=0),
    )
)

fig.add_vline(
    x=latest_actual_date,
    line_width=2,
    line_dash="dash",
    line_color="gray",
)

fig.update_layout(
    template="plotly_white",
    height=560,
    xaxis_title="Date",
    yaxis_title="Confirmed Cases",
    legend_title="Series",
)

st.plotly_chart(fig, use_container_width=True)

close_section()


left, right = st.columns([1.2, 1])

with left:
    open_section("Seven-Day Forecast Table")

    forecast_table = final_forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].copy()
    forecast_table.columns = [
        "Date",
        "Predicted Cases",
        "Lower 95% CI",
        "Upper 95% CI",
    ]

    forecast_table["Date"] = forecast_table["Date"].dt.date
    forecast_table["Predicted Cases"] = forecast_table["Predicted Cases"].round(0).astype(int)
    forecast_table["Lower 95% CI"] = forecast_table["Lower 95% CI"].round(0).astype(int)
    forecast_table["Upper 95% CI"] = forecast_table["Upper 95% CI"].round(0).astype(int)

    st.dataframe(forecast_table, use_container_width=True)

    close_section()

with right:
    open_section("Model Performance")

    p1, p2 = st.columns(2)

    with p1:
        render_metric_card(
            "MAE",
            f"{mae:,.0f}",
            "Mean absolute error",
            "red",
        )

    with p2:
        render_metric_card(
            "RMSE",
            f"{rmse:,.0f}",
            "Root mean squared error",
            "purple",
        )

    close_section()


open_section("Executive Forecast Insight")

render_insight(
    f"""
    The Prophet model projects global confirmed COVID-19 cases to reach
    <strong>{predicted_7_day_cases:,}</strong> by the end of the seven-day forecast window,
    compared with <strong>{latest_actual_cases:,}</strong> confirmed cases on the latest actual reporting date.
    This represents an estimated <strong>{forecast_growth:.2f}%</strong> change over the forecast horizon.
    The confidence interval provides a planning range for uncertainty in short-term epidemic forecasting.
    """
)

close_section()

render_footer()