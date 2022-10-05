from http import client
import re
from Cola import ListaEnlazada
class Cliente:
    def __init__(self,dpi,nombre,transacciones,tiempo,estado): #ESTADO PUEDE SER: EN CURSO=1, PENDIENTE=0, FINALIZADO=2
        self.dpi=dpi
        self.nombre=nombre
        self.transacciones=transacciones
        self.tiempo=tiempo
        self.estado=estado
        self.tiempo_espera=None
        self.siguiente=None

class Lista_cliente:
    def __init__(self):
        self.inicio=None
        self.fin=None   
        self.len=0

    def InsertarCliente(self,dpi,nombre,transacciones,tiempo,estado):
        nuevo=Cliente(dpi,nombre,transacciones,tiempo,estado)
        self.len+=1
        if self.inicio is None:
            self.inicio=nuevo
        else:
            tmp=self.inicio
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nuevo
    def mostrarClientes(self):
        tmp=self.inicio
        while tmp is not None:    
           print('DPI: ',tmp.dpi,' Nombre: ',tmp.nombre,' Transacciones: ',tmp.transacciones,"tiempo",tmp.tiempo,' Estado: ',tmp.estado)
           tmp=tmp.siguiente
    def MandarCliente(self,dpis):
        aux = ListaEnlazada()
        tmp=self.inicio
        while tmp is not None:
            if dpis==tmp.dpi:
                
                if tmp.estado==0:
                    tmp.estado=1
                    aux.append(tmp.dpi)
                    aux.append(tmp.nombre)
                    aux.append(tmp.transacciones)
                    aux.append(tmp.tiempo) 
                    return aux
            tmp=tmp.siguiente
    
    def Actualizar_cola(self,lista):
        tmp=self.inicio
        while tmp is not None:
            for i in range(len(lista)):

                if tmp.dpi==lista[i]:
                    if tmp.estado==1:
                        tmp.estado=2
            tmp=tmp.siguiente
        return None
    def pasar_a_escritorio(self):
        tmp=self.inicio
        while tmp is not None:
            if tmp.estado==0:
                print("       Siguiente en pasar:",tmp.nombre,"\n")
                return tmp.dpi
            tmp=tmp.siguiente
        return None
    def comprobar_clientes_atendidos(self):
        cont=0
        cont2=0
        tmp=self.inicio
        while tmp is not None:
            if tmp.estado==2:
                cont+=1
            cont2+=1
            tmp=tmp.siguiente
        if cont==cont2:
            print("       Clientes atendidos en el punto de servicio: ",cont)
            return True
        else:
            return False

    def getCliente(self,dpi):
        tmp=self.inicio
        while tmp is not None:
            if tmp.dpi==dpi:
                return tmp
            tmp=tmp.siguiente
        return None
    def Tiempo_Min_Espera(self):
        lista = []
        tmp=self.inicio
        if self.clientes_en_espera()>0:
            while tmp is not None:
                if tmp.estado==0:
                    lista.append(tmp.tiempo)
                tmp=tmp.siguiente
            return min(lista)
        else:
            while tmp is not None:
                if tmp.estado==1:
                    lista.append(tmp.tiempo)
                tmp=tmp.siguiente
            return min(lista)
        
    def Tiempo_Max_Espera(self):
        contador = 0
        tmp=self.inicio
        if self.clientes_en_espera()>0:
            while tmp is not None:
                if tmp.estado==0:
                    contador=contador+tmp.tiempo
                tmp=tmp.siguiente
            return contador
        else:
            return self.Tiempo_Min_Espera()
        
    def Tiempo_Promedio_Espera(self):
        clientes = 0
        contador = 0
        tmp=self.inicio
        if self.clientes_en_espera()>0:
            while tmp is not None:
                if tmp.estado==0:
                    contador=contador+tmp.tiempo
                    clientes+=1
                tmp=tmp.siguiente
            resultado=contador/clientes
            return resultado
        else:
            while tmp is not None:
                if tmp.estado==1:
                    contador=contador+tmp.tiempo
                    clientes+=1
                tmp=tmp.siguiente
            resultado=contador/clientes
            return resultado


    def Tiempo_Min_Atencion(self):
        lista = []
        tmp=self.inicio
        while tmp is not None:
            lista.append(tmp.tiempo)
            tmp=tmp.siguiente
        return min(lista)

    def tiempo_Max_Atencion(self):
        lista = []
        tmp=self.inicio
        while tmp is not None:
            lista.append(tmp.tiempo)
            tmp=tmp.siguiente
        return max(lista)
    
    def tiempo_espera_En_Escritorio(self,dpi):
        tmp = self.inicio
        while tmp is not None:
            if tmp.dpi ==dpi:
                tmp.tiempo_espera= tmp.tiempo
            tmp=tmp.siguiente
        return None
    def clientes_en_espera(self):
        contador = 0
        tmp=self.inicio
        while tmp is not None:
            if tmp.estado==0:
                contador+=1
            tmp=tmp.siguiente
        return contador

    def tiempo_Promedio_Atencion(self):
        lista = []
        tmp=self.inicio
        while tmp is not None:
            lista.append(tmp.tiempo)
            tmp=tmp.siguiente
        (max(lista)+min(lista))/2
        return (max(lista)+min(lista))/2
    def cola_clientes(self):
        clientes=0
        tmp=self.inicio
        text =""" clientes
            [ label = <
                <table>
                     <tr><td bgcolor="white">clientes en espera:</td><td bgcolor="white">"""+str(self.clientes_en_espera())+"""</td></tr>

                </table>
            >];"""
        while tmp is not None:
            if tmp.estado ==0:
                text+="""c"""+str(clientes)+"""
            [ label = <
                <table>
                    <tr><td bgcolor=\"lightyellow\">Cliente:</td>   <td bgcolor=\"lightyellow\">"""+tmp.nombre+"""</td></tr>
                    <tr><td bgcolor=\"darkseagreen1\">Transacciones:</td>   <td bgcolor=\"darkseagreen1\">"""+str(tmp.transacciones)+"""</td></tr>
                </table>
            > ];"""
                clientes+=1
            
            tmp=tmp.siguiente
        
        for i in range(clientes-1,-1,-1):
            if i ==0:
                text+="""\nc0->clientes"""
            else:
                text+="""\n c"""+str(i)+"""->c"""+str(i-1)
        return text
    def Mandar_tiempos(self):
        try:
            txt=""" 
                <td bgcolor="white">"""+str(self.clientes_en_espera())+"""</td>
                <td bgcolor="white">"""+str(self.Tiempo_Promedio_Espera())+"""</td><td bgcolor="white">"""+str(self.Tiempo_Max_Espera())+"""</td><td bgcolor="white">"""+str(self.Tiempo_Min_Espera()) +"""</td>
                <td bgcolor="white">"""+str(self.tiempo_Promedio_Atencion())+"""</td><td bgcolor="white">"""+ str(self.tiempo_Max_Atencion())+"""</td><td bgcolor="white">"""+str(self.Tiempo_Min_Atencion())+"""</td>
                </tr>"""
            return txt
        except:
            "ERROR"


