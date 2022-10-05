from stat import IO_REPARSE_TAG_APPEXECLINK
from unicodedata import name
import easygui
import os
import xml.etree.ElementTree as ET
from colorama import Fore
from ListaSimple import ListaSimple

Empresa= ListaSimple() #
limpiar= ListaSimple()
data =""
startAPP = True
def file_upload(type): #type tipo de archivo xml a subir
    if type==1:
        try:
            archivo=easygui.fileopenbox(title="Escoja el archivo .xml",filetypes=("Archivos xml","*.xml"))
            tree = ET.parse(archivo)
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
            
            print("     [ARCHIVO CARGADO CORRECTAMENTE]")
            return archivo
        except:
            print("     [ERROR]")
    
    if type==2:
        try:
            tree = ET.parse(easygui.fileopenbox(title="Escoja el archivo .xml",filetypes=("Archivos xml","*.xml")))
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
                    if Escritorio.comprobarActivo(Escritorio.getActivos())==True:
                        Escritorio.AgregarCliente(Escritorio.getActivos(),Cliente.MandarCliente(dpi))  

            print("         [ARCHIVO CARGADO CORRECTAMENTE]")
        except:
            print("         [Error]")

def crearEmpresa():
    codigo_Empresa = input("ID de la empresa: ")
    Nombre_Empresa = input("Nombre de la empresa: ")
    abreviatura = input("Abreviatura: ")
    Empresa.crearEmpresa(codigo_Empresa,Nombre_Empresa,abreviatura)# Creamos una empresa
    PA= Empresa.getEmpresa(codigo_Empresa)
    #Pedimos la cantidad de puntos de atención que tendrá la empresa
    cantidad_puntos_atencion= int(input(Fore.RED+"\nCantidad de puntos de atención: "))
    print(Fore.GREEN+"Ingrese la información de los puntos de servicio de: [",Nombre_Empresa,"]")
    for i in range (cantidad_puntos_atencion):
        codigo_punto=int(input(Fore.WHITE+"\nID del punto de servicio: "))
        nombre_punto = input("Nombre del punto de servicio: ")
        direccion= input("Dirección del punto de servicio: ")
        PA.lista_PdS.InsertarPunto_Atencion(codigo_punto,nombre_punto,direccion)
        Escritorio = PA.lista_PdS.getPunto_Atencion(codigo_punto)
        #Pedimos la cantidad de Escritorios del punto de servicio
        cantidad_escritorios= int(input(Fore.RED+"\nCantidad de escritorios del punto de servicio: "))
        print(Fore.GREEN+"Ingrese la información de los escritorios del punto de servicio : [",nombre_punto,"]")
        for k in range(cantidad_escritorios):
                codigo_escritorio= int(input(Fore.WHITE+"\nID del escritorio: "))
                identificacion= input("Identificación del escritorio: ")
                encargado= input("Encargado del escritorio: ")
                Escritorio.lista_escritorios.insertarEscritorio(codigo_escritorio,identificacion,encargado,False)
    cantidad_transacciones= int(input(Fore.RED+"\nCantidad de transacciones: "))
    print(Fore.GREEN+"Ingrese la información de las transacciones de: [",Nombre_Empresa,"]")
    for s in range (cantidad_transacciones):
        codigo_transaccion = int(input(Fore.WHITE+"\nID de la transacción: "))
        nombre_transaccion = input("Nombre de la transacción: ")
        tiempo = int(input("Tiempo de la transacción(minutos): "))
        PA.lista_Transacciones.insertarTransaccion(codigo_transaccion,nombre_transaccion,tiempo)
    print("\nEmpresa añadida correctamente")

def limpiar_sistema(archivo):
        try:
            tree=ET.parse(archivo)
            root=tree.getroot()
            for empresa in root:
                id = empresa.attrib['id']
                nombre =empresa[0].text
                abr = empresa[1].text
                limpiar.crearEmpresa(id,nombre, abr)
                for puntosAtencion in empresa[2]:
                    idPA=puntosAtencion.attrib['id']
                    Nombre_PA=puntosAtencion[0].text
                    direccion=puntosAtencion[1].text
                    limpiar.getEmpresa(id).lista_PdS.InsertarPunto_Atencion(idPA,Nombre_PA,direccion)
                    Escritorio=limpiar.getEmpresa(id).lista_PdS.getPunto_Atencion(idPA)
                    for escritorios in puntosAtencion[2]:  
                        id_Escritorio=escritorios.attrib['id']
                        identifiacion=escritorios[0].text
                        Encargado=escritorios[1].text
                        Escritorio.lista_escritorios.insertarEscritorio(id_Escritorio,identifiacion,Encargado,False)
                    Empresa.getEmpresa(id).lista_PdS=limpiar.getEmpresa(id).lista_PdS
        except:
            print("     [ERROR]")
