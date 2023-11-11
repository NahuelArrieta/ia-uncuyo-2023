library(dplyr)
library(randomForest)


## Mke undersampling of falses
undersampling <- function(dataframe) {

    # get the number of rows of the dataframe where inclinacion_peligrosa is 1
    n1 <- nrow(dataframe %>% filter(inclinacion_peligrosa == 1))
    # get the number of rows of the dataframe where inclinacion_peligrosa is 0
    n0 <- nrow(dataframe %>% filter(inclinacion_peligrosa == 0))

    ## set min to the minimum of n1 and n0
    min <- min(n1, n0)

    ## Make undersampling of falses
    dataframe <- dataframe %>%
        filter(inclinacion_peligrosa == 0) %>%
        sample_n(min) %>%
        bind_rows(dataframe %>% filter(inclinacion_peligrosa == 1))

    return(dataframe)
}


## Set 'altura' to a number
## Muy bajo (1 - 2 mts) -> 1.5
## Bajo (2 - 4 mts) -> 3
## Medio (4 - 8 mts) -> 6
## Alto (> 8 mts) -> 10
modifyHigh <- function(dataframe) {
    dataframe <- dataframe %>%
        mutate(altura = ifelse(altura == "Muy bajo (1 - 2 mts)", 1.5, altura)) %>%
        mutate(altura = ifelse(altura == "Bajo (2 - 4 mts)", 3, altura)) %>%
        mutate(altura = ifelse(altura == "Medio (4 - 8 mts)", 6, altura)) %>%
        mutate(altura = ifelse(altura == "Alto (> 8 mts)", 10, altura))

    return(dataframe)
}

## Set 'diametro_tronco' to a number
## Chico -> 0
## Mediano -> 1
## Grande -> 2
modifyDiam <- function(dataframe) {
    dataframe <- dataframe %>%
        mutate(diametro_tronco = ifelse(diametro_tronco == "Chico", 0, diametro_tronco)) %>%
        mutate(diametro_tronco = ifelse(diametro_tronco == "Mediano", 1, diametro_tronco)) %>%
        mutate(diametro_tronco = ifelse(diametro_tronco == "Grande", 2, diametro_tronco))

    return(dataframe)
}

## remove 'seccion'
removeSeccion <- function(dataframe) {
    dataframe <- dataframe %>%
        select(-seccion)
    
    return(dataframe)
}

preprocess <- function(dataframe) {
    dataframe <- modifyHigh(dataframe)
    dataframe <- modifyDiam(dataframe)
    dataframe <- removeSeccion(dataframe)

    return(dataframe)
}

## train the model with random forest
train_model <- function(dataframe, ntree, mtry) {
    ## train the model
    model <- randomForest(
        formula = inclinacion_peligrosa ~ .,
        data = dataframe,
        ntree = ntree,
        mtry = mtry
    )

    return(model)
}

## test the model
test <- function(model) {
    ## get validation dataframe
    test_dataframe <- get_validation_dataframe()
    test_dataframe <- preprocess(test_dataframe)

    ## predict the test dataframe
    test_dataframe$prediction_class <- predict(model, newdata = test_dataframe, type = "class")

    ## mutate to discrete values
    test_dataframe <- test_dataframe %>%
        mutate(prediction_class = ifelse(prediction_class > 0.5, 1, 0))

    return(test_dataframe)
}

## Make csv for kaggle submission
make_csv <- function(dataframe) {



    dataframe <- dataframe %>%
        select(id, prediction_class) %>%
        rename("inclinacion_peligrosa" = "prediction_class")

    write.csv(dataframe, file = "submission.csv", row.names = FALSE)
}


## Preprocess data
data_train <- get_train_dataframe()
data_train <- undersampling(data_train)
data_train <- preprocess(data_train)


## Train model
model <- train_model(data_train, 100, 3)


## Test model
val_data <- test(model)
print_result(val_data)

## Make csv
test_dataframe <- get_test_dataframe()
test_dataframe <- preprocess(test_dataframe)
test_dataframe$prediction_class <- predict(model, newdata = test_dataframe, type = "class")
## mutate to discrete values
test_dataframe <- test_dataframe %>%
    mutate(prediction_class = ifelse(prediction_class > 0.5, 1, 0))
make_csv(test_dataframe)
    




