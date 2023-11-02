## print results
print_result <- function(dataframe) {
    # Calculate True Positives (TP)
    tp <- dataframe %>%
    filter(inclinacion_peligrosa == 1, prediction_class == 1) %>%
    nrow()

    # Calculate True Negatives (TN)
    tn <- dataframe %>%
    filter(inclinacion_peligrosa == 0, prediction_class == 0) %>%
    nrow()

    # Calculate False Positives (FP)
    fp <- dataframe %>%
    filter(inclinacion_peligrosa == 0, prediction_class == 1) %>%
    nrow()

    # Calculate False Negatives (FN)
    fn <- dataframe %>%
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
}