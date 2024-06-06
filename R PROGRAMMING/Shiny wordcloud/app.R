# Load necessary libraries
library(shiny)
library(tm)
library(wordcloud2)
library(shinyWidgets)


# Define UI
ui <- fluidPage(
  # Application title
  titlePanel("Word Cloud"),
  
  sidebarLayout(
    # Sidebar with radio buttons for word source selection
    sidebarPanel(
      radioButtons("source", "Word source:",
                   choices = c("Pride and Prejudice", "State of the Union Address")),
      hr(),
      numericInput("num", "Number of words ( min: 3 ):", value = 3, min = 3),
      hr()
    ),
    # Show Word Cloud
    mainPanel(
      wordcloud2Output("cloud")
    )
  )
)

# Define server logic
server <- function(input, output) {
  # Define reactive value for the selected data source
  data_source <- reactive({
    if (input$source == "Pride and Prejudice") {
      readLines("pride.txt")
    } else if (input$source == "State of the Union Address") {
      readLines("state.txt")
    }
  })
  
  # Create word cloud function
  create_wordcloud <- function(data, num_words) {
    if (is.null(data)) return("Error: No data available.")
    
    corpus <- Corpus(VectorSource(data))
    corpus <- tm_map(corpus, tolower)
    corpus <- tm_map(corpus, removePunctuation)
    corpus <- tm_map(corpus, removeNumbers)
    corpus <- tm_map(corpus, removeWords, stopwords("english"))
    
    tdm <- as.matrix(TermDocumentMatrix(corpus))
    word_freq <- sort(rowSums(tdm), decreasing = TRUE)
    word_freq <- data.frame(word = names(word_freq), freq = as.numeric(word_freq))
    
    # Make sure a proper num_words is provided
    num_words <- max(num_words, 3)
    
    # Grab the top n most common words
    word_freq <- head(word_freq, n = num_words)
    
    wordcloud2(word_freq)
  }
  
  # Render the word cloud
  output$cloud <- renderWordcloud2({
    create_wordcloud(data_source(), input$num)
  })
}

# Run the application
shinyApp(ui = ui, server = server)
