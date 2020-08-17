#variables

import time
from datetime import datetime

def init():
    global tiempoRef

    tiempoRef=time.time()

    global V      #estado variador
    global LQR    #control lqr
    global PID    #control pid
    global M      #Modo Manual
    global A      #Modo Automatico
    global MFV    #Manual-frecuencia variador
    global SP     #Automatico - SetPoint
    global P      #variable proporcional
    global I      #variable integral
    global D      #variable derivativa
    global AFV    #Automatico - Frecuencia variador
    global TE     #Temperatura entrada
    global TS     #Temperatura de salida
    global TG     #Temperatura de los gases
    global TC     #temperatura de la camara
    global LTE    #Lectura - temperatura de entrada
    global LTS    #Lectura - temperatura de salida
    global LTG    #Lectura - temperatura de gases
    global LTC    #Lectura - temperatura de la camara
    global LFV    #Lectura - frecuencia variador

    global read   #Habilitar actualizacion de valores

    global tomarDatos
    global row
    global count #Contador interno para descansos del arduino

    global fecha

    #se ajusta el formato fecha hora
    now=datetime.now()
    fecha=now.strftime("_%d_%m__%H_%M")  

    tomarDatos = True
    row=1

    V=False
    LQR=False
    PID=False
    M=False
    A=False
    read=False
    MFV=0
    SP=0
    P=0
    I=0
    D=0
    AFV=0.0
    TE=0.0
    TS=0.0
    TG=0.0
    TC=0.0
    LTE=0.0
    LTS=0.0
    LTG=0.0
    LTC=0.0
    LFV=0.0
    count=0
    
