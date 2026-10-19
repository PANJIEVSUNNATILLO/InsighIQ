
"""Tests for InsightIQ charts."""

import pandas as pd
import pytest

from insightiq.charts import sales_by_industry_chart


def test_sales_by_industry_chart():
    summary = pd.DataFrame(
        {
            "서비스_업종_코드_명": ["Cafe", "Restaurant"],
            "estimated_sales": [300, 500],
        }
    )

    fig = sales_by_industry_chart(summary)

    assert fig.layout.title.text == "Estimated Sales by Industry"
    assert len(fig.data) == 1


def test_chart_rejects_missing_columns():
    summary = pd.DataFrame({"industry": ["Cafe"]})

    with pytest.raises(ValueError, match="Missing required columns"):
        sales_by_industry_chart(summary)
