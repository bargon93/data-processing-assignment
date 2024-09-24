import pandas as pd

def upload_description(output_file):
      descriptions = pd.DataFrame({
            'Step': ['Load the data', 'Raw Data', 'Unique Data', 'Aggregated Data', 'Save to output file'],
            'Description': [
                  'Calling the load_json_data function with the data file path. In the function, split the file to json objects, Then load and return the list of dictionaries of the json objects using json.loads',
                  'Creating a DataFrame using the uploaded data',
                  'Using the create_unique_key function, creating a new column in the raw data wich contain a string key combined of the given key_columns values calles unique_key. Then using the drop_duclicates() function, creating a new DataFrame for unique data without the duplicates',
                  'Using a loop to itirate the rows of the raw data, grouping the rows by their severity type by using a dictionaries list, where each row is appended to its severity index. Then initialize two epmty dictionaries, one for the entire data devided by their seveirties and one for the aggregated data. Then using the data from the severity groups object, creating DataFrames for each severity and a DataFrame for analysing the data',
                  'In the called save_to_excel functio, using the pandas.ExcelWriter to write a new outputfile, where all the DataFrames are uploaded using the to_excel function'                  
            ]
      })
      descriptions.reset_index(drop=True, inplace=True)
      descriptions.index += 1
      descriptions.index.name = 'Step number'
      with pd.ExcelWriter(output_file, mode='a', engine='openpyxl') as writer:
            descriptions.to_excel(writer, sheet_name='Descriptions')
