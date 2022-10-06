from re import X
from tkinter.messagebox import NO
from Escritorios import Escritorios
from cliente import Cliente
from Cola import ListaEnlazada
import graphviz
import os
class Lista_Escritorios():
    def __init__(self):
        self.inicio=None
    
    def insertarEscritorio(self,codigo,identificacion,encargado,estado):
        nuevo=Escritorios(codigo,identificacion,encargado,estado)
        if self.inicio is None:
            self.inicio=nuevo
        else:
            tmp=self.inicio
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nuevo
            nuevo.anterior=tmp
    def CambiarEstadoEscritorio(self,codigo):
        tmp=self.inicio
        while tmp is not None:
            if tmp.codigo==codigo:
                if tmp.estado==False:
                    tmp.estado=True
                    return True
            tmp=tmp.siguiente
        return False

    def Cambiar_a_inactivo(self,codigo):
        tmp=self.inicio
        while tmp is not None:
            if tmp.codigo==codigo:
                if tmp.estado==True:
                    tmp.estado=False
                    return True
            tmp=tmp.siguiente
        return False
    def mostrarEscritorio(self):
        tmp=self.inicio
        while tmp is not None:
            if tmp.estado==False:
                
                    print('ID: ',tmp.codigo,' Identificación: ',tmp.identificacion,' Encargado: ',tmp.encargado,' Estado: Inactivo')
            else:
                    print('ID: ',tmp.codigo,' Identificación: ',tmp.identificacion,' Encargado: ',tmp.encargado,' Estado: Activa')

            tmp=tmp.siguiente
    def ContadorActivos(self):
        activos= 0
        tmp=self.inicio
        while tmp is not None:
            if tmp.estado==True:
                activos+=1
            tmp=tmp.siguiente
        return activos

    def ContadorInactivo(self):
        inactivos= 0
        tmp=self.inicio
        while tmp is not None:
            if tmp.estado==False:
                inactivos+=1
            tmp=tmp.siguiente
        return inactivos
    
   
    def getEscritorio(self,codigo):
        tmp=self.inicio
        while tmp is not None:
            if tmp.codigo==codigo:
                return tmp
            tmp=tmp.siguiente
        return None
    def getActivos(self):
        tmp=self.inicio
        while tmp is not None:
            if tmp.estado==True and tmp.clientePresente==False:
                return tmp.codigo
            tmp=tmp.siguiente
        return None
    def comprobarActivo(self,id):
        tmp=self.inicio
        while tmp is not None:
            if id == tmp.codigo:
                if tmp.estado==True and tmp.clientePresente==False:
                    return True
            tmp=tmp.siguiente
        return False

    def Agregar_a_Escritorio(self,idEscritorio,cliente):
        tmp = self.inicio
        while tmp is not None:
            if tmp.codigo==idEscritorio :
                if tmp.estado==True and tmp.clientePresente==False:
                    tmp.clientePresente=True
                    tmp.cliente.append(cliente)
                    
            tmp=tmp.siguiente
        return None
    
    def AgregarCliente(self,idEscritorio,cliente):
        tmp = self.inicio
        while tmp is not None:
            if tmp.codigo==idEscritorio :
                if tmp.estado==True and tmp.clientePresente==False:
                    tmp.clientePresente=True
                    tmp.cliente.append(cliente)
            tmp=tmp.siguiente
        return None
    

    def getID_Escritorio(self,ID): #Comprobar que el ID existe
        tmp=self.inicio
        while tmp is not None:
            if tmp.codigo==ID:
                return True
            tmp=tmp.siguiente
        return False
    def MostrarCliente(self):
        contador= 0
        tmp=self.inicio
        while tmp is not None and tmp.cliente!= None:
            if tmp.estado==True and tmp.clientePresente==False:
                print(tmp.identificacion,"",tmp.cliente)
            tmp=tmp.siguiente

    def menor_tiempo(self):
        lista = ListaEnlazada()
        contador= self.ContadorActivos()
        tmp=self.inicio
        while tmp is not None:
            if tmp.estado==True and tmp.clientePresente==True:
                lista.append(tmp.cliente[0][3])
            tmp=tmp.siguiente
        menor = 500
        for i in range (len(lista)):
            if lista[i]<=menor:
                menor = lista[i]
        return menor
    def remover_cliente(self,lista):
        tmp= self.inicio
        while tmp is not None:
            for i in range(len(lista)):
                if tmp.codigo==lista[i]:
                    tmp.cliente.Remove(tmp.cliente[0])
            tmp=tmp.siguiente
    def SinCliente(self):
        contador = 0
        tmp= self.inicio
        while tmp is not None:
            if tmp.estado==True and tmp.clientePresente==False:
                contador+=1
            tmp=tmp.siguiente
        return contador

    def atender_cliente(self):
        quitar= ListaEnlazada()
        mandar= ListaEnlazada()
        tiempo = self.menor_tiempo()
        tmp=self.inicio
        mandar_dpi=""
        contador = 0
        while tmp is not None:
            if tmp.estado==True and tmp.clientePresente==True:
                if tmp.cliente[0][3]== tiempo:
                    print("       Cliente:  ",tmp.cliente[0][1],"atendido.")
                    print("       Escritorio",tmp.identificacion,"libre.\n")
                    tmp.clienteAtendido+=1
                    tmp.clientePresente=False
                    quitar.append(tmp.codigo)
                    mandar.append(tmp.cliente[0][0])
                else:
                    tmp.cliente[0][3]=tmp.cliente[0][3]-tiempo
            tmp=tmp.siguiente
        self.remover_cliente(quitar)
        return mandar
    def clientes_atendidos(self):
        tmp = self.inicio
        while tmp is not None:
            if tmp.clienteAtendido>0:
                print(
                    "      ",tmp.clienteAtendido,"clientes atendidos en el escritorio: ",tmp.identificacion
                )
            tmp=tmp.siguiente

    def cola_para_pasar(self,cola_clientesd):
        activos= 0
        tmp=self.inicio
        RutaPng="Fila de espera"
        text="""
                digraph X{
                    rankdir= BT
                    node[shape=none fontname=Helvetica]\n"""
        while tmp is not None:
            if tmp.estado==True and tmp.clientePresente==True:
                text+="""n"""+str(activos)+"""
            [ label = <
                <table>
                    <tr><td bgcolor=\"lightgray\">Escritorio:</td>      <td bgcolor=\"lightgray\">"""+tmp.identificacion+"""</td></tr>
                    <tr><td bgcolor=\"aliceblue\">Encargado:</td>      <td bgcolor=\"aliceblue\">"""+tmp.encargado+"""</td></tr>
                    <tr><td bgcolor=\"lightyellow\">Cliente en atención:</td>   <td bgcolor=\"lightyellow\">"""+str(tmp.cliente[0][1])+"""</td></tr>
                    <tr><td bgcolor=\"darkseagreen1\">Transacciones:</td>   <td bgcolor=\"darkseagreen1\">"""+str(tmp.cliente[0][2])+"""</td></tr>
                    <tr><td bgcolor=\"aliceblue\">Tiempo total de espera:</td>     <td bgcolor=\"aliceblue\">"""+str(tmp.cliente[0][3])+""" minutos</td></tr>      
                </table>
            > ];"""
                activos+=1
            
            tmp=tmp.siguiente
        text+="\n n100"+"""
        [ label = <
            <table>
                <tr><td bgcolor="white">«Fila de espera»  ╠ </td></tr>
             </table>
         > ];
         
         
         """
        text+=cola_clientesd
        for i in range(activos):
            text+="""\n clientes->n"""+str(i)
        for i in range(activos):
            text+="""\n n"""+str(i)+"""->n100"""
        text+="}"
        try:
            src = graphviz.Source(text,format="png")
            src.render(RutaPng)
            if os.path.exists(RutaPng):
                os.remove(RutaPng)
            os.startfile(str(RutaPng)+".png")
            print("Atención: Se guardo el archivo con el nombre: "+str(RutaPng)+".png")
        except :
            print("Error")

    def grafico_esperas(self,texto):
        RutaPng="Info. Punto atención"
        text="""
        digraph X{
            rankdir=TB
            node[shape=none fontname=Helvetica]
            n1
            [ label = <
                <table>
                    <tr><td bgcolor="white">Estado del punto de atención </td></tr>
             </table>
         > ];
            n2
            [ label = <
                <table>
                    <tr><td bgcolor=\"lightgray\">Escritorios activos</td>      <td bgcolor=\"lightgray\">Escritorios inactivos</td>    <td bgcolor=\"lightgray\">Clientes en espera de atención</td>
                        <td bgcolor=\"lightgray\">Tiempo promedio de espera</td><td bgcolor=\"lightgray\">Tiempo máximo de espera</td>  <td bgcolor=\"lightgray\">Tiempo mínimo de espera</td>
                        <td bgcolor=\"lightgray\">Tiempo promedio de atención</td><td bgcolor=\"lightgray\">Tiempo máximo de atención</td><td bgcolor=\"lightgray\">Tiempo mínimo de atención</td>
                    </tr> 
                    <tr><td bgcolor="white">"""+str(self.ContadorActivos())+"""</td>      <td bgcolor="white">"""+str(self.ContadorInactivo())+"""</td>"""
        text+=texto
        text+="""</table>> ];           
         n1->n2
         }"""
        try:
            src = graphviz.Source(text,format="png")
            src.render(RutaPng)
            if os.path.exists(RutaPng):
                os.remove(RutaPng)
            os.startfile(str(RutaPng)+".png")
            print("Atención: Se guardo el archivo con el nombre: "+str(RutaPng)+".png")
        except :
            print("Error")
            