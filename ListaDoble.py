from PuntoServicio import Punto_servicio
from Escritorios import Escritorios
from Transacciones import Transaccion

class ListaDoble_PA(): #PA : puntos de Atención
    def __init__(self):
        self.inicio=None
    
    def insertarPA(self,codigo,nombre,direccion):
        nuevo=Punto_servicio(codigo,nombre,direccion)
        if self.inicio is None:
            self.inicio=nuevo
        else:
            tmp=self.inicio
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nuevo
            nuevo.anterior=tmp

    def mostrarPA(self):
        tmp=self.inicio
        while tmp is not None:
            print('ID: ',tmp.codigo,' Nombre: ',tmp.nombre,' dirección: ',tmp.direccion)
            tmp=tmp.siguiente

class ListaDoble_Transacciones:
    def __init__(self):
        self.inicio=None
    
    def insertarTransaccion(self,codigo,nombre,tiempo):
        nuevo=Transaccion(codigo,nombre,tiempo)
        if self.inicio is None:
            self.inicio=nuevo
        else:
            tmp=self.inicio
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nuevo
            nuevo.anterior=tmp
    def comprobarID(self,id):
        tmp=self.inicio
        while tmp is not None:
            if tmp.codigo==id:
                return True
            tmp=tmp.siguiente
        return False
    def getTransaccion(self,id):
        tmp=self.inicio
        while tmp is not None:
            if tmp.codigo==id:
                return int(tmp.tiempo)
            tmp=tmp.siguiente
        return None
    def mostrarTransaccion(self):
        tmp=self.inicio
        while tmp is not None:
            print('ID: ',tmp.codigo,' Nombre: ',tmp.nombre,' Tiempo: ',tmp.tiempo,'min')
            tmp=tmp.siguiente