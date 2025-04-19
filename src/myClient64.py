from msl.loadlib import Client64

# Extensión de la clase Client64 para cargar la biblioteca compartida
class MyClient64(Client64):
    def __init__(self):
        super(MyClient64, self).__init__(module32='src.myServer32')
    def ftoi_add1_64(self, value):
        return self.request32('ftoi_add1_32', value)
