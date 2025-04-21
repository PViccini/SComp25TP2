#include <stdio.h>
#include <time.h>

extern int _ftoi_add1_32bits(float);

int c_float_to_int_add1(float value)
{
    int int_value = (int)value;
    int_value = int_value + 1;
    return int_value;
}

int asm_float_to_int_add1(float value)
{
    return _ftoi_add1_32bits(value);
}

int main() {
    clock_t start, end;
    long double tiempo;

    // Medir tiempo de c_float_to_int_add1
    start = clock();
    c_float_to_int_add1(4.56);  // Se agrega un numero tipo flotante al azar
    end = clock();
    tiempo = ((long double)(end - start)) / CLOCKS_PER_SEC;
    printf("Tiempo de funcion con C: %Lf segundos\n", tiempo);

    // Medir tiempo de funcion2
    start = clock();
    asm_float_to_int_add1(4.56); // Se agrega un numero tipo flotante al azar
    end = clock();
    tiempo = ((long double)(end - start)) / CLOCKS_PER_SEC;
    printf("Tiempo de funcion con ASM: %Lf segundos\n", tiempo);

    return 0;
}