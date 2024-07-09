#  Instructions

## Hide
Input files: OHS HC Template_v1.1.xlsx &amp; NTE REPORT - 4.17.24.xslx. These two workbooks need to be read into via Python and used to create the output outlined in the output template.

Output file template: OHS_Template_WithNoData.xlsx. This is the structure the output of the code should be. Row 1 is the header in each spreadsheet, Row 2 shows where from the input files the data is coming from and any transformation (if any) required.

The output file template is annotated with what data needs to be pulled from which file and transformed. Most of the data will come from the OHS HC Template, and some are annotated to show that it comes from the NTE Report. All transformations required are outlined in the output file template.

The most complex sheet is Vacancy data which will be using the times outlined in the Vacancy Stage Timeline sheet to determine how many days is required for each stage
