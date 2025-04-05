# Trabajo Práctico N°2: Stack Frame
## Cátedra de Sistemas de Computación, FCEFyN, UNC. 2025.

### Grupo: Los puntos flotantes
### Alumnos: Bernaus, Julieta; Di Pasquo, Franco; Viccini, Carlos Patricio.
### Profesor: Jorge, Javier.

## Introducción
En este informe, presentaremos un proyecto de software que utiliza software anidado en diferentes lenguajes y stack frame. Los lenguajes de programación utilizados en este desarrollo son Assembler, C y Python. Stack frame se refiere a una sección del stack dedicada a llamar a una función.

## Desarrollo

### Consigna
La consigna pedía lo siguiente:
- diseñar e implementar calculos en ensamblador,
- recuperar desde la capa superior información de una api REST,
- utilizar python, 
- entregar los datos de consulta a un programa en C que convocará rutinas en ensamblador para que hagan los cálculos de conversión y devuelvan los resultados a las capas superiores,
- mostrar los resultados en una capa superior,
- que la capa superior recuperase la información del banco mundial https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22,
- que se realicen cálculos de conversión de float a enteros y devuelva el índice de un país como Argentina u otro sumando uno (+1).

### Estructura del proyecto

A partir de la consigna, realizamos el siguiente diagrama para ilustrar el programa a realizar:
![Diagrama N°1, estructura del proyecto y responsabilidad de las capas](img/img1.png).

Este diagrama representa la responsabilidad de cada una de las capas.

### Diagramas del proyecto

El siguiente diagrama presenta las clases del proyecto:
![Diagrama N°2, diagrama de clases](img/img2.png).

Como se puede apreciar, introdujimos las capas MyClient64 y MiServer32 para salvar la incompatibilidad entre libs de 32bits y python de 64bits.

![Diagrama N°3, diagrama de secuencia](img/img3.png).

En el diagrama de secuencia se puede observar como las capas actúan de manera anidada.

### Time Profiling

## Conclusión

El principal problema con el que nos enfrentamos fue la incompatibilidad entre el trabajo en 64 bits de python y en 32 bits del programa de assembler. Sin embargo, la incorporación de la librería msl-loadlib nos permitió salvarlo, de manera tal que pudimos desarrollar el proyecto con todas sus capas interactuando como se deseaba.