from Empresa import Empresa
class ListaSimple():
    def __init__(self):
        self.inicio=None
        self.fin=None   
        self.len=0

    def crearEmpresa(self,codigo,nombre,abreviatura):
        nuevo=Empresa(codigo,nombre,abreviatura)
        self.len+=1
        if self.inicio is None:
            self.inicio=nuevo
        else:
            tmp=self.inicio
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nuevo

    def mostrarEmpresas(self):
        tmp=self.inicio
        while tmp is not None:
            print("Código: ",tmp.codigo,' Nombre: ',tmp.nombre,' Abreviatura: ',tmp.abreviatura)
            
            tmp=tmp.siguiente

    def getEmpresa(self,nombre):
        tmp=self.inicio
        while tmp is not None:
            if tmp.nombre==nombre:
                return tmp
            tmp=tmp.siguiente
        return None
    def getPuntos_Atencion(self,codigo):
        tmp=self.inicio
        while tmp is not None:
            if tmp.codigo==codigo:
                return tmp
            tmp=tmp.siguiente
        return None
    def getNombre(self,codigo):
        tmp=self.inicio
        while tmp is not None:
            if tmp.codigo==codigo:
                return tmp.nombre
            tmp=tmp.siguiente
        return None
    def getCodigo(self,codigo):
        tmp=self.inicio
        while tmp is not None:
            if tmp.codigo==codigo:
                return True
            tmp=tmp.siguiente
        return False


