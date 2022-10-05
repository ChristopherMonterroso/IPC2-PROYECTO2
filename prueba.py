from cgitb import text
from ListaSimple import ListaSimple
import xml.etree.ElementTree as ET
from xml.dom import minidom
from Cola import ListaEnlazada
Empresa = ListaSimple()

def main ():
   tree=ET.parse('ConfigSys.xml')
   root=tree.getroot()
   for empresa in root:
    id = empresa.attrib['id']
    nombre =empresa[0].text
    abr = empresa[1].text
    Empresa.crearEmpresa(id,nombre, abr)
    for puntosAtencion in empresa[2]:
     idPA=puntosAtencion.attrib['id']
     Nombre_PA=puntosAtencion[0].text
     direccion=puntosAtencion[1].text
     Empresa.getEmpresa(id).lista_PdS.InsertarPunto_Atencion(idPA,Nombre_PA,direccion)
     Escritorio=Empresa.getEmpresa(id).lista_PdS.getPunto_Atencion(idPA)
     for escritorios in puntosAtencion[2]:  
      id_Escritorio=escritorios.attrib['id']
      identifiacion=escritorios[0].text
      Encargado=escritorios[1].text
      Escritorio.lista_escritorios.insertarEscritorio(id_Escritorio,identifiacion,Encargado,False)
    for transacciones in empresa[3]:
     id_transaccion=transacciones.attrib['id']
     nombre_transaccion=transacciones[0].text
     tiempo=transacciones[1].text
     Empresa.getEmpresa(id).lista_Transacciones.insertarTransaccion(id_transaccion,nombre_transaccion,tiempo)


def xml():
  tree=ET.parse('ConfigInit.xml')
  root=tree.getroot()
  for configuracion in root:
    id_empresa=configuracion.attrib['idEmpresa']
    id_punto=configuracion.attrib['idPunto']
    Escritorio=Empresa.getEmpresa(id_empresa).lista_PdS.getPunto_Atencion(id_punto).lista_escritorios
    Cliente=Empresa.getEmpresa(id_empresa).lista_PdS.getPunto_Atencion(id_punto).lista_clientes
    Transaccion=Empresa.getEmpresa(id_empresa).lista_Transacciones
    for escritorios in configuracion[0]:
      activar =escritorios.attrib['idEscritorio']
      Escritorio.CambiarEstadoEscritorio(activar)
    for clientes in configuracion[1]:
      total=0
      nTransacciones=0
      sumando = 0
      for transacciones in clientes[1]:
        nTransacciones=int(transacciones.attrib['cantidad'])
        sumando = sumando+(nTransacciones *int(Transaccion.getTransaccion(transacciones.attrib['idTransaccion'])))
        total = total+nTransacciones
      dpi=clientes.attrib['dpi']
      nombreCliente=clientes[0].text
      Cliente.InsertarCliente(dpi,nombreCliente,total,sumando,0)
      if Escritorio.comprobarActivo(Escritorio.getActivos()):
        Escritorio.AgregarCliente(Escritorio.getActivos(),Cliente.MandarCliente(dpi,Escritorio.getActivos()))      
    Cliente.mostrarClientes()

def prueba():
  lista = ListaEnlazada()
  lista.append("HOLA")
  lista.append("HI")
  print(lista)
  lista.Remove(lista[0])
  print(lista)
  lista.Remove(lista[0])
  print(lista)
  lista.append(200)
  print(lista)
prueba()
#main()
#xml()