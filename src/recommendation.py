
def recommend_stock(metrics):

    average_return = metrics["Average Return"]

    volatility = metrics["Volatility"]

    ma20 = metrics["MA20"]
    ma50 = metrics["MA50"]

    if(average_return > 0 and ma20 > ma50 and volatility < 0.02):

        recommendation = "BUY"

        reason = (
            "Positive average return, "
            "20-day moving average is above "
            "50-day moving average, "
            "and volatility is moderate."
        )

    elif(average_return < 0 and ma20 < ma50):

        recommendation = "SELL"

        reason = (
            "Negative average return and "
            "20-day moving average is below "
            "50-day moving average, "
            "indicating a downward trend."
        )

    else:

        recommendation = "HOLD"

        reason = (
            "Returns are stable and "
            "no strong upward or downward "
            "trend is observed."
        )

    return recommendation, reason

# infy = analyze_stock("data/processed/INFY_cleaned.csv")

# recommendation, reason = recommend_stock(infy)

# print(recommendation)
# print(reason)



#  stocks = {

#      "TCS":"data/processed/TCS_cleaned.csv",

#      "Infosys":"data/processed/INFY_cleaned.csv",

#      "Reliance":"data/processed/RELIANCE_cleaned.csv"

#  }

#  for company, file in stocks.items():

#      metrics = analyze_stock(file)

#      recommendation, reason = recommend_stock(metrics)

#      print(f"\n{company}")
#      print("Recommendation:", recommendation)
#      print("Reason:", reason)

def risk_level(volatility):
    if(volatility < 0.01):
        return "Low"
    elif(volatility):
        return "Medium"
    else:
        return "High"
    