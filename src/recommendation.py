
def recommend_stock(metrics):

    average_return = metrics["Average Return"]

    volatility = metrics["Volatility"]

    ma20 = metrics["MA20"]
    ma50 = metrics["MA50"]

    if(average_return > 0 and ma20 > ma50 and volatility < 0.02):

        recommendation = "BUY"

        reason = (
            "Investment Rationale:\n\n"
            "The stock demonstrates a positive average daily return over the selected period, "
            "indicating consistent growth. The 20-day moving average remains above the "
            "50-day moving average, suggesting a bullish market trend. Daily return "
            "volatility is moderate, indicating manageable investment risk. Based on these "
            "technical indicators, the stock receives a BUY recommendation."
        )

    elif(average_return < 0 and ma20 < ma50):

        recommendation = "SELL"

        reason = (
            "Investment Rationale:\n\n"
            "The stock has produced a negative average daily return over the selected "
            "period. The 20-day moving average remains below the 50-day moving average, "
            "indicating bearish momentum. Although volatility may vary, the overall trend "
            "suggests weakening price performance. Based on these indicators, the stock "
            "receives a SELL recommendation."
        )

    else:

        recommendation = "HOLD"

        reason = (
            "Investment Rationale:\n\n"
            "The stock is currently showing stable returns without a strong upward or "
            "downward trend. The moving averages are close together, indicating market "
            "consolidation rather than a clear trend. Since the available indicators do "
            "not provide a strong buy or sell signal, a HOLD recommendation is appropriate."
        )

    return recommendation, reason


def risk_level(volatility):
    if(volatility < 0.01):
        return "Low"
    elif(volatility < 0.02):
        return "Medium"
    else:
        return "High"
    
   