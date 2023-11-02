
library(dplyr)




# Define the bigger_class function
bigger_class <- function(dataframe) {
   # get the number of rows of the dataframe
    n <- nrow(dataframe)
    # get the number of rows of the dataframe where inclinacion_peligrosa is 1
    n1 <- nrow(dataframe %>% filter(inclinacion_peligrosa == 1))
    # get the number of rows of the dataframe where inclinacion_peligrosa is 0
    n0 <- nrow(dataframe %>% filter(inclinacion_peligrosa == 0))
    # if n1 is bigger than n0, set the prediction_class to 1, otherwise set it to 0
    dataframe <- dataframe %>%
      mutate(prediction_class = ifelse(n1 > n0, 1, 0))
}

# Usage:
data_test <- get_test_dataframe()
data_test <- bigger_class(data_test)


## print results
print_result(data_test)


