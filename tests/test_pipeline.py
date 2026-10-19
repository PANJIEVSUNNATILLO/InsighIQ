
"""Tests for the InsightIQ pipeline."""

import pandas as pd

from insightiq.pipeline import run_pipeline


def test_run_pipeline_creates_reports(tmp_path):
    input_csv = tmp_path / "sample.csv"
    output_dir = tmp_path / "outputs"

    df = pd.DataFrame(
        {
            "서비스_업종_코드_명": ["Cafe", "Restaurant", "Cafe"],
            "당월_매출_금액": [1000, 3000, 2000],
            "당월_매출_건수": [10, 30, 20],
        }
    )
    df.to_csv(input_csv, index=False)

    result = run_pipeline(input_csv, output_dir)

    assert result["rows_analyzed"] == 3
    assert result["industries_analyzed"] == 2
    assert (output_dir / "data_quality_report.csv").exists()
    assert (output_dir / "industry_sales_summary.csv").exists()
    assert (output_dir / "sales_by_industry.html").exists()
