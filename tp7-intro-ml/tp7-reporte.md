# TP 7 - Intro Machine Learning

## 1. Indicar si se tendría mejor performance con un método flexible o inflexible

### a) n extremadamente grande, p pequeño
Se espera que un metodo inflexible tenga mejor performance, debido a que hay menos probabilidades de hacer overfitting.

### b) p extremadamente grande, n pequeño
En este caso, com un metodo flexible se tendría mejor performance porque puede ser más capaz de capturar relaciones complejas en los datos.

### c) La relación entre los predictores y la respuesta es altamente no lineal.
Sería mejor utilizar un métodos flexible ya que pueden capturar relaciones no lineales de manera más efectiva.

### d) La varianza de los errores es extremadamente alta.
Como regla general, al usar métodos flexibles, aumenta la varianza. Por lo tanto, lo ideal sería buscar un método flexible pero más restrictivo al mismo tiempo para disminuir la varianza sin aumentar demasiado el sesgo.

## 2. Indicar si es un problema de clasificacióm o regresión; indicar si hay mayor interés en inferencia o predicción; y determinarn n y p.

### a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors aﬀect CEO salary.

- Problema de regresión.
- Se busca inferir la relación entre los factores y el salario del CEO.
- n = 500
- p = 4

### b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.

- Problema de clasificación.
- Se busca predecir si el producto será un éxito o un fracaso.
- n = 20
- p = 14

### c) We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.

- Problema de regresión.
- Se busca predecir el % de cambio en el USD/Euro.
- n = 52 (semanas del año)
- p = 4


## 5.¿Cuáles son las ventajas y desventajas de un enfoque muy flexible (versus un enfoque menos flexible) para la regresión o la clasificación? ¿En qué circunstancias se puede preferir un enfoque más flexible y cuándo uno menos flexible?
En un enfoque flexible para la regresión o clasificación, el modelo se ajusta a los datos de entrenamiento de manera muy precisa cuando la relación subyacente entre los predictores y la respuesta es compleja. Sin embargo, si la relación subyacente entre los predictores y la respuesta es aproximadamente lineal, entonces un enfoque flexible puede resultar en un overfitting de los datos de entrenamiento.

Es conveniente usar un modelo flexible cuando la relación entre los predictores y la respuesta es compleja y cuando el objetivo principal es la predicción en lugar de la interpretación.

En cambio, podría preferirse un enfoque menos flexibles cuando la interpretabilidad es muy importante, cuando los datos son limitados (evita overfitting), o cuando los recursos computacionales son escasos.


## 6. Describa las diferencias entre un enfoque paramétrico y un enfoque no paramétrico. ¿Cuáles son las ventajas de cada uno?
Un enfoque paramétrico asume que la relación entre los predictores y la respuesta se puede resumir mediante un número finito de parámetros. Por ejemplo, asumir que la relación entre los predictores y la respuesta es lineal. En cambio, un enfoque no paramétrico no hace suposiciones explícitas sobre la forma funcional de la relación entre los predictores y la respuesta. En cambio, busca estimar esta relación de manera flexible a partir de los datos.

Un enfoque paramétrico tiene la ventaja de que reduce el problema de estimar f(x) a un problema de estimar un conjunto de parámetros. Esto a su vez reduce la complejidad computacional y estadística del problema. Por otro lado, un enfoque no paramétrico tiene la ventaja de que no hace suposiciones explícitas sobre la forma funcional de la relación entre los predictores y la respuesta, por lo que puede ajustarse a cualquier forma funcional.

## 7. Suponiendo que se quiere usar el sig. dataset para hacer una predicción para Y cuando X1 = X2 = X3 = 0 usando K-nearest neighbors. 

| Obs. | X1  | X2  | X3  |  Y   |
|------|----|----|----|-------|
|  1   |  0 |  3 |  0 |  Red  |
|  2   |  2 |  0 |  0 |  Red  |
|  3   |  0 |  1 |  3 |  Red  |
|  4   |  0 |  1 |  2 | Green |
|  5   | -1 |  0 |  1 | Green |
|  6   |  1 |  1 |  1 |  Red  |

### a) Calcule la distancia Euclidiana entre cada observación y el punto X1 = X2 = X3 = 0.
- obs_1 = 3
- obs_2 = 2
- obs_3 = $\sqrt{10}$
- obs_4 = $\sqrt{5}$
- obs_5 = $\sqrt{2}$
- obs_6 = $\sqrt{3}$

### b) ¿Cuál sería la predicción de Y para K = 1? ¿Por qué?
La predicción sería "Green"; ya que la observación más cercana es 5, que tiene Y = "Green".

### c) ¿Cuál sería la predicción de Y para K = 3? ¿Por qué?
La predicción es Y = "Red" porque 2 de sus 3 vecinos (obs_5 = "Green", obs_2 = obs_6 = "Red") más cercanos tienen esa clase.

### d) Si la frontera de decisión es altamente no lineal, ¿Se esperaría que el mejor valor de K sea grande o pequeño? ¿Por qué?
Para una frontera de decisión altamente no lineal, se esperaría que el mejor valor de K sea pequeño, ya que un valor grande de K implicaría una frontera de decisión más suave. 