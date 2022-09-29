import easygui
import os
import xml.etree.ElementTree as ET
from colorama import Fore
from ListaSimple import ListaSimple

Empresa= ListaSimple() #
startAPP = True
def file_upload(type): #type tipo de archivo xml a subir
    if type==1:
        try:
            tree = ET.parse(easygui.fileopenbox(title="Escoja el archivo .xml",filetypes=("Archivos xml","*.xml")))
            print("ARCHIVO CARGADO CORRECTAMENTE")
        except:
            print("ERROR")
    if type==2:
        try:
            tree = ET.parse(easygui.fileopenbox(title="Escoja el archivo .xml",filetypes=("Archivos xml","*.xml")))
            print("ARCHIVO CARGADO CORRECTAMENTE")
        except:
            print("Error")

def crearEmpresa():
    codigo_Empresa = int(input("Código de la empresa: "))
    Nombre_Empresa = input("Nombre de la empresa: ")
    abreviatura = input("Abreviatura: ")
    Empresa.crearEmpresa(codigo_Empresa,Nombre_Empresa,abreviatura)# Creamos una empresa
    PA= Empresa.getEmpresa(Nombre_Empresa)
    #Pedimos la cantidad de puntos de atención que tendrá la empresa
    cantidad_puntos_atencion= int(input(Fore.RED+"\nCantidad de puntos de atención: "))
    print(Fore.GREEN+"Ingrese la información de los puntos de servicio de: [",Nombre_Empresa,"]")
    for i in range (cantidad_puntos_atencion):
        codigo_punto=int(input(Fore.WHITE+"\nCódigo del punto de servicio: "))
        nombre_punto = input("Nombre del punto de servicio: ")
        direccion= input("Dirección del punto de servicio: ")
        PA.lista_PdS.InsertarPunto_Atencion(codigo_punto,nombre_punto,direccion)
        Escritorio = PA.lista_PdS.getPunto_Atencion(nombre_punto)
        #Pedimos la cantidad de Escritorios del punto de servicio
        cantidad_escritorios= int(input(Fore.RED+"\nCantidad de escritorios del punto de servicio: "))
        print(Fore.GREEN+"Ingrese la información de los escritorios del punto de servicio : [",nombre_punto,"]")
        for k in range(cantidad_escritorios):
                codigo_escritorio= int(input(Fore.WHITE+"\nCódigo del escritorio: "))
                identificacion= input("Identificación del escritorio: ")
                encargado= input("Encargado del escritorio: ")
                Escritorio.lista_escritorios.insertarEscritorio(codigo_escritorio,identificacion,encargado)
    cantidad_transacciones= int(input(Fore.RED+"\nCantidad de transacciones: "))
    print(Fore.GREEN+"Ingrese la información de las transacciones de: [",Nombre_Empresa,"]")
    for s in range (cantidad_transacciones):
        codigo_transaccion = int(input(Fore.WHITE+"\nCódigo de la transacción: "))
        nombre_transaccion = input("Nombre de la transacción: ")
        tiempo = int(input("Tiempo de la transacción(minutos): "))
        PA.lista_Transacciones.insertarTransaccion(codigo_transaccion,nombre_transaccion,tiempo)
             
        
    
    print("\nEmpresa añadida correctamente")

def Ver_Empresas():

        print("=====================================")
        print("||--Soluciones Guatemaltecas S.A.--||")
        print("=====================================")
        print("--------Listado de empresas----------")
        Empresa.mostrarEmpresas()
        print("\nIngrese el código de la empresa para visualizar\nsus puntos de atención ó presione 0 para regresar")   

def Ver_puntos_atencion(codigo):
    print("=====================================")
    print("||--Soluciones Guatemaltecas S.A.--||")
    print("=====================================")
    print("     Empresa: ",Empresa.getNombre(codigo))
    print("--------Puntos de atención----------")
    Empresa.getPuntos_Atencion(codigo).lista_PdS.mostrarPuntos_Atencion()
    print("\nIngrese el código de la empresa para visualizar \nsus puntos de atención ó presione 0 para regresar")



def Nueva_Empresa():
    print("=====================================")
    print("||--Soluciones Guatemaltecas S.A.--||")
    print("=====================================")
    print("--------Crear nueva empresa----------")
    print("\nIngrese los datos de la empresa.\n")

def MenuPrincipal():
    print("=====================================")
    print("||--Soluciones Guatemaltecas S.A.--||")
    print("=====================================")
    print("-----------Menú principal------------")
    print("       1. Cargar archivo C-S")
    print("       2. Cargar archivo C-I-P")
    print("       3. Crear Nueva empresa")
    print("       4. Ver empresas")
    print("       5. Limpiar sistema")
    print("       0. Salir")
    print("\nIngrese la opción a realizar")

while startAPP: #Inicia la app
    MenuPrincipal()
    try:
        choice = int(input()) #Elección
        if choice>6:
            print("La opción no es válida\n")
        else:
            if choice==0:
                print("Ejecución terminada")
                startAPP= False
            elif choice==1: #Carga archivo de congfiguración del sistema
                file_upload(1)
            elif choice==2: #Carga archivo inicial para la prueba
                file_upload(2)
            elif choice==3:
                Nueva_Empresa()     
                crearEmpresa()
            elif choice==4:
                verEmpresas= True
                while verEmpresas:
                    Ver_Empresas()
                    choice = int(input())
                    if choice==0:
                        verEmpresas=False
                    elif Empresa.getCodigo(choice)==True:
                        verPuntosAtencion= True
                        while verPuntosAtencion:
                            Ver_puntos_atencion(choice)
                            choice= int(input())
                            if choice==0:
                                verPuntosAtencion=False
    except:
        print("La opción no es un número\n")

    

    
    
    

