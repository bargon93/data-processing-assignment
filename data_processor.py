from collections import defaultdict
import pandas as pd

def create_unique_key(row, key_columns, nested_fields):
      return '_'.join(str(row[col]) if isinstance(row[col], (str, int, float)) 
                    else str(row[col].get(field, '')) for col in key_columns for field in nested_fields if isinstance(row[col], dict))
    

def process_data(json_data, dedup_columns, nested_fields):
      #Raw data
      raw_data = pd.DataFrame(json_data)
      
      #Deduplicated data
      raw_data['unique_key'] = raw_data.apply(lambda row: create_unique_key(row, dedup_columns, nested_fields), axis=1)
      deduplicate_data = raw_data.drop_duplicates(subset='unique_key').drop(columns=['unique_key'])

      #Group the data by severity
      severity_groups = defaultdict(list)
      for _, row in raw_data.drop(columns=['unique_key']).iterrows():
            severity = row['processed']['Severity']
            severity_groups[severity].append(row.to_dict())
      
      severity_data = {}
      aggregated_data = {}
      for severity, data in severity_groups.items():
            df = pd.DataFrame(data)
            severity_data[severity] = df
            aggregated_data[severity] = {
                  'count': len(df),
                  'unique_applications': df['application'].nunique(),
                  'unique_agents': df['agent'].apply(lambda agent: agent['name']).nunique(),
                  'unique_sources': df['processed'].apply(lambda processed: processed.get('Source', '')).nunique(),
                  'earliest_timestamp' : df['@timestamp'].min(),
                  'latest_timestamp': df['@timestamp'].max()
            }
            

      return raw_data.drop(columns=['unique_key']), deduplicate_data, severity_data, aggregated_data