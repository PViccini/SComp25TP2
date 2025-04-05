from msl.loadlib import Server32
import ctypes

# Extensión de la clase Server32 para cargar la biblioteca compartida
class MyServer32(Server32):
    def __init__(self, host, port, **kwargs):
        super(MyServer32, self).__init__('conversor_adder.so', 'cdll', host, port)
        self.lib.asm_float_to_int_add1.restype = ctypes.c_int
        self.lib.asm_float_to_int_add1.argtypes = [ctypes.c_float]
    def ftoi_add1_32(self, value):
        return self.lib.asm_float_to_int_add1(value)
