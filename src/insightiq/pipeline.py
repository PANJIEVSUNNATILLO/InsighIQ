
"""End-to-end analysis pipeline for InsightIQ."""

from pathlib import Path

import pandas as pd

from insightiq.analytics import summarize_sales
from insightiq.charts import sales_by_industry_chart
from insightiq.quality import summarize_quality


def run_pipeline(
    input_csv: str | Path,
    output_dir: str | Path = "outputs",
) -> dict:
    """Load a CSV, analyze sales, and export reports and a chart."""
    input_path = Path(input_csv)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        raise FileNotFoundError(f"Dataset not found: {input_path}")

    df = pd.read_csv(input_path, low_memory=False)

    quality = summarize_quality(df)
    pd.DataFrame([quality]).to_csv(
        output_path / "data_quality_report.csv",
        index=False,
    )

    industry_summary = summarize_sales(df)
    industry_summary.to_csv(
        output_path / "industry_sales_summary.csv",
        index=False,
    )

    chart = sales_by_industry_chart(industry_summary)
    chart.write_html(output_path / "sales_by_industry.html")

    return {
        "rows_analyzed": len(df),
        "industries_analyzed": len(industry_summary),
        "output_dir": str(output_path),
    }
