
"""Interactive charts for InsightIQ."""

import pandas as pd
import plotly.express as px


def sales_by_industry_chart(
    summary: pd.DataFrame,
    industry_col: str = "서비스_업종_코드_명",
):
    """Create a horizontal bar chart of estimated sales by industry."""
    required = [industry_col, "estimated_sales"]
    missing = [column for column in required if column not in summary.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    chart_data = summary.sort_values("estimated_sales", ascending=True)

    fig = px.bar(
        chart_data,
        x="estimated_sales",
        y=industry_col,
        orientation="h",
        title="Estimated Sales by Industry",
        labels={
            "estimated_sales": "Estimated Sales (KRW)",
            industry_col: "Industry",
        },
        template="plotly_white",
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        margin={"l": 20, "r": 20, "t": 60, "b": 20},
    )

    return fig
