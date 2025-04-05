global _ftoi_add1               ; Declarar como global para usar fuera de este archivo
section .text                   

_ftoi_add1:                     
    push ebp                    ; Guardar el puntero base
    mov ebp, esp                ; Copiar el valor del puntero base al puntero de pila
    sub esp, 4                  ; Reservar 4 bytes en la pila para almacenamiento temporal
    fld dword [ebp + 8]         ; Cargar el argumento float desde la pila en la FPU
    fistp dword [esp]           ; Convertir el float a un entero y almacenarlo en la pila
    mov eax, [esp]              ; Mover el valor entero desde la pila al registro EAX
    add eax, 1                  ; Incrementar el valor entero en 1
    add esp, 4                  ; Liberar el almacenamiento temporal en la pila
    pop ebp                     ; Restaurar el puntero base
    ret                         ; Retornar al llamador