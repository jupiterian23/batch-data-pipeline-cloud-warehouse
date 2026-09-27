import csv
from pathlib import Path

file_path = Path("data/sales.csv")

required_columns = {
    "order_id",
    "order_date",
    "customer_id",
    "product",
    "category",
    "quantity",
    "unit_price",
    "region",
}

with file_path.open(newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    missing_columns = required_columns - set(reader.fieldnames or [])

    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    rows = list(reader)

if not rows:
    raise ValueError("CSV file is empty")

for row in rows:
    if int(row["quantity"]) <= 0:
        raise ValueError(f"Invalid quantity: {row}")

    if float(row["unit_price"]) <= 0:
        raise ValueError(f"Invalid unit price: {row}")

print(f"Data validation successful: {len(rows)} records checked.")
