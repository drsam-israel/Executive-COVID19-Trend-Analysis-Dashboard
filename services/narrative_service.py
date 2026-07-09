def generate_global_narrative(latest_row, latest_date):
    confirmed = int(latest_row["Confirmed"])
    recovered = int(latest_row["Recovered"])
    deaths = int(latest_row["Deaths"])
    active = int(latest_row["Active"])

    recovery_rate = (recovered / confirmed * 100) if confirmed > 0 else 0
    fatality_rate = (deaths / confirmed * 100) if confirmed > 0 else 0
    active_rate = (active / confirmed * 100) if confirmed > 0 else 0

    return f"""
    As of <strong>{latest_date.date()}</strong>, the global COVID-19 dataset reports
    <strong>{confirmed:,}</strong> confirmed cases, <strong>{recovered:,}</strong> recoveries,
    <strong>{deaths:,}</strong> deaths, and <strong>{active:,}</strong> active cases.
    The recovery rate stands at <strong>{recovery_rate:.2f}%</strong>, while the case fatality rate is
    <strong>{fatality_rate:.2f}%</strong>. Active cases represent <strong>{active_rate:.2f}%</strong>
    of confirmed cases, indicating the continuing burden on healthcare systems.
    """


def generate_country_narrative(country_name, country_row):
    confirmed = int(country_row["Confirmed"])
    recovered = int(country_row["Recovered"])
    deaths = int(country_row["Deaths"])
    active = int(country_row["Active"])

    cfr = country_row["Case Fatality Rate (%)"]
    recovery = country_row["Case Recovery Rate (%)"]
    active_rate = country_row["Active Case Rate (%)"]

    return f"""
    <strong>{country_name}</strong> reports <strong>{confirmed:,}</strong> confirmed cases,
    <strong>{recovered:,}</strong> recoveries, <strong>{deaths:,}</strong> deaths, and
    <strong>{active:,}</strong> active cases. The country’s case fatality rate is
    <strong>{cfr}%</strong>, while the recovery rate is <strong>{recovery}%</strong>.
    The active case rate of <strong>{active_rate}%</strong> provides a useful indicator of current
    healthcare system pressure.
    """


def generate_region_narrative(region_name, region_row):
    confirmed = int(region_row["Confirmed"])
    recovered = int(region_row["Recovered"])
    deaths = int(region_row["Deaths"])
    active = int(region_row["Active"])

    recovery = region_row["Case Recovery Rate (%)"]
    cfr = region_row["Case Fatality Rate (%)"]
    active_rate = region_row["Active Case Rate (%)"]

    return f"""
    The <strong>{region_name}</strong> WHO region reports <strong>{confirmed:,}</strong>
    confirmed cases, <strong>{recovered:,}</strong> recoveries, <strong>{deaths:,}</strong> deaths,
    and <strong>{active:,}</strong> active cases. The regional recovery rate is
    <strong>{recovery}%</strong>, with a case fatality rate of <strong>{cfr}%</strong>.
    Active cases account for <strong>{active_rate}%</strong> of confirmed cases, supporting regional
    surveillance and resource planning.
    """


def generate_forecast_narrative(latest_cases, predicted_cases, forecast_growth):
    return f"""
    The forecasting model projects confirmed cases to reach <strong>{predicted_cases:,}</strong>
    by the end of the forecast horizon, compared with <strong>{latest_cases:,}</strong> latest
    confirmed cases. This represents an estimated <strong>{forecast_growth:.2f}%</strong> projected
    change. The forecast should be interpreted as a short-term planning signal, not a deterministic
    prediction.
    """