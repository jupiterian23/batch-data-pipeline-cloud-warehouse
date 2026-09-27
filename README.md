# 📊 Batch Data Pipeline into a Cloud Warehouse

> 🚀 An end-to-end batch data engineering project built with **Python, Amazon S3, Amazon Athena, SQL, Linux, and AWS CLI**.

This project demonstrates how raw sales data can be **validated, transformed, stored in different data layers, and analyzed using serverless SQL**.

### 🔄 Pipeline

**CSV → S3 Raw → Python ETL → S3 Processed → Amazon Athena → SQL Analytics**

---

## 🏷️ Project Highlights

| Area               | Implementation |
| ------------------ | -------------- |
| ☁️ Cloud           | AWS            |
| 🪣 Storage         | Amazon S3      |
| 🔎 Analytics       | Amazon Athena  |
| 🐍 ETL             | Python         |
| 🗄️ Query Language | SQL            |
| 🐧 Environment     | Linux          |
| 💻 Automation      | AWS CLI        |
| 📦 Version Control | Git & GitHub   |

---

# 🏗️ Architecture

```text
                    📄 CSV DATA
                        │
                        ▼
              ┌───────────────────┐
              │     S3 RAW        │
              │                   │
              │   raw/sales.csv   │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │    PYTHON ETL    │
              │                   │
              │  ✓ Validate      │
              │  ✓ Transform     │
              │  ✓ Calculate     │
              │    total_amount  │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │  S3 PROCESSED    │
              │                   │
              │ sales_processed   │
              │      .csv         │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │   AMAZON ATHENA   │
              │                   │
              │   SQL ANALYTICS   │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │  ANALYTICS        │
              │     RESULTS       │
              └───────────────────┘
```

---

# 🎯 Project Objective

The objective was to build a practical **batch data pipeline** that demonstrates how cloud-based data can move through multiple processing stages.

The pipeline performs:

1. 📥 Raw data ingestion
2. ✅ Data validation
3. 🔄 Data transformation
4. 🗂️ Raw and processed data separation
5. ☁️ S3 data storage
6. 🔎 Serverless SQL querying
7. 📊 Business analytics

---

# ☁️ AWS Services

### 🪣 Amazon S3

Used as the project's cloud storage layer.

```text
S3 Bucket
│
├── raw/
│   └── sales.csv
│
├── processed/
│   └── sales_processed.csv
│
├── scripts/
│
└── athena-results/
```

### 🔎 Amazon Athena

Used to query the processed CSV data directly from Amazon S3 using SQL.

### 🔐 AWS IAM

Used for AWS identity and access management during the project.

### 💻 AWS CLI

Used to create, upload, verify, and manage AWS resources from Linux.

---

# 🔄 Pipeline Workflow

## 1️⃣ Create the Dataset

The source dataset contains sales information including:

* 🆔 Order ID
* 📅 Order date
* 👤 Customer ID
* 📦 Product
* 🏷️ Category
* 🔢 Quantity
* 💰 Unit price
* 🌍 Region

Source file:

```text
data/sales.csv
```

---

## 2️⃣ Validate the Data

Before processing, Python validates the source dataset.

The validation checks:

* ✅ Required columns
* ✅ Dataset is not empty
* ✅ Quantity is greater than zero
* ✅ Unit price is greater than zero

Run:

```bash
python3 scripts/validate_data.py
```

Result:

```text
Data validation successful: 10 records checked.
```

---

## 3️⃣ Transform the Data

The ETL script processes the dataset and calculates the total value of every order.

### 🧮 Transformation

```text
total_amount = quantity × unit_price
```

Run:

```bash
python3 scripts/transform_data.py
```

Output:

```text
processed/sales_processed.csv
```

---

## 4️⃣ Store Processed Data

The transformed dataset is uploaded to the S3 processed layer.

```text
S3
│
├── raw/
│   └── sales.csv
│
└── processed/
    └── sales_processed.csv
```

This demonstrates a simple **raw → processed data architecture**.

---

# 🔎 Amazon Athena

Athena queries the processed S3 dataset using SQL.

The project performs:

* 📦 Total record analysis
* 🌍 Regional sales analysis
* 📅 Daily sales analysis
* 🛒 Category analysis

---

# 📊 Analytics Results

## 📦 Total Records

**10 records**

---

## 🌍 Regional Sales

| Region   | Total Sales |
| -------- | ----------: |
| 🥇 West  |     194,000 |
| 🥈 North |     118,000 |
| 🥉 South |      72,500 |

---

## 📅 Daily Sales

