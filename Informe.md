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

Además, existe una interfaz gráfica desarrollada en python, que permite un acceso más fácil al programa.

### Diagramas del proyecto

El siguiente diagrama presenta las clases del proyecto:
![Diagrama N°2, diagrama de clases](img/img2.png).

Como se puede apreciar, introdujimos las capas MyClient64 y MiServer32 para salvar la incompatibilidad entre libs de 32bits y python de 64bits.

![Diagrama N°3, diagrama de secuencia](img/img3.png).

En el diagrama de secuencia se puede observar como las capas actúan de manera anidada.

### Time Profiling

#### Función clock

Para realizar el profiling con C de forma directa, se utiliza la función clock(). Se han seguido los siguientes pasos para obtener resultados aproximados:

1. Se crea un nuevo prof_main_med_Clock.c para poder modificar main.c para realizar el profiling.
2. Se crea un nuevo prof_main.s para poder modificar main.s para realizar el profiling. 
3. main.s daba un error de compatibilidad con gcc, por lo que se tradujo de NASM a GAS.
4. Se crea el archivo ensamblador .o para 32 bits.
5. Se compila enlazando el archivo ftoi_add1_32bits.o, y generando el ejecutable prof_main_med_Clock.
6. Luego, se ejecuta el ejecutable prof_main_med_Clock.

Se han obtenido los siguientes resultados:

- Tiempo de función con C: 0.000003 segundos.
- Tiempo de función con ASM: 0.000001 segundos.

Esto representa una pequeña diferencia en tiempos nominales, pero una diferencia muy significativa en comparación, ya que es casi 3 veces más en C que en ASM.

#### Gprof

Utilizando gprof, se realiza también un análisis, para el cual se siguen los siguientes pasos:
1. Se crea un nuevo prof_main_med_gprof.c para poder modificar main.c para realizar el profiling.
2. Se crea una función main simplificada, que llame iteradas veces (10.000.000 de veces) a cada funcion, debido a que son funciones muy rápidas
3. Se compila el programa con la opción -pg, que habilita la generación de datos de profiling, y -O0, para que no optimice el código, evitando posible simplicaciones.
4. Luego, se ejecuta el ejecutable prof_main_med_gprof.

A partir de gprof, se obtienen los siguientes resultados, que representan el tiempo dedicado a cada tarea.

| % Time | Cumulative Seconds | Self Seconds | Calls     | ns/Call (Self) | ns/Call (Total) | Name                    |
|--------|--------------------|--------------|-----------|----------------|------------------|-------------------------|
| 91.97  | 1.26               | 1.26         |           |                |                  | _ftoi_add1_32bits       |
| 4.38   | 1.32               | 0.06         | 10,000,000| 6.00           | 6.00             | asm_float_to_int_add1   |
| 2.92   | 1.36               | 0.04         |           |                |                  | main                    |
| 0.73   | 1.37               | 0.01         |           |                |                  | __x86.get_pc_thunk.bx   |
| 0.00   | 1.37               | 0.00         | 10,000,000| 0.00           | 0.00             | c_float_to_int_add1     |


## Conclusión

El principal problema con el que nos enfrentamos fue la incompatibilidad entre el trabajo en 64 bits de python y en 32 bits del programa de assembler. Sin embargo, la incorporación de la librería msl-loadlib nos permitió salvarlo, de manera tal que pudimos desarrollar el proyecto con todas sus capas interactuando como se deseaba.