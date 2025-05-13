import pandas as pd
from datetime import datetime, timedelta

# Load the Excel file
file_path = '/home/dragon/DATA/Data_CW2.xlsx'
df = pd.read_excel(file_path)

# Function to convert decimal year to datetime
def decimal_year_to_date(decimal_year):
    year = int(decimal_year)
    start = datetime(year, 1, 1)
    end = datetime(year + 1, 1, 1)
    days_in_year = (end - start).days
    fraction = decimal_year - year
    return start + timedelta(days=int(fraction * days_in_year))

# Convert 'sale date' column
df['sale date'] = df['sale date'].apply(decimal_year_to_date)

# Drop rows with any missing values
df.dropna(inplace=True)

# Show the cleaned data
print(df.head())
