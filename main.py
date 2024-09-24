from data_loader import load_json_data
from data_processor import process_data
from excel_exporter import save_to_excel
from process_descriptor import upload_description


def main():
      input_file = './example_file.json'
      output_file = './processed_data.xlsx'
      
      #Specify the columns and their nested fields for de-duplication
      dedup_columns = ['@timestamp', 'agent','application']
      fields_names = ['name']

      json_data = load_json_data(input_file)
      raw_data, deduplicated_data, severity_data, aggregated_data = process_data(json_data, dedup_columns, fields_names)
      save_to_excel(raw_data, deduplicated_data, severity_data, aggregated_data, output_file)
      upload_description(output_file)

if __name__ == '__main__':
      main()
