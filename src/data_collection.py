import yfinance as yf

# Download TCS stock data
START_DATE = "2024-01-01"
END_DATE = "2025-01-01"

tcs = yf.download("TCS.NS", start=START_DATE, end=END_DATE)

# Flatten MultiIndex columns (needed for recent yfinance versions)
tcs.columns = tcs.columns.get_level_values(0)

# Save raw data
tcs.to_csv("data/raw/TCS.csv")

print("Raw data saved successfully!")