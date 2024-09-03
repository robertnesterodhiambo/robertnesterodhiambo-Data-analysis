## importing data into R
library(readr)


stock <- read_csv("GIT/Data/stock_details_5_years.csv")
colnames(stock)

library(dplyr)

stock.list <-  stock  %>%
  distinct(Company)

stock.list

library(quantmod)

stock_symbols <- stock.list$Company

stock_data_list <- list()

#stock_data <- getSymbols(stock.list$Company, src = "yahoo", from = "2023-12-12", to = "2024-01-01", auto.assign = FALSE)
#stock_data
# Loop through each symbol and download the data
for(symbol in stock_symbols) {
  tryCatch({
    # Download stock data for the current symbol
    stock_data <- getSymbols(symbol, src = "yahoo", from = "2023-12-12", to = "2024-01-01", auto.assign = FALSE)
    
    # Convert the xts object to a data frame
    stock_df <- data.frame(Date = index(stock_data), coredata(stock_data))
    
    # Add a column for the stock symbol
    stock_df$Symbol <- symbol
    
    # Append the data frame to the list
    stock_data_list[[symbol]] <- stock_df
  }, error = function(e) {
    message(paste("Error downloading data for", symbol, ":", e$message))
  })
}


###########################33
# Define the common column names
common_colnames <- c("Date", "Open", "High", "Low", "Close", "Volume", "Adjusted", "Symbol")

# Function to rename columns to the common names
rename_columns <- function(df) {
  # If the data frame has the correct number of columns, rename them
  if (ncol(df) == length(common_colnames)) {
    colnames(df) <- common_colnames
  }
  return(df)
}

# Apply the renaming function to each data frame in the list
renamed_df_list <- lapply(stock_data_list, rename_columns)
combined_df <- bind_rows(renamed_df_list)
head(combined_df)
View(combined_df)
write.csv(combined_df,"sample.csv")
getwd()
##########################333
