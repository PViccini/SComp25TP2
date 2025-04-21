## Codigo modificado para poder ejecutarse con gcc (es decir, utilizando sintaxis de GNU AS (GAS) en lugar de NASM)

.global _ftoi_add1_32bits              # Declarar como global para usar fuera de este archivo
.section .text                   # Sección de código

_ftoi_add1_32bits:                     
    pushl %ebp                   # Guardar el puntero base
    movl %esp, %ebp              # Copiar el valor del puntero base al puntero de pila
    subl $4, %esp                # Reservar 4 bytes en la pila para almacenamiento temporal
    fldl 8(%ebp)                 # Cargar el argumento float desde la pila en la FPU
    fistpl (%esp)                # Convertir el float a un entero y almacenarlo en la pila
    movl (%esp), %eax            # Mover el valor entero desde la pila al registro EAX
    addl $1, %eax                # Incrementar el valor entero en 1
    addl $4, %esp                # Liberar el almacenamiento temporal en la pila
    popl %ebp                    # Restaurar el puntero base
    ret                          # Retornar al llamador

.section .note.GNU-stack,"",@progbits   # Evita una advertencia al compilar