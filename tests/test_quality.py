
"""Tests for InsightIQ data quality checks."""

import pandas as pd

from insightiq.quality import summarize_quality


def test_summarize_quality():
    df = pd.DataFrame(
        {
            "industry": ["Cafe", "Restaurant", "Cafe"],
            "sales": [1000, None, 1000],
        }
    )

    result = summarize_quality(df)

    assert result["rows"] == 3
    assert result["columns"] == 2
    assert result["duplicate_rows"] == 1
    assert result["missing_cells"] == 1
