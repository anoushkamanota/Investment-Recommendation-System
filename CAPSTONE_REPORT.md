# Investment Recommendation System

## Project Objective

The objective of this project is to design and develop a Python-based Investment Recommendation System that analyzes historical stock market data and generates Buy, Hold, or Sell recommendations using technical analysis indicators. The system also provides an interactive Streamlit dashboard to help users visualize stock performance and understand investment decisions.

## Problem Statement

Many beginner investors find it difficult to interpret stock market data and make informed investment decisions. Manual analysis of historical price trends and financial indicators can be time-consuming and confusing. This project aims to simplify the investment decision-making process by automatically analyzing stock data and providing easy-to-understand recommendations.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- yfinance
- Streamlit
- Git
- GitHub

## Project Workflow

1. Collect historical stock market data using yfinance.
2. Clean and preprocess the collected data.
3. Calculate financial metrics including Daily Return, Moving Averages, and Volatility.
4. Apply rule-based investment recommendation logic.
5. Generate Buy, Hold, or Sell recommendations.
6. Display results using an interactive Streamlit dashboard.
7. Allow users to download recommendation reports.

## Financial Metrics

### Daily Return
Measures the percentage change in stock price between consecutive trading days and helps evaluate short-term performance.

### Moving Average (MA20 and MA50)
The 20-day and 50-day moving averages are used to identify short-term and medium-term market trends.

### Volatility
Volatility measures the variation in daily returns and represents the investment risk associated with a stock.

## Recommendation Logic

BUY:
- Average Return > 0
- MA20 > MA50
- Volatility < 0.02

HOLD:
- Mixed market signals
- No strong trend

SELL:
- Average Return < 0
- MA20 < MA50
