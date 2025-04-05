// TODO: add asm implementation of this function
extern int ftoi_add1(float);

int c_float_to_int_add1(float value)
{
    int int_value = (int)value;
    int_value = int_value + 1;
    return int_value;
}

int asm_float_to_int_add1(float value)
{
    return ftoi_add1(value);
}