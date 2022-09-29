from PuntoServicio import Punto_servicio
class Simple_PuntosAtencion():
    def __init__(self):
        self.inicio=None
        self.fin=None   
        self.len=0

    def InsertarPunto_Atencion(self,codigo,nombre,direccion):
        nuevo=Punto_servicio(codigo,nombre,direccion)
        self.len+=1
        if self.inicio is None:
            self.inicio=nuevo
        else:
            tmp=self.inicio
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nuevo

    def mostrarPuntos_Atencion(self):
        tmp=self.inicio
        while tmp is not None:
            print("Código: ",tmp.codigo,' Nombre: ',tmp.nombre,' Abreviatura: ',tmp.direccion)
            tmp=tmp.siguiente
            
    def getPunto_Atencion(self,nombre):
        tmp=self.inicio
        while tmp is not None:
            if tmp.nombre==nombre:
                return tmp
            tmp=tmp.siguiente
        return None
