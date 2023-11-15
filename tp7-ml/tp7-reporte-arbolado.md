# TP 7 - Machine Learning - Reporte arbolado

## Descripción del proceso de preprocesamiento
Las acciones de preparación de los datos fueron las siguientes:
- Se eliminó la variable sección ya que no aportaba información relevante para el análisis porque estaba relacionada con nombre_seccion.
- Se modifico la variable altura de [muy bajo, bajo, medio, alto] a [1.5, 3, 6, 10] para tener una variable numérica.
- Se modifico la variable diametro de [chico, mediano, grande] a [0, 1, 2] para tener una variable numérica.


## Resultados obtenidos sobre el conjunto de validación
Se obtuvieron la siguiente matriz de confusion para la validación:

| | **Predicted Positive**| **Predicted Negative** | |
|:--:|:--:|:--:|:--:|
|**Actual Positive**| TP = 489 | FN = 201 | Sensitivity = 0.7086957  |
|**Actual Negative**| FP = 1819 | TN = 3874 | Specificity = 0.6804848   |
| | Precision =  0.2118718 | Negative PV = 0.9506748 | Accuracy = 0.6835344 |


## Resultados obtenidos en Kaggle
![](./images/kaggle_results.png)

## Descripción detallada del algoritmo propuesto
El algoritmo es el siguiente:

1. Se **dividió los datos** en dos conjuntos: entrenamiento y validación. Con un 80% de los datos para entrenamiento y un 20% para validación.

2. Se realizo **undersampling** al conjunto debido a la alta cantidad de datos negativos. Se redujo la cantidad de datos negativos para igualar a los positivos.

3. Se aplicó el **preprocesamiento** de datos.

4. Se entrenó el modelo de **Random Forest** con el conjunto de entrenamiento, 100 árboles y 3 variables de selección aleatoria.



