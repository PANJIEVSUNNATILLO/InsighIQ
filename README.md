InsightIQ — AI Commercial Intelligence

Turning commercial sales data into actionable business insights.

InsightIQ is a Python-based commercial intelligence project designed to assess data quality, analyze sales performance by industry, and generate interactive visualizations. The project uses automated tests and continuous integration to support reliable, maintainable analysis.

Project Goals

* Assess dataset quality by measuring missing values and duplicate rows.
* Summarize sales and transaction counts by industry.
* Generate interactive sales visualizations using Plotly.
* Export analysis results into reusable CSV reports.
* Validate core functionality with automated tests and GitHub Actions.

Features

Data Quality Analysis

Produces a basic data quality report containing:

* Number of rows and columns
* Duplicate row count
* Total number of missing cells

Sales Analytics

Aggregates estimated sales and transaction counts by industry, then sorts industries by estimated sales.

Interactive Visualization

Creates an interactive horizontal bar chart showing estimated sales by industry.

Automated Testing

Uses pytest to test data quality checks, sales aggregation, chart creation, and pipeline outputs. GitHub Actions runs the tests automatically when changes are pushed to main or a pull request targets main.

Tech Stack

* Python 3.11
* Pandas — data manipulation and analysis
* NumPy — numerical computing
* Plotly — interactive visualizations
* Pytest — automated testing
* GitHub Actions — continuous integration

Project Structure

InsightIQ/
├── .github/
│   └── workflows/
│       └── tests.yml
├── src/
│   └── insightiq/
│       ├── __init__.py
│       ├── quality.py
│       ├── analytics.py
│       ├── charts.py
│       └── pipeline.py
├── tests/
│   ├── test_quality.py
│   ├── test_analytics.py
│   ├── test_charts.py
│   └── test_pipeline.py
├── requirements.txt
└── README.md

Getting Started

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/InsightIQ.git
cd InsightIQ

Replace YOUR-USERNAME with your GitHub username.

2. Create a virtual environment

python -m venv .venv

Activate it:

Windows

.venv\Scripts\activate

macOS/Linux

source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run the tests

macOS/Linux

PYTHONPATH=src python -m pytest -v

Windows PowerShell

$env:PYTHONPATH="src"
python -m pytest -v

Running the Analysis Pipeline

Prepare a CSV dataset containing these columns:

* 서비스_업종_코드_명 — industry name
* 당월_매출_금액 — current-month sales amount
* 당월_매출_건수 — current-month transaction count

Then run the pipeline from the repository root:

PYTHONPATH=src python -c "from insightiq.pipeline import run_pipeline; print(run_pipeline('data/your_dataset.csv'))"

Replace data/your_dataset.csv with the path to your dataset.

The pipeline creates an outputs/ directory containing:

* data_quality_report.csv
* industry_sales_summary.csv
* sales_by_industry.html

Open sales_by_industry.html in a web browser to explore the interactive chart.

Current Status

* [x]	Data quality checks
* [x]	Industry-level sales aggregation
* [x]	Interactive Plotly chart
* [x]	Automated tests
* [x]	GitHub Actions workflow
* [x]	End-to-end analysis pipeline implementation

Note: The pipeline expects the specified Korean column names. Actual dataset compatibility and analysis results should be verified using the intended dataset.

Future Improvements

* Add a user-friendly dashboard.
* Expand data validation and error reporting.
* Explore trends across locations and time periods.
* Add further commercial performance metrics.

⸻

InsightIQ is a portfolio project exploring practical data engineering, analytics, and business intelligence workflows.
