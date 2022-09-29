class Transaccion:
    def __init__(self,codigo,nombre,tiempo: int):
        self.codigo=codigo
        self.nombre=nombre
        self.tiempo=tiempo
        self.anterior=None
        self.siguiente=None