def Ver_Empresas():

    print("         =====================================")
    print("         ||--Soluciones Guatemaltecas S.A.--||")
    print("         =====================================")
    print("         --------Listado de empresas----------")
    Empresa.mostrarEmpresas()
    print("\n Ingrese el ID de la empresa para visualizar\nsus puntos de atención ó presione 0 para regresar")   

def Ver_puntos_atencion(codigo):
    print("         =====================================")
    print("         ||--Soluciones Guatemaltecas S.A.--||")
    print("         =====================================")
    print("             Empresa: ",Empresa.getNombre(codigo))
    print("         --------Puntos de atención----------")
    Empresa.getPuntos_Atencion(codigo).lista_PdS.mostrarPuntos_Atencion()
    print("\n         --------Transacciones-----------")
    Empresa.getEmpresa(codigo).lista_Transacciones.mostrarTransaccion()
    print("\nIngrese el ID del punto de atención para visualizar sus acciones de manejo ó 0 para regresar.")

def Manejo_puntosDeAtencion(codigo,codigo2):
    print("         =====================================")
    print("         ||--Soluciones Guatemaltecas S.A.--||")
    print("         =====================================")
    print("        Punto de atención: ",Empresa.getEmpresa(codigo).lista_PdS.getNombre_Punto_Atencion(codigo2))
    print("              --------Manejo----------")
    print("            1. Estado del punto de atención")
    print("            2. Activar escritorio ")
    print("            3. Desactivar escritorio ")
    print("            4. Atender cliente ")
    print("            5. Solicitud atención")
    print("            6. Simular actividad")
    print("            0. Regresar")
    print("\n       Ingrese la opción a realizar")
    


def Nueva_Empresa():
    print("         =====================================")
    print("         ||--Soluciones Guatemaltecas S.A.--||")
    print("         =====================================")
    print("         --------Crear nueva empresa----------")
    print("\n       Ingrese los datos de la empresa.\n")

def MenuPrincipal():
    print("         =====================================")
    print("         ▓---Soluciones Guatemaltecas S.A.---▓")
    print("         =====================================")
    print("         -----------Menú principal------------")
    print("                 1. Cargar archivo C-S")
    print("                 2. Cargar archivo C-I-P")
    print("                 3. Crear Nueva empresa")
    print("                 4. Ver empresas")
    print("                 5. Limpiar sistema")
    print("                 0. Salir")
    print("\n           Ingrese la opción a realizar")

