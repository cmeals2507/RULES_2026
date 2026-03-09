import pandas as pd

# Replace with the actual Excel output file from survey platform
df = pd.read_excel('survey_data.xlsx')
with open('peaks.txt', 'w') as f:
    f.write(f"Columns: {df.columns.tolist()}\n")
    f.write(f"Row count: {len(df)}\n")
    # Finding rows with files
    for idx, row in df.iterrows():
        files = [val for val in row if isinstance(val, str) and ('.m4a' in val or '.mp3' in val or '.wav' in val)]
        if files:
            f.write(f"Row {idx} files: {files}\n")
            f.write(f"Row {idx} ResponseId: {row.get('ResponseId', 'N/A')}\n")
