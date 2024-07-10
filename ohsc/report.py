import pandas as pd

# Define the file paths
file_path_ohs = '/home/dragon/Git/Data/ohs-hc-template_v11.xlsx'
file_path_nte = '/home/dragon/Git/Data/nte-report-41724.xlsx'

# Read the specific sheet from the OHS HC Template file
positions_df = pd.read_excel(file_path_ohs, sheet_name='Positions Data Template', engine='openpyxl')

# Clean up column names by stripping any leading/trailing whitespace or newline characters
positions_df.columns = positions_df.columns.str.strip().str.replace('\n', '')

# Read the NTE REPORT file starting from the second row
nte_df = pd.read_excel(file_path_nte, skiprows=1, engine='openpyxl')

# Create a new DataFrame with specific columns from positions_df
position = positions_df[[
    'OHS PIN', 'FY Position Authorization', 'Supervisor PIN',
    'Directorate/Unit', 'Division', 'Branch/Program', 'Position Type',
    'Encumbered Position', 'Position Status', 'Employee Status',
    'Employee ID', 'Employee Name', 'Preferred Name', 'Position Title',
    'Position Description Title', 'Pay Plan', 'Minimum Grade',
    'Maximum Grade', 'Career Ladder Position','Hiring Type','Lapse in Appropriations Status',
    'Official Workplace Flexibility (Position)', 'Position Clearance','Position DOE Clearance', 'Notes'
]].copy()



# Add a new column 'Supervisor Role'       
position['Supervisor Role'] = position['OHS PIN'].map(position['Supervisor PIN'].value_counts())

# Fill NaN values with 0
position['Supervisor Role'].fillna(0, inplace=True)

# Rearrange columns so 'Supervisor Role' comes immediately after 'Supervisor PIN'                


# Function to check if Pay Plan is within position grade range
def check_grade_range(row):
    try:
        pay_plan = float(row['Pay Plan'])
        min_grade = float(row['Minimum Grade'])
        max_grade = float(row['Maximum Grade'])
        
        if pay_plan >= min_grade and pay_plan <= max_grade:
            return 'Within Position Grade Range'
        else:
            return 'Outside of Position Grade Range'
    except ValueError:
        return 'Error: Non-numeric value'


# Apply the function to create a new column 'Grade Range Status'
position['Grade Range Status'] = position.apply(check_grade_range, axis=1)

position = position[['OHS PIN', 'FY Position Authorization', 'Supervisor PIN','Supervisor Role',
                     'Directorate/Unit', 'Division', 'Branch/Program', 'Position Type',
                     'Encumbered Position', 'Position Status', 'Employee Status',
                     'Employee ID', 'Employee Name', 'Preferred Name', 'Position Title',
                     'Position Description Title', 'Pay Plan', 'Minimum Grade',
                     'Maximum Grade', 'Career Ladder Position','Grade Range Status','Hiring Type',
                     'Lapse in Appropriations Status','Official Workplace Flexibility (Position)', 
                     'Position Clearance','Position DOE Clearance', 'Notes'
                     ]]

# Set pandas options to display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# Display the new DataFrame
print("Position DataFrame with rearranged columns and Supervisor Role:")
position


import pandas as pd
import numpy as np
from datetime import datetime

# Define the file path for the OHS HC Template
file_path_ohs = '/home/dragon/Git/Data/ohs-hc-template_v11.xlsx'

# Read the 'Vacancy Data' sheet from the Excel file
vacancy_df = pd.read_excel(file_path_ohs, sheet_name='Vacancy Data', engine='openpyxl')

# Extract specific columns from vacancy_df
columns_to_add = [
    'Hire Manager', 'HC Servicing Specialists', 'FedHR Navigation Number', 
    'Nature of Action', 'Current Status', 'Action Owner', 'USA Jobs', 
    '1. PND PRF Submission', '2. PRF Approved', '3. Budget Certification Complete', 
    '4. Recruitment Request Submitted to OCHCO', '5. PD Classification Complete', 
    '6. Recruitment Package Routed to HRMS Staffing POC', '7. Draft Job Analysis Received', 
    '8. Job Analysis Returned', '9. Draft Vacancy Announcement Documents Received', 
    '10. Vacancy Announcement Documents Returned', '11. Vacancy Announcement Open', 
    '12. Vacancy Announcement Closed', '13. Certificate Issued', '14. Certificate Returned', 
    '15. TJO Issued', '16. Security', '17. FJO Issued', '18. EOD Set or Cancellation Date', 
    'EOD Set or Cancellation', 'Certificate Expiration Date','Honorific Title', 'Selectee Legal Last Name',
    'Selectee Legal First Name', 'Suffix', 'Notes'
]

# Select only the required columns from vacancy_df
additional_data = vacancy_df[columns_to_add].copy()

# Concatenate vacancy_df and additional_data horizontally (side by side)
vacancy = pd.concat([vacancy_df, additional_data], axis=1)

# Convert 'Vacant Date' to datetime format
vacancy['Vacant Date'] = pd.to_datetime(vacancy['Vacant Date'], errors='coerce')

# Calculate 'Length of Vacancy (Days)'
vacancy['Length of Vacancy (Days)'] = (datetime.now() - vacancy['Vacant Date']).dt.days

# Extract columns of interest for date calculation
date_columns = vacancy.columns[vacancy.columns.str.startswith('1.') & vacancy.columns.str.endswith('Date')]

# Convert date columns to datetime format
vacancy[date_columns] = vacancy[date_columns].apply(pd.to_datetime, errors='coerce')

# Find the furthest date recorded to the right
vacancy['LastDate'] = vacancy[date_columns].max(axis=1)

# Calculate the number of workdays between 'LastDate' and today's date, excluding weekends
valid_dates = vacancy['LastDate'].notna()
vacancy.loc[valid_dates, 'Days in Stage'] = np.busday_count(vacancy.loc[valid_dates, 'LastDate'].values.astype('datetime64[D]'), np.datetime64('today'))

vacancy = vacancy[[
    'Hire Manager', 'HC Servicing Specialists', 'FedHR Navigation Number', 
    'Nature of Action', 'Current Status', 'Action Owner', 'USA Jobs', 
    '1. PND PRF Submission', '2. PRF Approved', '3. Budget Certification Complete', 
    '4. Recruitment Request Submitted to OCHCO', '5. PD Classification Complete', 
    '6. Recruitment Package Routed to HRMS Staffing POC', '7. Draft Job Analysis Received', 
    '8. Job Analysis Returned', '9. Draft Vacancy Announcement Documents Received', 
    '10. Vacancy Announcement Documents Returned', '11. Vacancy Announcement Open', 
    '12. Vacancy Announcement Closed', '13. Certificate Issued', '14. Certificate Returned', 
    '15. TJO Issued', '16. Security', '17. FJO Issued', '18. EOD Set or Cancellation Date', 
    'EOD Set or Cancellation', 'Certificate Expiration Date','Vacant Date', 'Length of Vacancy (Days)',
    'LastDate','Days in Stage','Honorific Title', 'Selectee Legal Last Name','Selectee Legal First Name', 
    'Suffix', 'Notes'
]]

# Display the updated DataFrame with the new columns
vacancy.head()
