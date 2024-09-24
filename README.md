# Data Processing Assignment

This project processes JSON log data from developer's scanner logs, creating three data layers: raw data, deduplicated data, and aggregated data. The processed data is then saved to an Excel file for analysis.

## Assignment Requirements

- Given a representing data file from the developer's scanner logs, the data should by represented in 3 different layers according to the following rules:
  1. Raw data layer:
     - No data loss
     - Every log is a different row in the table
     - The data kept in its original form
  2. De-duplicated data, which will be unique for eact row based on:
     - @timestamp
     - agent
     - application
  3. Aggregate data and divided to different tables by process.severity
- The program should create an excel file with the 3 different data layers

## Features

- Loads and parses JSON log data
- Creates three data layers:
  1. Raw data layer (no data loss)
  2. Unique data layer (deduplicated)
  3. Aggregated data layer (divided by severity)
- Saves processed data to an Excel file with multiple sheets
- Includes a description sheet explaining the processing steps

## Requirements

- Python3
- pandas
- openpyxl

## Project Structure

- `main.py`: The entry point of the application
- `data_loader.py`: Contains functions for loading JSON data
- `data_processor.py`: Handles data processing and transformation
- `excel_exporter.py`: Manages exporting data to Excel
- `process_descriptor.py`: Generates process description for the Excel output

## Installation

1. Clone this repository:

```bash
git clone https://github.com/bargon93/data-processing-assignment.git
cd data-processing-assignment
```

2. Install the required packages:

```bash
pip install pandas openpyxl
```

## Usage

1. Place your input JSON file in the project directory and name it `example_file.json`.

2. Run the script:

```bash
python3 main.py
```

3. The processed data will be saved in `processed_data.xlsx` in the same directory.

## Docker Support

This project includes a Dockerfile for containerization. To build and run the Docker container:

1. Build the Docker image:

```bash
docker build -t data-processing-assignment .
```

2. Run the Docker container:

```bash
docker run -v $(pwd):/app data-processing-assignment
```

This will process the `example_file.json` in the current directory and output `processed_data.xlsx` in the same location.

## Contributing

Feel free to fork this project and submit pull requests with any improvements or bug fixes.