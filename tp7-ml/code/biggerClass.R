
library(readr)
library(dplyr)

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
data_train <- bigger_class(data_train)


## print results
print_result(data_train)


