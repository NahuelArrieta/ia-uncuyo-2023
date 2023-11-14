# TP 6 - CSP

## Describir en detalle una formulación CSP para el Sudoku.

El Sudoku es un juego de lógica en el que se debe completar una grilla de 9x9 casilleros con números del 1 al 9, de manera que no se repitan números en una misma fila, columna o subgrilla de 3x3 casilleros. El objetivo del juego es completar la grilla de manera que se cumplan las reglas anteriores.

- Variables: $V =  \{C_{(1,1)}, C_{(1,2)}, \dots, C_{(1,9)}, C_{(2,1)}, \dots, C_{(9,9)}\}$

- Dominio: $D = \{1, 2, \dots, 9\}$

- Restricciones:

    - Dos casillas ubicadas en la misma fila no pueden tener el mismo valor:

        $R_1 = \{C_{(i,j)} \neq C_{(i,k)} \mid j \neq k\}$

    - Dos casillas ubicadas en la misma columna no pueden tener el mismo valor:

        $R_2 = \{C_{(i,j)} \neq C_{(k,j)} \mid i \neq k\}$

    - Dos casillas ubicadas en la misma cuadricula de 3x3 no pueden tener el mismo valor:

        $R_3 = \{C_{(i,j)} \neq C_{(k,l)} \mid  
        \lfloor{{i}\div{3}}\rfloor \neq \lfloor{{k}\div{3}}\rfloor \land 
        \lfloor{{j}\div{3}}\rfloor \neq \lfloor{{l}\div{3}}\rfloor \}$ 


## Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {WA=red, V=blue} para el problema del colorar el mapa de Australia

En la siguiente imagen se muestra como se va reduciendo el dominio de las variables a medida que se van aplicando las restricciones de los arcos (ubicado a la izquierda en naranja) hasta que NT no tiene más valores posibles, demostrando la inconsistencia.

![](./images/ac_3.png)


## Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP.

La complejidad en el peor caso es $O(n * d^2)$, donde $n$ es la cantidad de variables y $d$ es el tamaño del dominio de las variables.

## AC-3 coloca de nuevo en la cola todo arco (Xk, Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Supongamos que por  cada arco ( Xk,Xi)  se puede llevar la cuenta del número de valores restantes de Xi que sean consistentes con cada valor de Xk . Explicar como actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(n² * d²).

Se puede llevar la cuenta en una matriz de d*n, contando la cantidad de valores que sean consistentes con cada valor de esa variable. Luego, al remover un valor del dominio de Xi, se puede actualizar la matriz restando 1 a cada valor de la columna correspondiente a Xi. De esta manera, se puede saber si el arco es consistente en O(1) y actualizar la matriz en O(n*d). Por lo tanto, la complejidad total es O(n² * d²) ya que se debe actualizar la matriz para cada arco.

## Demostrar la correctitud del algoritmo CSP para  árboles estructurados (sección 5.4, p. 172 AIMA 2da edición). Para ello, demostrar: 
### Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica n-consistencia (siendo n número total de variables)
Si suponemos CSP es 2-consistente, para cada restricción binaria los valores en los dominios de las dos variables involucradas son consistentes.

Si comenzamos la propagación de restricciones desde las hojas del árbol, cada vez que lleguemos al nodo padre de un arco, este será consistente ya que los valores de las variables involucradas en el arco son consistentes. Por lo tanto, el CSP será n-consistente.

### Argumentar por qué lo demostrado en a. es suficiente
Cada vez que se remueva un valor del dominio de una variable, se debe propagar la restricción a todas las variables que tengan una restricción binaria con esa variable. Como el grafo de restricciones es un árbol, cada vez que se remueva un valor del dominio de una variable, se propagará hasta la raíz del árbol. 



