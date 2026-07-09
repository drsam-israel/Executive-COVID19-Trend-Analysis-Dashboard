def classify_model_performance(mape, mae=None, rmse=None):
    if mape < 10:
        return {
            "overall_rating": "Excellent",
            "stars": "★★★★★",
            "model_status": "Executive Ready",
            "forecast_confidence": "Very High",
            "business_risk": "Low",
            "message": "The model demonstrates excellent forecasting performance and is suitable for executive-level monitoring and short-term planning.",
        }

    if mape < 20:
        return {
            "overall_rating": "Very Good",
            "stars": "★★★★☆",
            "model_status": "Executive Ready",
            "forecast_confidence": "High",
            "business_risk": "Low to Moderate",
            "message": "The model demonstrates strong forecasting performance and can support operational decision-making with routine monitoring.",
        }

    if mape < 50:
        return {
            "overall_rating": "Moderate",
            "stars": "★★★☆☆",
            "model_status": "Usable",
            "forecast_confidence": "Moderate",
            "business_risk": "Moderate",
            "message": "The model captures the broad trend but should be interpreted with caution due to moderate percentage error.",
        }

    return {
        "overall_rating": "Needs Improvement",
        "stars": "★★☆☆☆",
        "model_status": "Retraining Recommended",
        "forecast_confidence": "Low",
        "business_risk": "High",
        "message": "The model requires improvement before being used for high-confidence executive forecasting.",
    }


def generate_recommendations(mape):
    recommendations = [
        "Continue using Prophet for short-term trend forecasting.",
        "Monitor MAE, RMSE, and MAPE together rather than relying on a single metric.",
        "Use prediction intervals to communicate uncertainty to decision-makers.",
        "Retrain the model periodically as new surveillance data become available.",
    ]

    if mape >= 20:
        recommendations.append(
            "Benchmark Prophet against alternative models such as XGBoost, ARIMA, or LSTM."
        )

    if mape >= 50:
        recommendations.append(
            "Review preprocessing, outliers, and early low-count observations before production use."
        )

    return recommendations