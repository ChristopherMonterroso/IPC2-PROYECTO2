from cliente import Cliente
from Cola import ListaEnlazada
class Escritorios:
    def __init__(self,codigo,identificacion,encargado,estado: bool):
        self.codigo=codigo
        self.identificacion=identificacion
        self.encargado=encargado
        self.estado = estado
        self.cliente=ListaEnlazada()
        self.clientePresente = False
        self.anterior=None
        self.siguiente=None
        self.clienteAtendido=0