| Date       | Daily Sales |
| ---------- | ----------: |
| 2026-09-01 |     122,500 |
| 2026-09-02 |      57,000 |
| 2026-09-03 |      48,000 |
| 2026-09-04 |      79,000 |
| 2026-09-05 |      78,000 |

---

## 🛒 Category Analytics

| Category       | Quantity | Total Sales |
| -------------- | -------: | ----------: |
| 💻 Electronics |       25 |     294,500 |
| 🪑 Furniture   |        6 |      90,000 |

Detailed results:

```text
docs/analytics-results.txt
```

---

# 🧪 Example Athena Queries

### 📦 Count Records

```sql
SELECT COUNT(*) AS total_records
FROM batch_warehouse.sales;
```

### 🌍 Regional Sales

```sql
SELECT
    region,
    SUM(total_amount) AS total_sales
FROM batch_warehouse.sales
GROUP BY region
ORDER BY total_sales DESC;
```

### 📅 Daily Sales

```sql
SELECT
    order_date,
    SUM(total_amount) AS daily_sales
FROM batch_warehouse.sales
GROUP BY order_date
ORDER BY order_date;
```

### 🛒 Category Analytics

```sql
SELECT
    category,
    SUM(quantity) AS total_quantity,
    SUM(total_amount) AS total_sales
FROM batch_warehouse.sales
GROUP BY category
ORDER BY total_sales DESC;
```

---

# 📁 Project Structure

```text
batch-data-pipeline-cloud-warehouse/
│
├── 📂 data/
│   └── 📄 sales.csv
│
├── 📂 processed/
│   └── 📄 sales_processed.csv
│
├── 📂 scripts/
│   ├── 🐍 transform_data.py
│   └── 🐍 validate_data.py
│
├── 📂 docs/
│   ├── 📄 architecture.md
│   └── 📊 analytics-results.txt
│
├── 📄 .gitignore
└── 📄 README.md
```

---

# 💻 Running Locally

### 1️⃣ Validate the dataset

```bash
python3 scripts/validate_data.py
```

### 2️⃣ Transform the dataset

```bash
python3 scripts/transform_data.py
```

### 3️⃣ Inspect the processed dataset

```bash
head processed/sales_processed.csv
```

---

# 🧠 Key Concepts Demonstrated

### ☁️ Cloud Engineering

* Amazon S3
* Amazon Athena
* AWS IAM
* AWS CLI
* Cloud storage
* Serverless analytics

### 📊 Data Engineering

* ETL
* Batch processing
* Data validation
* Data transformation
* Data lake layers
* SQL analytics
* Aggregations

### 🛠️ Development

* Python
* SQL
* Bash
* Linux
* Git
* GitHub

---

# 🏛️ Architecture Decision

The original architecture considered:

```text
CSV
 ↓
Amazon S3
 ↓
AWS Glue
 ↓
Amazon Redshift
```

During implementation:

* AWS Glue job creation was unavailable in the AWS account.
* Amazon Redshift required service opt-in.

Therefore, the project was adapted to an available and cost-conscious architecture:

```text
CSV
 ↓
S3 Raw
 ↓
Python ETL
 ↓
S3 Processed
 ↓
Amazon Athena
 ↓
SQL Analytics
```

This allowed the complete batch data workflow to be implemented without creating a Redshift cluster.

---

# 💰 Cost Awareness

This project was intentionally designed to minimize AWS costs.

* 🪣 Small S3 datasets
* 🔎 Serverless Athena
* 🚫 No Redshift cluster
* 🚫 No long-running EC2 infrastructure
* 🧹 Resources can be cleaned up after testing

> ⚠️ Always review AWS resources after completing a project and remove resources that are no longer required.

---

# 📚 Documentation

Additional documentation:

📐 **Architecture**

```text
docs/architecture.md
```

📊 **Analytics Results**

```text
docs/analytics-results.txt
```

---

# 🚀 Skills Practiced

```text
☁️ AWS
├── Amazon S3
├── Amazon Athena
├── IAM
└── AWS CLI

📊 Data Engineering
├── ETL
├── Batch Processing
├── Data Validation
├── Data Transformation
└── SQL Analytics

💻 Development
├── Python
├── Linux
├── Bash
├── Git
└── GitHub
```

---

# 👨‍💻 Portfolio Project

This project was built as a practical **Cloud / Data Engineering portfolio project** to demonstrate hands-on experience with:

**AWS ☁️ | Python 🐍 | SQL 🗄️ | Linux 🐧 | ETL 🔄 | S3 🪣 | Athena 🔎 | GitHub 🐙**

---

⭐ **Built for hands-on cloud engineering practice and portfolio development.**
