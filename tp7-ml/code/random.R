
library(readr)

file_path <- "/home/aarrieta/Documents/Facultad/Inteligencia Artificial 1/practica/tp7-ml/code/dataset/arbolado-mendoza-dataset-validation.csv"

data_train <-  readr::read_csv(file_path,col_types = cols(
  id = col_integer(),
  especie = col_character(),
  ultima_modificacion = col_character(),
  altura = col_character(),
  circ_tronco_cm = col_double(),
  diametro_tronco = col_character(),
  long = col_double(),
  lat = col_double(),
  seccion = col_integer(),
  nombre_seccion = col_character(),
  area_seccion = col_double()
))

data_train$predictions_prob <- runif(nrow(data_train))


# Load the dplyr package if not already loaded
library(dplyr)

# Define the random_classifier function
random_classifier <- function(dataframe) {
  dataframe <- dataframe %>%
    mutate(prediction_class = ifelse(predictions_prob > 0.5, 1, 0))
  return(dataframe)
}

# Usage:
data_train <- random_classifier(data_train)


# Calculate True Positives (TP)
tp <- data_train %>%
  filter(inclinacion_peligrosa == 1, prediction_class == 1) %>%
  nrow()

# Calculate True Negatives (TN)
tn <- data_train %>%
  filter(inclinacion_peligrosa == 0, prediction_class == 0) %>%
  nrow()

# Calculate False Positives (FP)
fp <- data_train %>%
  filter(inclinacion_peligrosa == 0, prediction_class == 1) %>%
  nrow()

# Calculate False Negatives (FN)
fn <- data_train %>%
  filter(inclinacion_peligrosa == 1, prediction_class == 0) %>%
  nrow()

#  Calculate Accuracy
accuracy <- (tp + tn) / (tp + tn + fp + fn)

# Calculate Precision
precision <- tp / (tp + fp)

# Calculate Recall
recall <- tp / (tp + fn)

# Calculate negative predictive value
npv <- tn / (tn + fn)

# Calculate specifity
specifity <- tn / (tn + fp)

# Display the results
cat("True Positives:  ", tp, "\n")
cat("True Negatives:  ", tn, "\n")
cat("False Positives: ", fp, "\n")
cat("False Negatives: ", fn, "\n")
cat("Accuracy:        ", accuracy, "\n")
cat("Precision:       ", precision, "\n")
cat("Recall:          ", recall, "\n")
cat("Negative PV:     ", npv, "\n")
cat("Specifity:       ", specifity, "\n")




