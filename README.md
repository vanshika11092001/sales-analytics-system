# Sales Analytics System

## Project Overview
This project is a Python-based Sales Data Analytics System that reads raw sales transaction data, cleans and validates it, analyzes sales performance, and generates a summary report for business decision-making.

## Features
- Reads pipe-delimited sales data from a text file
- Handles non-UTF-8 encoded data
- Cleans messy data (commas in names and numbers)
- Removes invalid records based on given rules
- Analyzes total revenue and region-wise revenue
- Generates a summary report

## Project Structure
sales-analytics-system/
├── main.py
├── README.md
├── requirements.txt
├── data/
│ └── sales_data.txt
├── utils/
│ ├── file_handler.py
│ ├── data_processor.py
│ └── api_handler.py
└── output/
└── summary_report.txt


## How to Run
1. Clone the repository
2. Open terminal inside the project folder
3. Run the following command:

```bash
python main.py

Output

Console displays validation summary:

Total records parsed

Invalid records removed

Valid records after cleaning

A summary report is generated in:

output/summary_report.txt

Requirements

Python 3.x

No external libraries required
