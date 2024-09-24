import pandas as pd

def save_to_excel(raw_data, deduplicated_data, severity_data, aggregated_data, output_file):
      with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            raw_data.to_excel(writer, sheet_name='Raw Data', index=False)
            deduplicated_data.to_excel(writer, sheet_name='Unique Data', index=False)

            for severity, df in severity_data.items():
                  df.to_excel(writer, sheet_name=f'Severity_{severity}', index=False)

            agg_df = pd.DataFrame(aggregated_data).T
            agg_df.index.name = 'Severity'
            agg_df.to_excel(writer, sheet_name='Aggregated Data')
      
