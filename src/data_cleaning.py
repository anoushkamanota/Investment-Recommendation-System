import pandas as pd

# Read raw data
df = pd.read_csv("data/raw/TCS.csv")

# Check missing values
print(df.isnull().sum())

# Check duplicates
print(df.duplicated().sum())

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values(by="Date")

# Save cleaned data
df.to_csv("data/processed/TCS_cleaned.csv", index=False)

print("Cleaned data saved successfully!")