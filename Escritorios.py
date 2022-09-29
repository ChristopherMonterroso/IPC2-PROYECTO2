class Escritorios:
    def __init__(self,codigo,identificacion,encargado):
        self.codigo=codigo
        self.identificacion=identificacion
        self.encargado=encargado
        self.anterior=None
        self.siguiente=None