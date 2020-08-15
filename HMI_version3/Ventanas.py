#librerias ventanas
import tkinter as Tk
from tkinter.ttk import Frame
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import font as tkfont

#se importan las ventanas de la interf
from V_principal import *
from V_Manual import *
from V_Automatica import*
#librerias imagenes
from PIL import Image, ImageTk

from Serial_conexion import *

import var

class raiz(Tk.Tk):
    def __init__(self, SerialReference, workbook, *args, **kwargs):
    #def __init__(self,*args, **kwargs):#constructor
        super().__init__(*args, **kwargs)#hereda las caracterisitias de la clase superior en este caso Tkinter

        self.serialReference=SerialReference
        self.workbook=workbook
                
        self.title("Secadora de Café")
        #super().iconbitmap(self, default="UnabCasa.ico")
        self.Imagen1= Tk.PhotoImage(file="button_manual.png")
        self.Imagen2= Tk.PhotoImage(file="button_automatico.png")
        Imagen3= Tk.PhotoImage(file="Unab.png")
        self.Imagen3=Imagen3.subsample(11)
        Imagen4= Tk.PhotoImage(file="Casa.png")
        self.Imagen4= Imagen4.subsample(13)
        load=Image.open('Maquina_v3.png').resize((560,440), Image.ANTIALIAS)
        self.Imagen5= ImageTk.PhotoImage(load)
        
        load=Image.open('button_cargar.png').resize((60,27), Image.ANTIALIAS)
        self.Imagen7= ImageTk.PhotoImage(load)
        load=Image.open('arrow.png').resize((20,20), Image.ANTIALIAS)
        self.Imagen8= ImageTk.PhotoImage(load)
        load=Image.open('arrowDown.png').resize((20,20), Image.ANTIALIAS)
        self.Imagen9= ImageTk.PhotoImage(load)

        load=Image.open('encendido.png').resize((100,30), Image.ANTIALIAS)
        self.Imagen6= ImageTk.PhotoImage(load)
        load=Image.open('apagado.png').resize((100,30), Image.ANTIALIAS)
        self.Imagen10= ImageTk.PhotoImage(load)

        load=Image.open('estado_on.png').resize((15,15), Image.ANTIALIAS)
        self.Imagen11= ImageTk.PhotoImage(load)
        load=Image.open('estado_off.png').resize((15,15), Image.ANTIALIAS)
        self.Imagen12= ImageTk.PhotoImage(load)

        load=Image.open('lqr_on.png').resize((60,30), Image.ANTIALIAS)
        self.Imagen13= ImageTk.PhotoImage(load)
        load=Image.open('lqr_off.png').resize((60,30), Image.ANTIALIAS)
        self.Imagen14= ImageTk.PhotoImage(load)

        load=Image.open('pid_on.png').resize((60,30), Image.ANTIALIAS)
        self.Imagen15= ImageTk.PhotoImage(load)
        load=Image.open('pid_off.png').resize((60,30), Image.ANTIALIAS)
        self.Imagen16= ImageTk.PhotoImage(load)

        load=Image.open('tomaDatos.png').resize((100,30), Image.ANTIALIAS)
        self.Imagen17= ImageTk.PhotoImage(load)
        load=Image.open('Detener.png').resize((100,30), Image.ANTIALIAS)
        self.Imagen18= ImageTk.PhotoImage(load)
        load=Image.open('enviarFrec.png').resize((100,30), Image.ANTIALIAS)
        self.Imagen19= ImageTk.PhotoImage(load)     

        contenedor = Tk.Frame(self)
        contenedor.pack(side="top", fill="both", expand=True)
        contenedor.grid_rowconfigure(0, weight=1)
        contenedor.grid_columnconfigure(0, weight=1)
        contenedor['bg']='white'

        self.frames = {}

        #para una ventana
        #NombrePag=PagInicio.__name__
        #frame= PagInicio(parent=contenedor, controller=self)
        #self.frames[NombrePag]=frame
        #frame.grid(row=0, column=0, sticky="nsew")

        #Para varias ventanas        
        for F in (PagInicio, Manual, Automatico):
            NombrePag= F.__name__
            frame= F(parent=contenedor, controller=self)
            self.frames[NombrePag]=frame
            frame.grid(row=0, column=0, sticky="nsew")
    
        self.MostrarMarco("PagInicio")
        
    def MostrarMarco(self,NombrePag):
        frame = self.frames[NombrePag]
        if(NombrePag == 'Manual'):
            self.serialReference.sendSerialData('M')
            var.read = True
            var.M=True
            var.A=False
            self.serialReference.sendSerialData('E')
                  
        if(NombrePag == 'Automatico'):  
            self.serialReference.sendSerialData('A')
            var.A=True
            var.M=False
            var.read = True
            self.serialReference.sendSerialData('E')
        frame.tkraise()

#para probar se ejectua el siguiente comando
#a=raiz()
