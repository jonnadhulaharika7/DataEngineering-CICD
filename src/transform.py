import csv
import os


def transform_sales(input_file, output_file):

    # Read input CSV file
    with open(input_file, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        sales_data = list(reader)

    # Filter only completed orders
    completed_orders = [
        row for row in sales_data
        if row["status"] == "COMPLETED"
    ]

    # Create output directory if it does not exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Write transformed data into output CSV
    with open(output_file, mode="w", newline="") as file:
        fieldnames = ["order_id", "amount", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(completed_orders)

    return len(completed_orders)
