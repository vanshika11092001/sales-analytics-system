from utils.file_handler import read_sales_file
from utils.data_processor import clean_and_validate_records
from utils.api_handler import fetch_product_info

def generate_report(clean_data):
    total_revenue = 0
    region_sales = {}

    for record in clean_data:
        revenue = record["Quantity"] * record["UnitPrice"]
        total_revenue += revenue

        region = record["Region"]
        region_sales[region] = region_sales.get(region, 0) + revenue

    return total_revenue, region_sales


def main():
    header, records = read_sales_file("data/sales_data.txt")
    clean_data = clean_and_validate_records(records)

    total_revenue, region_sales = generate_report(clean_data)

    with open("output/summary_report.txt", "w") as f:
        f.write(f"Total Revenue: {total_revenue}\n")
        f.write("Revenue by Region:\n")
        for region, revenue in region_sales.items():
            f.write(f"{region}: {revenue}\n")

    print("\nReport generated: output/summary_report.txt")


if __name__ == "__main__":
    main()
