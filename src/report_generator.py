import pandas as pd
from pathlib import Path

def generate_report(company, metrics, recommendation, risk, reason):

    report = pd.DataFrame({
        "Company": [company],
        "Average Return": [metrics["Average Return"]],
        "Volatility": [metrics["Volatility"]],
        "Recommendation": [recommendation],
        "Risk Level": [risk],
        "Reason": [reason]
    })

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    report.to_csv(
        reports_dir / "stock_recommendation.csv",
        index=False
    )

    return report
