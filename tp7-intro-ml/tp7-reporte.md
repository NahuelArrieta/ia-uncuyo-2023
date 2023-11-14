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



