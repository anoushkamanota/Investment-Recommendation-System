# Investment Recommendation System

## 1. Project Objective

To build a software application that analyzes historical stock market data and provides Buy, Hold, or Sell recommendations based on financial analysis using historical stock price data.


## 2. Problem Statement

Many beginner investors find it difficult to analyze stocks and make informed investment decisions. This system simplifies the process by analyzing historical stock data and providing easy-to-understand investment recommendations.


## 3. Target Users

- Beginner Investors
- Students learning Finance and Data Analytics
- Individual Investors


## 4. Inputs

- Stock Symbol (TCS, Infosys, Reliance)
- Historical Stock Data
- Investment Amount (Future Enhancement)


## 5. Outputs

- Historical Price Data
- Daily Returns
- Moving Averages (20-Day & 50-Day)
- Volatility Analysis
- Risk Analysis
- Price Trend Charts
- Buy/Hold/Sell Recommendation
- Comparison Report


## 6. Project Modules

### Module 1 – Data Collection ✅
- Download historical stock data using yfinance
- Save raw CSV files

### Module 2 – Data Cleaning ✅
- Handle missing values
- Remove duplicate records
- Sort data by date
- Save cleaned datasets

### Module 3 – Financial Analysis ✅
- Calculate Daily Returns
- Calculate Moving Averages (MA20 & MA50)
- Calculate Volatility
- Generate summary metrics

### Module 4 – Multi-Stock Comparison ✅
- Compare TCS, Infosys, and Reliance
- Analyze Return vs Risk
- Generate comparison table

### Module 5 – Recommendation Engine ✅
- Rule-based Buy/Hold/Sell recommendation
- Explain recommendation using financial metrics

### Module 6 – Data Visualization ✅
- Plot Closing Price
- Plot 20-Day Moving Average
- Plot 50-Day Moving Average
- Save charts

### Module 7 – Streamlit Dashboard ✅
- Select stock from dropdown
- Display financial metrics
- Show recommendation
- Display stock chart


## 7. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- yfinance
- Streamlit
- Jupyter Notebook
- VS Code


## 8. Project Workflow

Historical Stock Data

↓

Data Collection

↓

Data Cleaning

↓

Financial Analysis

↓

Multi-Stock Comparison

↓

Recommendation Engine

↓

Visualization

↓

Streamlit Dashboard

↓

Final Investment Recommendation


## 9. Current Project Status

| Module | Status |
|--------|--------|
| Data Collection | ✅ Completed |
| Data Cleaning | ✅ Completed |
| Financial Analysis | ✅ Completed |
| Multi-Stock Analysis | ✅ Completed |
| Recommendation Engine | ✅ Completed |
| Visualization | ✅ Completed |
| Streamlit Dashboard | ✅ Completed |


## 10. Future Improvements

- Add support for more stocks
- Fetch live market data
- Include company financial statements
- Add technical indicators (RSI, MACD, Bollinger Bands)
- Implement Machine Learning models for prediction
- Add portfolio optimization
- Perform news sentiment analysis


## 11. Expected Outcome

The project provides an end-to-end stock analysis system that automates data collection, preprocessing, financial analysis, visualization, and rule-based investment recommendations. It demonstrates the practical application of Python, data analysis, and financial concepts through an interactive Streamlit dashboard.