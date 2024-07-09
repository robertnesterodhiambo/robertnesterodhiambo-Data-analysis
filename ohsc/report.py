import pandas as pd

# Define the file paths
file_path_ohs = '/home/dragon/Git/Data/ohs-hc-template_v11.xlsx'
file_path_nte = '/home/dragon/Git/Data/nte-report-41724.xlsx'

# Read the sheet names from the OHS HC Template file
ohs_sheet_names = pd.ExcelFile(file_path_ohs, engine='openpyxl').sheet_names

# Create a dictionary to store the dataframes
ohs_dfs = {}

# Read each sheet into a separate dataframe
for sheet_name in ohs_sheet_names:
    ohs_dfs[sheet_name] = pd.read_excel(file_path_ohs, sheet_name=sheet_name, engine='openpyxl')

# Read the NTE REPORT file starting from the second row
nte_df = pd.read_excel(file_path_nte, skiprows=1, engine='openpyxl')

# Display the sheet names
print("OHS HC Template Sheet Names:")
print(ohs_sheet_names)

# Display the first few rows of each dataframe from the OHS HC Template file
print("\nOHS HC Template DataFrames:")
for sheet_name, df in ohs_dfs.items():
    print(f"\nSheet name: {sheet_name}")
    print(df.head())

# Display the first few rows of the NTE REPORT dataframe
print("\nNTE REPORT DataFrame:")
print(nte_df.head())
