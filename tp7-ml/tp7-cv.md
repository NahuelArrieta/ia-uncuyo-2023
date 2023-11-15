# TP 7 - Machine Learning - Cross Validation

## Código
    
```R
create_folds <- function(dataframe, n) {
    ## separate the dataframe in n folds
    folds <- dataframe %>%
        mutate(fold = sample(1:n, nrow(dataframe), replace = TRUE)) %>%
        group_by(fold)
    return(folds)
}

cross_validation <- function(dataframe, n) {
    ## create the folds
    folds <- create_folds(dataframe, n)

    ## Instance the variables
    accuracy_vec <- c()
    precision_vec <- c()
    recall_vec <- c()
    specifity_vec <- c()

    ## iterate over the folds
    for (i in 1:n) {
        ## get the train dataframe
        train <- folds %>%
            filter(fold != i) %>%
            select(-fold) %>%
            ungroup()

        ## get the test dataframe
        test <- folds %>%
            filter(fold == i) %>%
            select(-fold) %>%
            ungroup()

        ## train the model
        model <- rpart(
            formula = inclinacion_peligrosa ~ .,
            data = train,
            method = "class"
        )

        ## predict the test dataframe
        test$prediction_class <- predict(model, newdata = test, type = "class")

        ## calculate the results
        # Calculate True Positives (TP)
        tp <- test %>%
            filter(inclinacion_peligrosa == 1, prediction_class == 1) %>%
            nrow()

        # Calculate True Negatives (TN)
        tn <- test %>%
            filter(inclinacion_peligrosa == 0, prediction_class == 0) %>%
            nrow()

        # Calculate False Positives (FP)
        fp <- test %>%
            filter(inclinacion_peligrosa == 0, prediction_class == 1) %>%
            nrow()

        # Calculate False Negatives (FN)
        fn <- test %>%
            filter(inclinacion_peligrosa == 1, prediction_class == 0) %>%
            nrow()

        #  Calculate Accuracy
        accuracy <- (tp + tn) / (tp + tn + fp + fn)

        # Calculate Precision
        precision <- tp / (tp + fp)

        # Calculate Recall
        recall <- tp / (tp + fn)

        # Calculate specifity
        specifity <- tn / (tn + fp)

        ## append the results only if is a number
        if (!is.nan(accuracy)) {
            accuracy_vec <- c(accuracy_vec, accuracy)
        }
        if (!is.nan(precision)) {
            precision_vec <- c(precision_vec, precision)
        } 
        if (!is.nan(recall)) {
            recall_vec <- c(recall_vec, recall)
        }
        if (!is.nan(specifity)) {
            specifity_vec <- c(specifity_vec, specifity)
        }
    }

    ## calculate the mean of the results
    accuracy <- mean(accuracy_vec)
    precision <- mean(precision_vec)
    recall <- mean(recall_vec)
    specifity <- mean(specifity_vec)

    ## calcualte de sd
    accuracy_sd <- sd(accuracy_vec)
    precision_sd <- sd(precision_vec)
    recall_sd <- sd(recall_vec)
    specifity_sd <- sd(specifity_vec)

    ## print the means and the sd
    cat("Accuracy:  ", accuracy, " ± ", accuracy_sd, "\n")
    cat("Precision: ", precision, " ± ", precision_sd, "\n")
    cat("Recall:    ", recall, " ± ", recall_sd, "\n")
    cat("Specifity: ", specifity, " ± ", specifity_sd, "\n")

}
```

## Resultados
- Accuracy:   0.886777  ±  0.009340104 
- Precision:  NA  ±  NA 
- Recall:     0  ±  0 
- Specifity:  1  ±  0 