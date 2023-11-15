# TP 7 - Machine Learning - Clasificadores

## Random

```R
random_classifier <- function(dataframe) {
  dataframe$predictions_prob <- runif(nrow(dataframe))
  dataframe <- dataframe %>%
    mutate(prediction_class = ifelse(predictions_prob > 0.5, 1, 0))
  return(dataframe)
}
```

| | **Predicted Positive**| **Predicted Negative** | |
|:--:|:--:|:--:|:--:|
|**Actual Positive**| TP = 335 | FN = 355 | Sensitivity = 0.4855072  |
|**Actual Negative**| FP = 2811 | TN = 2882 | Specificity = 0.5062357   |
| | Precision =  0.1064844 | Negative PV = 0.8919004 | Accuracy = 0.503995 |

## Bigger Classs

```R
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
```

| | **Predicted Positive**| **Predicted Negative** | |
|:--:|:--:|:--:|:--:|
|**Actual Positive**| TP = 0 | FN = 690 | Sensitivity = 0 |
|**Actual Negative**| FP = 0 | TN = 5693 | Specificity = 1 |
| | Precision = NaN | Negative PV = 0.8919004 | Accuracy = 0.8919004 |





       