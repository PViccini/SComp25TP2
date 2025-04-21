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
    const int iterations = 100000000;  // Número de iteraciones para aumentar el tiempo de ejecución
    float value = 4.56;

    // Medir tiempos a traves de iteraciones
    for (int i = 0; i < iterations; i++) {
        c_float_to_int_add1(value);
        asm_float_to_int_add1(value);
    }

    return 0;
}
