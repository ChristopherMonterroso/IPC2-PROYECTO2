from ListaDoble import ListaDoble_PA,ListaDoble_Transacciones
from ListaSimple_PA import Simple_PuntosAtencion

class Empresa:
    def __init__(self, codigo, nombre, abreviatura):
        self.codigo= codigo
        self.nombre=nombre
        self.abreviatura=abreviatura
        self.lista_PdS=Simple_PuntosAtencion()
        self.lista_Transacciones=ListaDoble_Transacciones()
        self.siguiente=None
    def getlista_PA(self):
        return self.lista_PdS
        