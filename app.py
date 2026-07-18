import streamlit as st 
from src.analysis import analyze_stock
from src.recommendation import recommend_stock
from src.recommendation import risk_level
from src.report_generator import generate_report

stock_files = {
    "TCS": "data/processed/TCS_cleaned.csv",
    "Infosys": "data/processed/INFY_cleaned.csv",
    "Reliance": "data/processed/RELIANCE_cleaned.csv"
}

chart_files = {
    "TCS": "assets/TCS_price_analysis.png",
    "Infosys": "assets/INFY_price_analysis.png",
    "Reliance": "assets/RELIANCE_price_analysis.png"
}

st.title("📈 Investment Recommendation System")
st.subheader("Analyze Stocks and Get Investment Recommendations")

st.divider()

st.header("Stock Recommendation Dashboard")
st.subheader("Select a Stock")

stock = st.selectbox(
    "Choose a Company",
    ["TCS", "Infosys", "Reliance"]
)

st.write("You selected :", stock)

metrics = analyze_stock(stock_files[stock])
recommendation, reason = recommend_stock(metrics)
risk = risk_level(metrics["Volatility"])

st.header("Stock Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📊 Average Return",
        f"{metrics['Average Return']:.4f}"
    )

with col2:
    st.metric(
        "⚠️ Volatility",
        f"{metrics['Volatility']:.4f}"
    )

with col3:
    st.metric(
        "💡 Recommendation",
        recommendation
    )

with col4:
    st.metric(
        "🛡 Risk Level",
        risk
    )

st.divider()

st.header("📉 Stock Price Analysis")
st.image(
    chart_files[stock],
    use_container_width=True
)

st.divider()

st.header("📝 Investment Summary")

trend = (
    "Uptrend"
    if metrics["MA20"] > metrics["MA50"]
    else "Downtrend"
)

st.write(
    f"""
Average Return:
{metrics['Average Return']:.4f}

Volatility:
{metrics['Volatility']:.4f}

Trend:
{trend}

Recommendation:
{recommendation}

Risk Level:
{risk}
"""
)

st.subheader("Reason")

st.write(reason)

report = generate_report(
    stock,
    metrics,
    recommendation,
    risk,
    reason
)

csv = report.to_csv(index=False)

st.download_button(
    label="📥 Download Recommendation Report",
    data=csv,
    file_name="stock_recommendation.csv",
    mime="text/csv"
)

