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
