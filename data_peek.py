import pandas as pd
import sys

# Replace with the actual Excel output file from survey platform
excel_path = 'survey_data.xlsx' 
try:
    df = pd.read_excel(excel_path)
    print("Columns:", df.columns.tolist())
    print("Row count:", len(df))
    # Find rows with an audio file attached (non-null in the relevant columns)
    # Print the head to understand what columns exist
    print(df.head(2).to_dict('records'))
except Exception as e:
    print(f"Error reading excel: {e}")
    sys.exit(1)
