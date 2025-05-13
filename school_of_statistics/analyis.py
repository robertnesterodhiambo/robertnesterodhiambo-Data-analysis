import pandas as pd

# Load the Excel file
file_path = '/home/dragon/DATA/Data_CW2.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Display the first few rows
print(df.head())
