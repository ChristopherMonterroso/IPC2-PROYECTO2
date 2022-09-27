import easygui
import os
import xml.etree.ElementTree as ET



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
        if choice>4:
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
                choice = int(input()) #Elección


            
    except:
        print("La opción no es un número\n")

    

    
    
    

