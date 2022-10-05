from DobleES import Lista_Escritorios
from cliente import Lista_cliente
class Punto_servicio:
    def __init__(self,codigo,nombre,direccion):
        self.codigo=codigo
        self.nombre=nombre
        self.direccion=direccion
        self.lista_escritorios = Lista_Escritorios()
        self.lista_clientes = Lista_cliente()
        self.anterior=None
        self.siguiente=None
    def getEscritorios(self):
        return self.lista_escritorios