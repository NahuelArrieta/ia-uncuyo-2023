# TP 7 - Machine Learining - EDA

## ¿Cual es la distribución de las clase inclinacion_peligrosa?
La distribución de la clase inclinacion_peligrosa es la siguiente:
- No: 22640
- Sí: 2889

![](./images/inc_peligrosa_dist.png)

## ¿Se puede considerar alguna sección más peligrosa que otra?

Las secciones Cuarta Oeste, Residencial Norte y Residencial Sur son más peligrosa que el resto.

![Alt text](./images/inc_pel_x_seccion.png)

## ¿Se puede considerar alguna especie más peligrosa que otra?
![Alt text](./images/inc_pel_x_especie.png)

## Generar un histograma de frecuencia para la variable circ_tronco_cm.

![Alt text](./images/dist_circ.png)

## Repetir el punto anterior pero separando por la clase de la variable inclinación_peligrosa

![Alt text](./images/inc_pel_x_circ.png)

## Crear una nueva variable categórica de nombre circ_tronco_cm_cat a partir circ_tronco_cm, en donde puedan asignarse solo  4 posibles valores [ muy alto, alto, medio, bajo ]

```r
discrete_circ <- function(value){
  if (value < 80){
    return("bajo")
  }
  else if (value < 190){
    return("medio")
  }
  else if (value < 250){
    return("alto")
  }
  else {
    return("muy alto")
  }
}

dataframe <- dataframe %>% dplyr::mutate(circ_tronco_cm_discrete = sapply(circ_tronco_cm, discrete_circ))
```