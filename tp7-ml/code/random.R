
library(dplyr)



# Define the random_classifier function
random_classifier <- function(dataframe) {
  dataframe$predictions_prob <- runif(nrow(dataframe))
  dataframe <- dataframe %>%
    mutate(prediction_class = ifelse(predictions_prob > 0.5, 1, 0))
  return(dataframe)
}

# Usage:
data_test <- get_validation_dataframe()
data_test <- random_classifier(data_test)


## print results
print_result(data_test)





