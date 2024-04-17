library(readr)
grocery <- read_csv("~/Downloads/GroceryDataSet.csv")
View(grocery)

# summary 

summary(grocery)

##

library(tibble)
install.packages("tidyverse")
install.packages("textshaping")
library(tidyverse)
grocery_frequency <- tibble(Items = names(itemFrequency(grocery)),
                            Frequency = itemFrequency(grocery))
head(grocery_frequency)
