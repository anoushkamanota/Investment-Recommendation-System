import pandas as pd

def analyze_stock(file_path):
    """
    Reads a cleaned stock CSV and calculates
    important financial metrics.
    """

    df = pd.read_csv(file_path)

    #Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    #Calculate daily percentage return
    df["Daily Return"] = df["Close"].pct_change()

    #Moving Averages
    df["MA20"] = df["Close"].rolling(window=20).mean()

    df["MA50"] = df["Close"].rolling(window=50).mean()
    
    #Metrics
    average_return = df["Daily Return"].mean()

    volatility = df["Daily Return"].std()

    latest_ma20 = df["MA20"].iloc[-1]

    latest_ma50 = df["MA50"].iloc[-1]

    # Save analyzed file
    output_file = file_path.replace("_cleaned.csv", "_analysis.csv")
    df.to_csv(output_file, index=False)

    return {
        "data": df,
        "Average Return": average_return,
        "Volatility": volatility,
        "MA20": latest_ma20,
        "MA50": latest_ma50
    }

tcs = analyze_stock("data/processed/TCS_cleaned.csv")

print(tcs)

