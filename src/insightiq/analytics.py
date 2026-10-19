
"""Commercial sales analytics for InsightIQ."""

import pandas as pd


def summarize_sales(
    df: pd.DataFrame,
    industry_col: str = "서비스_업종_코드_명",
    sales_col: str = "당월_매출_금액",
    count_col: str = "당월_매출_건수",
) -> pd.DataFrame:
    """Aggregate estimated sales and transaction counts by industry."""
    required = [industry_col, sales_col, count_col]
    missing = [column for column in required if column not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    data = df[required].copy()

    data[sales_col] = pd.to_numeric(data[sales_col], errors="coerce")
    data[count_col] = pd.to_numeric(data[count_col], errors="coerce")

    summary = (
        data.groupby(industry_col, dropna=False)
        .agg(
            estimated_sales=(sales_col, "sum"),
            estimated_transactions=(count_col, "sum"),
            records=(industry_col, "size"),
        )
        .reset_index()
        .sort_values("estimated_sales", ascending=False)
        .reset_index(drop=True)
    )

    return summary
