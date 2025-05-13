import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Load and clean the data
file_path = '/home/dragon/DATA/Data_CW2.xlsx'
df = pd.read_excel(file_path)

# Convert decimal year to datetime
def decimal_year_to_date(decimal_year):
    year = int(decimal_year)
    start = datetime(year, 1, 1)
    end = datetime(year + 1, 1, 1)
    days_in_year = (end - start).days
    fraction = decimal_year - year
    return start + timedelta(days=int(fraction * days_in_year))

df['sale date'] = df['sale date'].apply(decimal_year_to_date)

# Drop missing values
df.dropna(inplace=True)

# Set Seaborn style
sns.set(style="whitegrid")

# 1. Scatter plot: Model age vs Vehicle sale price
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Model age', y='vechicle sale price', data=df)
plt.title('Model Age vs Vehicle Sale Price')
plt.xlabel('Model Age (months)')
plt.ylabel('Sale Price')
plt.tight_layout()
plt.show()

# 2. Scatter plot: Proximity to urban centres vs Vehicle sale price
plt.figure(figsize=(8, 5))
sns.scatterplot(x='proximity to urban centres', y='vechicle sale price', data=df)
plt.title('Proximity to Urban Centres vs Vehicle Sale Price')
plt.xlabel('Distance to Urban Centre')
plt.ylabel('Sale Price')
plt.tight_layout()
plt.show()

# 3. Bar plot: Number of dealerships nearby vs average vehicle sale price
plt.figure(figsize=(8, 5))
sns.barplot(x='number of dealerships nearby', y='vechicle sale price', data=df, estimator='mean', ci=None)
plt.title('Dealerships Nearby vs Average Vehicle Sale Price')
plt.xlabel('Number of Dealerships Nearby')
plt.ylabel('Average Sale Price')
plt.tight_layout()
plt.show()

# 4. Line plot: Sale date vs Vehicle sale price
plt.figure(figsize=(10, 5))
df_sorted = df.sort_values('sale date')
sns.lineplot(x='sale date', y='vechicle sale price', data=df_sorted)
plt.title('Vehicle Sale Price Over Time')
plt.xlabel('Sale Date')
plt.ylabel('Sale Price')
plt.tight_layout()
plt.show()
