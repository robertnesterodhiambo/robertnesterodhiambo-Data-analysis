// question 1

// Set the working directory
cd "C:\Users\ROBERT\3D Objects\git hub\robertnesterodhiambo-Data-analysis"

// Start logging to aaa9985_hw1.txt
log using aaa9985_hw1.txt, replace

// question 2

// Housekeeping commands
clear all
capture log close
cd "C:\Users\ROBERT\3D Objects\git hub\robertnesterodhiambo-Data-analysis"
log using aaa9985_hw1.txt, replace

// Load Excel dataset into Stata
import excel "WorldBankData.xlsx", firstrow



// question 3

// Explanation of housekeeping commands:

// 1. clear all: 
//    Clears all data from memory in Stata. Removes any existing datasets, macros, and other objects.
//    Ensures a clean slate for starting analysis to avoid conflicts or issues from previous data or commands.



// 2. capture log close:
//    Closes any open log files in Stata. The "capture" keyword suppresses error messages if no log file is open.
//    Important before starting a new logging session to prevent appending to existing logs or overwriting them unintentionally.



// 3. cd:
//    Changes the current directory in Stata to the specified directory.
//    Sets the working directory where data and do-file are located, ensuring Stata knows where to find files for reading and writing.


// 4. log using:
//    Starts logging Stata output to a file. The "using" option specifies the filename for the log file,
//    and "replace" overwrites any existing log file with the same name.
//    Logging is useful for keeping track of commands executed, results obtained, and any errors encountered during analysis.



// 5. import excel:
//    Imports data from an Excel file into Stata. Reads data from the specified Excel file and creates a Stata dataset.
//    The "firstrow" option indicates that the first row of the Excel file contains variable names.


// question 4
// Rename variables using wildcards
rename *Laborforce* flfp
rename *GDPgrowth* GDPgr
rename *GDPpercap* GDPpc
rename GDPPPPconstant2017internat GDP
rename *Manufactur* ManufVA

//// Drop the TimeCode variable
drop TimeCode

// question 5

// Convert the dataset to Stata format and save it
save "aaa9985_hw1.dta", replace

// Message confirming the save
di "Dataset saved as WorldBankData.dta in the working directory."

// ii
// Load dataset from Stata format
use "aaa9985_hw1.dta", clear

// question 6

// (i) How many observations are in the dataset?
local obs_count = _N
di "Number of observations: `obs_count'"

// (ii) What is the unique identifier for this data?
ds, has(type numeric)
di "Unique identifier: " `r(varlist)'

// (iii) How many variables are there in the data?

local var_count = _N
di "Number of variables: `var_count'"

// (iv) How many string variables? Are all of these string variables categorical? Discuss.
// Count the number of string variables
local str_count = 0
foreach var of varlist _all {
    if strpos("`: variable label `var''", "str") > 0 {
        local ++str_count
    }
}
di "Number of string variables: `str_count'"

// question 8

//i
 // Check for missing observations in the GDP variable
summarize GDP, detail

//ii
// List countries with missing GDP values
list CountryName if missing(GDP)

// QUESTION 9
//  i )Calculate average and standard deviation of female labor force participation
summarize flfp, meanonly

// Calculate standard deviation of female labor force participation
summarize flfp
scalar sd_flfp = r(sd)

// Display mean and standard deviation of female labor force participation
di "Mean of female labor force participation: " r(mean)
di "Standard deviation of female labor force participation: " scalar(sd_flfp)

// ii)Calculate median GDP per capita
summarize GDPpc, detail


// Calculate average and standard deviation of female labor force participation
// for countries with GDP per capita below the median
summarize flfp if GDPpc < r(p50), meanonly

// Calculate average and standard deviation of female labor force participation
// for countries with GDP per capita above the median
summarize flfp if GDPpc > r(p50), meanonly

// iii)
// Calculate the median GDP per capita
summarize GDPpc, detail
scalar median_GDPpc = r(p50)

// Create a new variable indicating GDP per capita below or above the median
gen GDPpc_below_median = (GDPpc < median_GDPpc)
gen GDPpc_above_median = (GDPpc > median_GDPpc)

// Calculate average and standard deviation of female labor force participation
// for countries with GDP per capita below the median
summarize flfp if GDPpc_below_median
di "Average flfp for countries with GDP per capita below the median: " r(mean)
di "Standard deviation of flfp for countries with GDP per capita below the median: " r(sd)

// Calculate average and standard deviation of female labor force participation
// for countries with GDP per capita above the median
summarize flfp if GDPpc_above_median
di "Average flfp for countries with GDP per capita above the median: " r(mean)
di "Standard deviation of flfp for countries with GDP per capita above the median: " r(sd)

// question 10

//i 
// Draw histogram of female labor force participation
histogram flfp, title("Histogram of Female Labour Force Participation") saving(hist_flfp.png, replace)

// ii)
// Scatter plot of female labor force participation against manufacturing value added
scatter flfp ManufVA, title("Scatter Plot of Female Labour Force Participation vs Manufacturing Value Added") saving(scatter_flfp_ManufVA.png, replace)
//iii)
// Calculate the correlation coefficient between female labor force participation and manufacturing value added
pwcorr flfp ManufVA






