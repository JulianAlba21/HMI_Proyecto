#!/usr/bin/env python3

#prorgrama principal de la interfaz
#Esta funcion llama a modulos de comunicacion y de despliegue de ventanas

#librerias
from threading import Thread
import time

#se importan variables
import var
#se importa la clase de conexion serial
from Serial_conexion import *
#importamos el modulo ventanas
from Ventanas import *
#importamos el modulo para la hoja de excel
from TomaDatos import *


def main():
    var.init()#se incializan las variables

    #Para comunicación Serial
    #portName='/dev/ttyACM0'
    portName='COM11 '
    baudRate=38400
    dataNumBytes = 4
    numIn=5
    
    s=ConexionSerial(portName, baudRate, dataNumBytes, numIn)
    s.readSerialStart() #No activar si no esta conectado el arduino, inicializa el thread
    #s=1
    if var.tomarDatos==True:
        workSheet=TomarDatos("Datos"+var.fecha)
        app=raiz(s,workSheet)#se incluye comunicaciòn serial y hoja de excel
    else:
        app=raiz(s,0)
    app.geometry("800x450")
    app.resizable(0,0)
    app.mainloop()
    s.close()

if __name__=='__main__':
    #print("Ejecutando Main")
    main()
