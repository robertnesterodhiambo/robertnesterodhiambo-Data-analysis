# Load necessary libraries
library(gutenbergr)
library(tidytext)
library(dplyr)
library(wordcloud)
library(RColorBrewer)
library(stringi)
library(shiny)

# Define UI for application
ui <- fluidPage(
  
  # Application title
  titlePanel("Text Analysis and Word Cloud"),
  
  # Sidebar with inputs
  sidebarLayout(
    sidebarPanel(
      radioButtons("book_type", "Select Book:",
                   choices = c("Jane Austen" = "Jane Austen", 
                               "Gutenberg - State of the Union Addresses" = "Gutenberg")),
      uiOutput("author_selection"),
      actionButton("analyze", "Analyze Text")
    ),
    
    # Main panel to show outputs
    mainPanel(
      plotOutput("wordcloud")
    )
  )
)

# Define server logic
server <- function(input, output, session) {
  
  # Dynamically render author selection based on user's choice
  observe({
    if (input$book_type == "Gutenberg") {
      books <- gutenberg_works(title == "State of the Union Addresses")
      authors <- unique(books$author)
      output$author_selection <- renderUI({
        selectInput("gutenberg_authors", "Choose Authors:", choices = authors, multiple = TRUE)
      })
    } else {
      output$author_selection <- renderUI({
        NULL
      })
    }
  })
  
  text_data <- eventReactive(input$analyze, {
    if (input$book_type == "Gutenberg") {
      selected_books <- gutenberg_works(author %in% input$gutenberg_authors)
      book_ids <- selected_books$gutenberg_id
      text <- gutenberg_download(book_ids)
      text <- text %>%
        left_join(selected_books, by = "gutenberg_id") %>%
        select(gutenberg_id, text, title, author)
    } else {
      text <- data.frame(text = prideprejudice, 
                         title = "Pride and Prejudice", 
                         author = "Jane Austen",
                         stringsAsFactors = FALSE)
    }
    
    # Remove punctuation and convert to a tidy format
    text$text <- stri_replace_all_regex(text$text, "[[:punct:]]", "")
    tidy_text <- text %>%
      unnest_tokens(word, text) %>%
      anti_join(stop_words)
    
    # Get word count
    word_count <- tidy_text %>%
      count(title, author, word, sort = TRUE)
    
    word_count
  })
  
  output$wordcloud <- renderPlot({
    word_count <- text_data()
    
    if (nrow(word_count) > 0) {
      # Create a palette of colors for authors
      author_colors <- RColorBrewer::brewer.pal(length(unique(word_count$author)), "Set3")
      names(author_colors) <- unique(word_count$author)
      
      # Define a function to assign colors based on authors
      assign_colors <- function(author) {
        author_colors[author]
      }
      
      # Create word cloud
      with(word_count, wordcloud(word, n, scale = c(3, 0.5), colors = assign_colors(author), 
                                 random.order = FALSE, max.words = 100))
    }
  })
}

# Run the application 
shinyApp(ui = ui, server = server)
