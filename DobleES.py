from Escritorios import Escritorios
class Lista_Escritorios():
    def __init__(self):
        self.inicio=None
    
    def insertarEscritorio(self,codigo,identificacion,encargado):
        nuevo=Escritorios(codigo,identificacion,encargado)
        if self.inicio is None:
            self.inicio=nuevo
        else:
            tmp=self.inicio
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nuevo
            nuevo.anterior=tmp

    def mostrarEscritorio(self):
        tmp=self.inicio
        while tmp is not None:
            print('Código: ',tmp.codigo,' Identificación: ',tmp.identificacion,' Encargado: ',tmp.encargado)
            tmp=tmp.siguiente