while startAPP: #Inicia la app
    MenuPrincipal()
    try:
        choice = int(input("        -> ")) #Elección
        if choice>6:
            print("La opción no es válida\n")
        else:
            if choice==0:
                print("     [Ejecución terminada]")
                startAPP= False
            elif choice==1: #Carga archivo de congfiguración del sistema
                data= file_upload(1)
            elif choice==2: #Carga archivo inicial para la prueba
                file_upload(2)
            elif choice==3:
                Nueva_Empresa()     
                crearEmpresa()
            elif choice==4:
                verEmpresas= True
                while verEmpresas:
                    print("")
                    Ver_Empresas()
                    id_empresa = input("        -> ")
                    if id_empresa=="0":
                        verEmpresas=False 
                        #confirma que el código sea válido 
                    else:
                        if Empresa.getCodigo(id_empresa)==True:
                            empresav= Empresa.getPuntos_Atencion(id_empresa).lista_PdS
                            transacciones=Empresa.getEmpresa(id_empresa).lista_Transacciones
                            codigo = id_empresa
                            verPuntosAtencion= True
                            while verPuntosAtencion:
                                print("")
                                Ver_puntos_atencion(id_empresa)
                                id_PA= input("        -> ")
                                Punto_Atencion=id_PA
                                if id_PA=="0":
                                    verPuntosAtencion=False
                                elif empresav.getCodigo(id_PA)==True:
                                    Manejo_PA=True
                                    while Manejo_PA:
                                        print("")
                                        Manejo_puntosDeAtencion(codigo,id_PA)
                                        opcion = input("        -> ")
                                        if opcion=="0":
                                            Manejo_PA=False
                                        elif opcion=="1":
                                            try:
                                                print("                Generando gráfica")
                                                print("\n       ----Estado del punto de atención----")
                                                empresav.getPunto_Atencion(id_PA).lista_escritorios.grafico_esperas(empresav.getPunto_Atencion(id_PA).lista_clientes.Mandar_tiempos())
                                                input("\n             [Presione ENTER]\n")
                                                print("         ----Estado escritorios activos----")
                                                empresav.getPunto_Atencion(id_PA).lista_escritorios.cola_para_pasar(empresav.getPunto_Atencion(id_PA).lista_clientes.cola_clientes())
                                                input("\n             [Presione ENTER]\n")
                                            except:
                                                print("         <<No se ha logrado generar la gráfica>>") 
                                        elif opcion=="2":
                                            empresav.getPunto_Atencion(id_PA).lista_escritorios.mostrarEscritorio()
                                            
                                            print("\nIngrese el ID del escritorio del cual desea activar.")
                                            id_escritorio= input("        -> ")
                                            print("")
                                            if empresav.getPunto_Atencion(id_PA).lista_escritorios.getID_Escritorio(id_escritorio)==True:
                                                empresav.getPunto_Atencion(id_PA).lista_escritorios.CambiarEstadoEscritorio(id_escritorio)
                                                print("\n         Escritorio Activado")
                    
                                            else:
                                                print("         No se ha logrado completar la acción.")
                                        elif opcion=="3":
                                            empresav.getPunto_Atencion(id_PA).lista_escritorios.mostrarEscritorio()
                                            
                                            print("\nIngrese el ID del escritorio del cual desea desactivar.")
                                            id_escritorio= input("        -> ")
                                            print("")
                                            if empresav.getPunto_Atencion(id_PA).lista_escritorios.getID_Escritorio(id_escritorio)==True:
                                                if empresav.getPunto_Atencion(id_PA).lista_escritorios.Cambiar_a_inactivo(id_escritorio)==True:
                                                    print("\n         Escritorio Desactivado")
                                                else:
                                                    print("\n     Atención -> ¡Este escritorio ya está inactivo!")
                                            else:
                                                print("         No se ha logrado completar la acción.")
                                        
                                        elif opcion=="4":
                                            Cliente=empresav.getPunto_Atencion(id_PA).lista_clientes
                                            escritorio=empresav.getPunto_Atencion(id_PA).lista_escritorios
                                            empresav.getPunto_Atencion(id_PA).lista_clientes.Actualizar_cola(escritorio.atender_cliente())
                                            if Cliente.len>0:
                                                if Cliente.clientes_en_espera()>0:
                                                    for i in range (escritorio.SinCliente()):
                                                        escritorio.AgregarCliente(escritorio.getActivos(),Cliente.MandarCliente(Cliente.pasar_a_escritorio())) 
                                                input("\n             [Presione ENTER]\n")
                                            else:
                                                print("             No hay clientes para atender")
                                        elif opcion=="5":
                                            Escritorio=empresav.getPunto_Atencion(id_PA).lista_escritorios
                                            sumando = 0
                                            print("         --Nuevo cliente--")
                                            dpi=input("     DPI: ")
                                            nombre= input("     Nombre: ")
                                            transacciones.mostrarTransaccion()
                                            ntransacciones= int(input("\n     Cantidad de transacciones: "))
                                            for i in range (ntransacciones):
                                                id_transaccion= input("     Ingrese el ID de la transacción: ")
                                                sumando = sumando+int(transacciones.getTransaccion(id_transaccion))
                                            empresav.getPunto_Atencion(id_PA).lista_clientes.InsertarCliente(dpi,nombre,ntransacciones,sumando,0)
                                            if Escritorio.comprobarActivo(Escritorio.getActivos())==True:
                                                Escritorio.AgregarCliente(Escritorio.getActivos(),empresav.getPunto_Atencion(id_PA).lista_clientes.MandarCliente(dpi))
                                                print("Cliente pasa a escritorio")
                                            else:
                                                print("\n     Cliente añadido a la cola ☻")
                                        elif opcion=="6":
                                            Cliente=empresav.getPunto_Atencion(id_PA).lista_clientes
                                            escritorio=empresav.getPunto_Atencion(id_PA).lista_escritorios
                                            print("       ╔═══════════════════════╗")
                                            print("       ║Simulación de actividad║")
                                            print("       ╚═══════════════════════╝")

                                            simular =True
                                            while simular:
                                                empresav.getPunto_Atencion(id_PA).lista_clientes.Actualizar_cola(escritorio.atender_cliente())
                                                if Cliente.len>0:
                                                    if Cliente.clientes_en_espera()>0:
                                                        for i in range (escritorio.SinCliente()):
                                                            escritorio.AgregarCliente(escritorio.getActivos(),Cliente.MandarCliente(Cliente.pasar_a_escritorio()))
                                                if Cliente.comprobar_clientes_atendidos()==True:
                                                    print("\n       Escritorios activos: ",escritorio.ContadorActivos())
                                                    print("       Escritorios inactivos: ",escritorio.ContadorInactivo())
                                                    print("")
                                                    escritorio.clientes_atendidos()
                                                    simular=False
                                            print("       ╔════════════════════╗")
                                            print("       ║Simulación terminada║")
                                            print("       ╚════════════════════╝")
                                            input("             [Presione ENTER]\n")
                                        else:
                                            print("         Opción inválida")
                                else:
                                    print("         ID incorrecto")
                        else:
                            print("         ID incorrecto")
                else:
                    print("         ID incorrecto")
            elif choice==5:
                limpiar_sistema(data)
                print("\n       ╔═══════════════════════════════╗")
                print("       ║Sistema reiniciado exitosamente║")
                print("       ╚═══════════════════════════════╝\n")
    except:
        print("Opción inválida\n")

    

    
    
    

