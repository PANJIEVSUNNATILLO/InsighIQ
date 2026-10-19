
"""Tests for commercial sales analytics."""

import pandas as pd
import pytest

from insightiq.analytics import summarize_sales


def test_summarize_sales_by_industry():
    df = pd.DataFrame(
        {
            "서비스_업종_코드_명": ["Cafe", "Cafe", "Restaurant"],
            "당월_매출_금액": [100, 200, 500],
            "당월_매출_건수": [10, 20, 50],
        }
    )

    result = summarize_sales(df)

    assert result.loc[0, "서비스_업종_코드_명"] == "Restaurant"
    assert result.loc[0, "estimated_sales"] == 500
    assert result.loc[1, "estimated_sales"] == 300
    assert result.loc[1, "estimated_transactions"] == 30


def test_summarize_sales_rejects_missing_columns():
    df = pd.DataFrame({"industry": ["Cafe"]})

    with pytest.raises(ValueError, match="Missing required columns"):
        summarize_sales(df)
