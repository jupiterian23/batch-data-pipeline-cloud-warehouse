import csv
from pathlib import Path

input_file = Path("data/sales.csv")
output_file = Path("processed/sales_processed.csv")

with input_file.open(newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    fieldnames = reader.fieldnames + ["total_amount"]

    with output_file.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            row["total_amount"] = (
                int(row["quantity"]) * float(row["unit_price"])
            )
            writer.writerow(row)

print(f"Transformation complete: {output_file}")
