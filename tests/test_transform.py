
import csv

from src.transform import transform_sales


# Helper function to create sample input data
def create_input_file(tmp_path):

    input_file = tmp_path / "sales.csv"

    sales_records = [
        {"order_id": "101", "amount": "500", "status": "COMPLETED"},
        {"order_id": "102", "amount": "700", "status": "PENDING"},
        {"order_id": "103", "amount": "900", "status": "COMPLETED"},
        {"order_id": "104", "amount": "300", "status": "CANCELLED"},
        {"order_id": "105", "amount": "600", "status": "COMPLETED"}
    ]

    with open(input_file, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["order_id", "amount", "status"]
        )
        writer.writeheader()
        writer.writerows(sales_records)

    return input_file


# Test 1: Check the number of completed orders
def test_completed_orders_count(tmp_path):

    input_file = create_input_file(tmp_path)
    output_file = tmp_path / "output" / "cleaned_sales.csv"

    result = transform_sales(str(input_file), str(output_file))

    assert result == 3


# Test 2: Check whether output file is created
def test_output_file_created(tmp_path):

    input_file = create_input_file(tmp_path)
    output_file = tmp_path / "output" / "cleaned_sales.csv"

    transform_sales(str(input_file), str(output_file))

    assert output_file.exists()


# Test 3: Check whether output contains three records
def test_output_record_count(tmp_path):

    input_file = create_input_file(tmp_path)
    output_file = tmp_path / "output" / "cleaned_sales.csv"

    transform_sales(str(input_file), str(output_file))

    with open(output_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        records = list(reader)

    assert len(records) == 3


# Test 4: Check whether all records are completed
def test_all_orders_are_completed(tmp_path):

    input_file = create_input_file(tmp_path)
    output_file = tmp_path / "output" / "cleaned_sales.csv"

    transform_sales(str(input_file), str(output_file))

    with open(output_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        records = list(reader)

    assert all(row["status"] == "COMPLETED" for row in records)
