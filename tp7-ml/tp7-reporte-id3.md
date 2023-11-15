# TP 7 - Random Forest

## Resultados sobre la evaluación sobre tennis.csv

### Minimo de información ganada = 0.23

```
Rules of the tree:
If: outlook = sunny & humidity = high -> no
If: outlook = sunny & humidity = normal -> yes
If: outlook = overcast -> yes
If: outlook = rainy & windy = false -> yes
If: outlook = rainy & windy = true -> no
```

| | **Predicted Positive**| **Predicted Negative** | |
|:--:|:--:|:--:|:--:|
|**Actual Positive**| TP = 7 | FN = 0 | Sensitivity = 1  |
|**Actual Negative**| FP = 0 | TN = 3 | Specificity = 1   |
| | Precision =  1 | Negative PV = 1 | Accuracy = 1 |

### Minimo de información ganada = 0.25

```
Rules of the tree:
Always: yes
```

| | **Predicted Positive**| **Predicted Negative** | |
|:--:|:--:|:--:|:--:|
|**Actual Positive**| TP = 6 | FN = 0 | Sensitivity = 1  |
|**Actual Negative**| FP = 4 | TN = 0 | Specificity = 0   |
| | Precision =  0.6 | Negative PV = 1 | Accuracy = 0.6 |


## Información sobre las estrategias para datos de tipo real
Los árboles decisión se basan en atributos categóricos, por lo que se debe realizar un preprocesamiento de los datos para convertir los atributos numéricos en categóricos. Para esto se puede utilizar la técnica de discretización, que consiste en dividir el rango de valores de un atributo numérico en intervalos y asignarle una categoría a cada intervalo. 
Por otr lado, también es posible determinar umbrales para determinar qué camino debe seguir el árbol. Por ejemplo, si el atributo es la edad, se puede determinar que si la edad es menor a 18 años, el camino a seguir es el de la izquierda, y si es mayor o igual a 18 años, el camino a seguir es el de la derecha.