#  Instructions

## Hide

Input files: OHS HC Template_v1.1.xlsx &amp; NTE REPORT - 4.17.24.xslx. These two workbooks need to be read into via Python and used to create the output outlined in the output template.

Output file template: OHS_Template_WithNoData.xlsx. This is the structure the output of the code should be. Row 1 is the header in each spreadsheet, Row 2 shows where from the input files the data is coming from and any transformation (if any) required.

The output file template is annotated with what data needs to be pulled from which file and transformed. Most of the data will come from the OHS HC Template, and some are annotated to show that it comes from the NTE Report. All transformations required are outlined in the output file template.

The most complex sheet is Vacancy data which will be using the times outlined in the Vacancy Stage Timeline sheet to determine how many days is required for each stage


##  Changes to be made
Vacancy sheet: missing columns A - D
2. Vacancy sheet: Column Q - AV are incorrect column names (duplicate columns from steps 1-17 and there shouldn’t bet be a step 18 as reflected in columns AW and AX.)
3. Vacancy sheet: columns after the 17 steps are also mislabeled and in a different order from the template. Some columns and calculations are missing i.e. Amount Exceeding Total Process


4. Employee Data sheet: column J mislabeled - should just be email address and column N email address is repeated.
5. Employee Data sheet: employee location city : national capital region is not getting translated to District of Columbia
6. Employee Data sheet: Column for Veteran Preference Code missing from NFC data (should be before Security Clearance)
7. Employee Data sheet: Employee Type column missing before the Notes column
8. Make sure sheet names are the same as the template