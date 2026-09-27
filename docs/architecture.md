# Batch Data Pipeline Architecture

## Data Flow

CSV Data
   |
   v
S3 Raw Layer
   |
   v
Python ETL Transformation
   |
   v
S3 Processed Layer
   |
   v
Amazon Athena
   |
   v
SQL Analytics

## Components

- **CSV** — Source batch data
- **Amazon S3 Raw Layer** — Stores original input data
- **Python ETL** — Validates and transforms the dataset
- **Amazon S3 Processed Layer** — Stores transformed data
- **Amazon Athena** — Queries processed data using SQL
- **Athena Results** — Stores query results in Amazon S3

## Transformation

The ETL process calculates:

`total_amount = quantity × unit_price`

The processed dataset is then queried using Athena for:

- Total record count
- Regional sales
- Daily sales
- Category-level sales

## Architecture Decision

The original design considered AWS Glue and Amazon Redshift. This AWS account did not have access to Glue job creation and required Redshift service opt-in.

Therefore, the implemented project uses:

**Python ETL + Amazon S3 + Amazon Athena**

This keeps the project fully functional while demonstrating the core batch data engineering workflow.
