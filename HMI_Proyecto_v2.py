from threading import Thread
import serial
import time
import collections
import struct
import copy
import tkinter as Tk
from tkinter.ttk import Frame
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import font as tkfont
import pandas as pd
from PIL import Image, ImageTk
import ctypes
import urllib
import json

#variables contadoras
cont1=255
cont2=255
cont3=255
cont4=255
cont5=255
cont6=255

tiempoRef=time.time()

pot1=0
pot2=0
pot3=0
pot4=0


class raiz(Tk.Tk):
    def __init__(self, SerialReference, *args, **kwargs):#serial reference
        Tk.Tk.__init__(self, *args, **kwargs)

        self.serialReference=SerialReference
                
        self.title("Secadora de Café")
        Tk.Tk.iconbitmap(self, default="UnabCasa.ico")
        self.Imagen1= Tk.PhotoImage(file="button_manual.png")
        self.iconbitmap(self, default='UnabCasa.ico')
        self.Imagen2= Tk.PhotoImage(file="button_automatico.png")
        Imagen3= Tk.PhotoImage(file="Unab.png")
        self.Imagen3=Imagen3.subsample(11)
        Imagen4= Tk.PhotoImage(file="Casa.png")
        self.Imagen4= Imagen4.subsample(13)
        load=Image.open('Maquina.png').resize((600,350), Image.ANTIALIAS)
        self.Imagen5= ImageTk.PhotoImage(load)
        load=Image.open('Tornillo.png').resize((125,70), Image.ANTIALIAS)
        self.Imagen6= ImageTk.PhotoImage(load)
        load=Image.open('button_cargar.png').resize((60,27), Image.ANTIALIAS)
        self.Imagen7= ImageTk.PhotoImage(load)
        load=Image.open('arrow.png').resize((20,20), Image.ANTIALIAS)
        self.Imagen8= ImageTk.PhotoImage(load)
        load=Image.open('arrowDown.png').resize((20,20), Image.ANTIALIAS)
        self.Imagen9= ImageTk.PhotoImage(load)

        contenedor = Tk.Frame(self)
        contenedor.pack(side="top", fill="both", expand=True)
        contenedor.grid_rowconfigure(0, weight=1)
        contenedor.grid_columnconfigure(0, weight=1)
        contenedor['bg']='white'


        barraMenu = Tk.Menu(contenedor)
        ArchivoMenu= Tk.Menu(barraMenu, tearoff=0)
        ArchivoMenu.add_command(label="Salir", command=quit)
        barraMenu.add_cascade(label="Archivo", menu=ArchivoMenu)

        Tk.Tk.config(self, menu=barraMenu)

        self.frames = {}
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
            print('entramos en Manual')
                  
        if(NombrePag == 'Automatico'):  
            self.serialReference.sendSerialData('A')
            print('entramos en automatico')
        frame.tkraise()

class PagInicio(Frame):#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    def __init__(self, parent, controller):
        Tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='white')

        Fondo = Tk.Canvas(self, width=300, height=450, bg="#C9C9C9")#canvas
        Fondo.pack(side='left')
        Fondo.create_text(152,90,text="Dosificado automático de cisco en una secadora de café",font=("Helvetica", 21), fill="gray", width=300, justify="left") #titulo
        Fondo.create_text(150,90,text="Dosificado automático de cisco en una secadora de café",font=("Helvetica", 21), fill="white", width=300, justify="left")
        Fondo.create_text(60,220,text="Integrantes",font=("Helvetica", 13, 'bold'), fill="#240A0A", width=300, justify="left")#integrantes
        Fondo.create_text(127,250,text="José Fernando Calderón Larrotta",font=("Helvetica", 11), fill="#091029", width=300, justify="left")
        Fondo.create_text(90,270,text="Julian Camilo Alba Gil",font=("Helvetica", 11), fill="#091029", width=300, justify="left")
        Fondo.create_text(55,310,text="Directores",font=("Helvetica", 13, 'bold'), fill="#240A0A", width=300, justify="left")#directores
        Fondo.create_text(120,340,text="MSc. Johann Barragán Gómez",font=("Helvetica", 11), fill="#091029", width=300, justify="left")
        Fondo.create_text(160,360,text="MSc. Camilo Enrique Moncada Guayazán  ",font=("Helvetica", 11), fill="#091029", width=300, justify="left")
        Fondo2 = Tk.Canvas(self, width=510, height=450,bg="white")
        Fondo2.pack(side="top")
        Fondo2.create_text(246,60,text="BIENVENIDO!",font=("Helvetica", 15), fill="gray", width=300, justify="center")
        Fondo2.create_text(245,60,text="BIENVENIDO!",font=("Helvetica", 15), fill="black", width=300, justify="center")#sombra
        Fondo2.create_text(241,130,text="Sistema de Control de la Secadora de Cisco",font=("Helvetica", 11, 'bold'), fill="gray", width=500, justify="left")
        Fondo2.create_text(240,130,text="Sistema de Control de la Secadora de Cisco",font=("Helvetica", 11, 'bold'), fill="black", width=500, justify="left") #sombra
        Fondo2.create_text(241,200,text="¿Qué tipo de control desea efectuar?",font=("Helvetica", 11, 'bold'), fill="gray", width=500, justify="left")
        button1 = Tk.Button(self,image=controller.Imagen1, command=lambda: controller.MostrarMarco("Manual"), bg='white') # boton manual
        button1['border']='0'
        button1.pack()
        button2 = Tk.Button(self, image=controller.Imagen2,command=lambda: controller.MostrarMarco("Automatico"), bg='white') #boton automatico
        button2['border']='0'
        button2.pack()
        Fondo2.create_window(120,290, window=button1) #ventana para los botones del canvas
        Fondo2.create_window(360,290, window=button2)
        Fondo2.create_image(450, 390, image=controller.Imagen3) #logo unab
        Fondo.create_line(300,0,300,450)

        

class Manual(Frame):#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def __init__(self, parent, controller):
        Tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='white')

        CanvasM=Tk.Canvas(self, width=800, height=450, bg='white',)
        CanvasM.pack()
        CanvasM.create_image(460,280,image=controller.Imagen5)#Imagen de la maquina
        CanvasM.create_image(570,85,image=controller.Imagen6)

        #Boton Casa
        button1 = Tk.Button(self,image=controller.Imagen4, command=lambda: controller.MostrarMarco("PagInicio"), bg='white')
        button1['border']='0'
        button1.pack()
        #Boton cargar1/ frecuencia motor aire de secado FMAS
        button2 = Tk.Button(self, image=controller.Imagen7,command=lambda: send_FMAS(),bg='white')
        button2['border']='0'
        button2.pack()      
        #Boton cargar2/ Frecuencia motor aire combustion FMAC
        button3 = Tk.Button(self, image=controller.Imagen7,command=lambda: send_FMAC(),bg='white')
        button3['border']='0'
        button3.pack()
        #Boton cargar3 / Frecuencia motor cisco FMC
        button4 = Tk.Button(self, image=controller.Imagen7,command=lambda: send_FMC(),bg='white')
        button4['border']='0'
        button4.pack()

        def send_FMAS():
            controller.serialReference.sendSerialData('B' + str(cont1) + '%')
            print('se envio valor cont 1 = '+str(cont1))
        def send_FMAC():
            controller.serialReference.sendSerialData('C' + str(cont2) + '%')
            print('se envio valor cont 2 = '+str(cont2))
        def send_FMC():
            controller.serialReference.sendSerialData('D' + str(cont3) + '%')
            print('se envio valor cont 3 = '+str(cont3))
        
        #boton flecha arriba 1
        button5 = Tk.Button(self, image=controller.Imagen8,command=lambda: suma1(),bg='white')
        button5['border']='0'
        button5.pack()
        #boton flecha abajo 1
        button6 = Tk.Button(self, image=controller.Imagen9,command=lambda: resta1(),bg='white')
        button6['border']='0'
        button6.pack()
        #boton flecha arriba 2
        button7 = Tk.Button(self, image=controller.Imagen8,command=lambda: suma2(),bg='white')
        button7['border']='0'
        button7.pack()
        #boton flecha abajo 2
        button8 = Tk.Button(self, image=controller.Imagen9,command=lambda: resta2(),bg='white')
        button8['border']='0'
        button8.pack()
        #boton flecha arriba 3
        button9 = Tk.Button(self, image=controller.Imagen8,command=lambda: suma3(),bg='white')
        button9['border']='0'
        button9.pack()
        #boton flecha abajo 3
        button10 = Tk.Button(self, image=controller.Imagen9,command=lambda: resta3(),bg='white')
        button10['border']='0'
        button10.pack()
        #Franja de titulo
        Label1=Tk.Label(self, text='CONTROL MANUAL',bg='#4D4D4D',width=800,height=1,fg='white', font=('Helvetica',10,'bold'),borderwidth=1, relief='solid')
        Label1.pack()

        #Labels escritores****************** modificar
        #Frecuencia motor aire secado
        Label2=Tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=cont1)
        Label2.pack()
        #Frecuencia motor aire combustion
        Label3=Tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=cont2)
        Label3.pack()
        #Frecuencia motor aire cisco
        Label4=Tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=cont3)
        Label4.pack()
        #Frecuencia motor tornillo
        Label5=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=cont4)
        Label5.pack()

        #Frecuencia M. Aire Secado
        Label61=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label61.pack()
        #Frecuencia M. Aire Combustion
        Label7=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label7.pack()
        #Flujo aire de secado
        Label8=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label8.pack()
        #Flujo aire de combustion
        Label9=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label9.pack()
        #Temp aire de entrada
        Label10=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label10.pack()
        #Temp gases de salida
        Label11=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label11.pack()
        #Temp Gases de combustion
        Label12=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label12.pack()
        #Temp Aire de salida
        Label13=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label13.pack()

    #LABELS mostradores ***conectar a arduino



        #Frecuencia motor aire secado
        CanvasM.create_text(101,35, text="Frecuencia Motor Aire Secado",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(100,35, text="Frecuencia Motor Aire Secado",font=("Helvetica", 10), fill="black", width=500, justify="left")
        CanvasM.create_text(90,70, text="Hz",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")
        
        #Frecuencia motor aire combustion
        CanvasM.create_text(112,105, text="Frecuencia Motor Aire Combustión",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(111,105, text="Frecuencia Motor Aire Combustión",font=("Helvetica", 10), fill="black", width=500, justify="left")
        CanvasM.create_text(90,140, text="Hz",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        #Frecuencia motor aire cisco
        CanvasM.create_text(81,175, text="Frecuencia Motor Cisco",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(80,175, text="Frecuencia Motor Cisco",font=("Helvetica", 10), fill="black", width=500, justify="left")
        CanvasM.create_text(90,210, text="Hz",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        #Frecuencia motor tornillo
        CanvasM.create_text(751,90, text="Frecuencia M. Cisco",font=("Helvetica", 8), fill="gray", width=55, justify="center")
        CanvasM.create_text(750,90, text="Frecuencia M. Cisco",font=("Helvetica", 8), fill="black", width=55, justify="center")
        CanvasM.create_text(705,90, text="Hz",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        #Frecuencia M. aire secado
        CanvasM.create_text(41,300, text="Frecuencia M. Aire Secado",font=("Helvetica", 8), fill="gray", width=55, justify="center")
        CanvasM.create_text(40,300, text="Frecuencia M. Aire Secado",font=("Helvetica", 8), fill="black", width=55, justify="center")
        CanvasM.create_text(130,300, text="Hz",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")
        
        #Frecuencia M. aire combustion
        CanvasM.create_text(41,370, text="Frecuencia M. Aire Combustión",font=("Helvetica", 8), fill="gray", width=60, justify="center")
        CanvasM.create_text(40,370, text="Frecuencia M. Aire Combustión",font=("Helvetica", 8), fill="black", width=60, justify="center")
        CanvasM.create_text(130,370, text="Hz",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")
#Flujos
        #Flujo aire de secado
        CanvasM.create_text(251,260, text="Flujo Aire de Secado",font=("Helvetica", 8), fill="gray", width=60, justify="center")
        CanvasM.create_text(250,260, text="Flujo Aire de Secado",font=("Helvetica", 8), fill="black", width=60, justify="center")
        CanvasM.create_text(290,300, text="m3/s",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        #Flujo aire de combustion
        CanvasM.create_text(261,332, text="Flujo Aire de Combustión",font=("Helvetica", 8), fill="gray", width=70, justify="center")
        CanvasM.create_text(260,332, text="Flujo Aire de Combustión",font=("Helvetica", 8), fill="black", width=70, justify="center")
        CanvasM.create_text(290,354, text="m3/s",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")
#Temperaturas

        #Temp. Aire de Entrada

        CanvasM.create_text(331,225, text="Temp. Aire de Entrada",font=("Helvetica", 8), fill="gray", width=60, justify="center")
        CanvasM.create_text(330,225, text="Temp. Aire de Entrada",font=("Helvetica", 8), fill="black", width=60, justify="center")
        CanvasM.create_text(350,250, text="ºC",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        #Temp. Gases de Salida
        CanvasM.create_text(421,125, text="Temp. Gases de Salida",font=("Helvetica", 8), fill="gray", width=60, justify="center")
        CanvasM.create_text(420,125, text="Temp. Gases de Salida",font=("Helvetica", 8), fill="black", width=60, justify="center")
        CanvasM.create_text(450,155, text="ºC",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        #Temp. Gases de Combustión
        CanvasM.create_text(441,350, text="Temp. Gases de Combustión",font=("Helvetica", 8), fill="gray", width=60, justify="center")
        CanvasM.create_text(440,350, text="Temp. Gases de Combustión",font=("Helvetica", 8), fill="black", width=60, justify="center")
        CanvasM.create_text(465,380, text="ºC",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        #Temp. Aire de Salida
        CanvasM.create_text(563,327, text="Temp. Aire de Salida",font=("Helvetica", 8), fill="gray", width=60, justify="center")
        CanvasM.create_text(562,327, text="Temp. Aire de Salida",font=("Helvetica", 8), fill="black", width=60, justify="center")
        CanvasM.create_text(581,367, text="ºC",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        
    #Ventanas para los botones dentro del canvas
        CanvasM.create_window(780,430, window=button1)
        CanvasM.create_window(177,69, window=button2)
        CanvasM.create_window(177,140, window=button3)
        CanvasM.create_window(177,210, window=button4)

        #botones arriba/abajo 1
        CanvasM.create_window(125,57, window=button5)
        CanvasM.create_window(125,82, window=button6)
        #botones arriba/abajo 2
        CanvasM.create_window(125,128, window=button7)
        CanvasM.create_window(125,153, window=button8)
        #botones arriba/abajo 3
        CanvasM.create_window(125,198, window=button9)
        CanvasM.create_window(125,223, window=button10)
    #Ventana para el label
        CanvasM.create_window(400,10, window=Label1)

        def suma1():
            global cont1
            cont1=cont1+1
            Label2.config(text=cont1)
        def resta1():
            global cont1
            cont1=cont1-1
            Label2.config(text=cont1)
        def suma2():
            global cont2
            cont2=cont2+1
            Label3.config(text=cont2)
        def resta2():
            global cont2
            cont2=cont2-1
            Label3.config(text=cont2)
        def suma3():
            global cont3
            cont3=cont3+1
            Label4.config(text=cont3)
        def resta3():
            global cont3
            cont3=cont3-1
            Label4.config(text=cont3)

        #Ventanas Para los Labels
        CanvasM.create_window(50,70, window=Label2) #Frecuencia motor aire secado
        CanvasM.create_window(50,140, window=Label3)#Frecuencia motor aire combustion
        CanvasM.create_window(50,210, window=Label4)#Frecuencia motor aire cisco
        CanvasM.create_window(670,90, window=Label5)#Frecuencia motor tornillo
        CanvasM.create_window(100,300, window=Label61)#Frecuencia M. Aire secado
        CanvasM.create_window(100,370, window=Label7)#Frecuencia M. Aire combustion
        CanvasM.create_window(250,300, window=Label8)#Flujo M. Aire secado
        CanvasM.create_window(250,355, window=Label9)#Flujo M. Aire combustion
        CanvasM.create_window(320,250, window=Label10)#Temp aire entrada
        CanvasM.create_window(420,155, window=Label11)#Temp gases de salida
        CanvasM.create_window(435,380, window=Label12)#Temp gases combustion
        CanvasM.create_window(550,365, window=Label13)#Temp aire salida

        #lineas decorativa
        CanvasM.create_line(0,0,0,240)
        CanvasM.create_line(0,240,220,240)
        CanvasM.create_line(220,240,220,0)
        CanvasM.create_line(1,241,220,241,fill='gray')
        CanvasM.create_line(221,240,221,0,fill='gray')
        CanvasM.create_line(500,40,500,130)
        CanvasM.create_line(501,40,501,130,fill='gray')
        CanvasM.create_line(500,40,785,40)
        CanvasM.create_line(500,41,785,41,fill='gray')
        CanvasM.create_line(785,40,785,130)
        CanvasM.create_line(786,40,786,130,fill='gray')
        CanvasM.create_line(500,130,785,130)
        CanvasM.create_line(500,131,785,131,fill='gray')

        def refresh():

            Label10.config(text=controller.serialReference.getSerialData(1))
            Label11.config(text=controller.serialReference.getSerialData(2))
            Label12.config(text=controller.serialReference.getSerialData(3))
            Label13.config(text=controller.serialReference.getSerialData(4))
            
            self.after(500, refresh)

        refresh()
#se crea la pagina Automatico //////////////////////////////////////////////////
class Automatico(Frame):

    def __init__(self, parent, controller):
        Tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='white')
        CanvasM=Tk.Canvas(self, width=800, height=450, bg='white')
        CanvasM.pack()
        
        CanvasM.create_image(460,280,image=controller.Imagen5)
        CanvasM.create_image(570,85,image=controller.Imagen6)

        button1 = Tk.Button(self,image=controller.Imagen4, command=lambda: controller.MostrarMarco("PagInicio"), bg='white')
        button1['border']='0'
        button1.pack()
        #Boton cargar1 Set Point aire salida/ SetPoint
        button2 = Tk.Button(self, image=controller.Imagen7, command=lambda: send_FMAS(), bg='#DAE3E9')
        button2['border']='0'
        button2.pack()
        #Boton cargar2 Frecuencia motor aire secado / FMAS
        button3 = Tk.Button(self, image=controller.Imagen7, command=lambda: send_FMAC(), bg='white')
        button3['border']='0'
        button3.pack()
        #Boton cargar3 Frecuencia Motor Aire Combustion / FMAC
        button4 = Tk.Button(self, image=controller.Imagen7, command=lambda: send_FMC(), bg='white')
        button4['border']='0'
        button4.pack()

        def send_FMAS():
            controller.serialReference.sendSerialData('E' + str(cont4) + '%')
            print('se envio valor cont 4 = '+str(cont4))
        def send_FMAC():
            controller.serialReference.sendSerialData('F' + str(cont5) + '%')
            print('se envio valor cont 5 = '+str(cont5))
        def send_FMC():
            controller.serialReference.sendSerialData('G' + str(cont6) + '%')
            print('se envio valor cont 6 = '+str(cont6))
            
        #boton flecha arriba 1
        button5 = Tk.Button(self, image=controller.Imagen8,command=lambda: suma1(),bg='#DAE3E9')
        button5['border']='0'
        button5.pack()
        #boton flecha abajo 1
        button6 = Tk.Button(self, image=controller.Imagen9,command=lambda: resta1(),bg='#DAE3E9')
        button6['border']='0'
        button6.pack()
        #boton flecha arriba 2
        button7 = Tk.Button(self, image=controller.Imagen8,command=lambda: suma2(),bg='white')
        button7['border']='0'
        button7.pack()
        #boton flecha abajo 2
        button8 = Tk.Button(self, image=controller.Imagen9,command=lambda: resta2(),bg='white')
        button8['border']='0'
        button8.pack()
        #boton flecha arriba 3
        button9 = Tk.Button(self, image=controller.Imagen8,command=lambda: suma3(),bg='white')
        button9['border']='0'
        button9.pack()
        #boton flecha abajo 3
        button10 = Tk.Button(self, image=controller.Imagen9,command=lambda: resta3(),bg='white')
        button10['border']='0'
        button10.pack()
        #Franja de titulo
        Label1=Tk.Label(self, text='CONTROL AUTOMÁTICO',bg='#ED7D31',width=800,height=1,fg='white', font=('Helvetica',10,'bold'),borderwidth=1, relief='solid')
        Label1.pack()
        #Cuadrado azul de set point
        CanvasM.create_rectangle(0,0,220,90,fill='#DAE3E9')
        
     #Labels escritores****************** modificar
        #Tem. Deseada del Aire de Salida
        Label2=Tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=cont4)
        Label2.pack()
        #Frecuencia motor Aire de secado
        Label3=Tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=cont5)
        #Label3.pack()
        #Frecuencia motor aire de combustion
        Label4=Tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=cont6)
        #Label4.pack()
        #Frecuencia motor tornillo
        Label5=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label5.pack()
        #Frecuencia M. Aire Secado
        Label61=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label61.pack()
        #Frecuencia M. Aire Combustion
        Label7=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label7.pack()
        #Flujo aire de secado
        Label8=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label8.pack()
        #Flujo aire de combustion
        Label9=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label9.pack()
        #Temp aire de entrada
        Label10=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label10.pack()
        #Temp gases de salida
        Label11=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label11.pack()
        #Temp Gases de combustion
        Label12=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label12.pack()
        #Temp Aire de salida
        Label13=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label13.pack()

    #LABELS mostradores ***conectar a arduino

    #textos

        #Temp. Deseada del Aire de Salida
        CanvasM.create_text(111,35, text="Temp. Deseada del Aire de Salida",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(110,35, text="Temp. Deseada del Aire de Salida",font=("Helvetica", 10), fill="black", width=500, justify="left")
        CanvasM.create_text(90,70, text="Hz",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")
        #Frecuencia motor aire secado
        CanvasM.create_text(102,105, text="Frecuencia Motor Aire secado",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(101,105, text="Frecuencia Motor Aire secado",font=("Helvetica", 10), fill="black", width=500, justify="left")
        CanvasM.create_text(90,140, text="Hz",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")
        #Frecuencia Motor Aire Combustión
        CanvasM.create_text(111,175, text="Frecuencia Motor Aire Combustión",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(110,175, text="Frecuencia Motor Aire Combustión",font=("Helvetica", 10), fill="black", width=500, justify="left")
        CanvasM.create_text(90,210, text="Hz",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")
        #Frecuencia motor tornillo
        CanvasM.create_text(751,90, text="Frecuencia M. Cisco",font=("Helvetica", 8), fill="gray", width=55, justify="center")
        CanvasM.create_text(750,90, text="Frecuencia M. Cisco",font=("Helvetica", 8), fill="black", width=55, justify="center")
        CanvasM.create_text(705,90, text="Hz",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")
        #Frecuencia M. aire secado
        CanvasM.create_text(41,300, text="Frecuencia M. Aire Secado",font=("Helvetica", 8), fill="gray", width=55, justify="center")
        CanvasM.create_text(40,300, text="Frecuencia M. Aire Secado",font=("Helvetica", 8), fill="black", width=55, justify="center")
        CanvasM.create_text(130,300, text="Hz",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")     
        #Frecuencia M. aire combustion
        CanvasM.create_text(41,370, text="Frecuencia M. Aire Combustión",font=("Helvetica", 8), fill="gray", width=60, justify="center")
        CanvasM.create_text(40,370, text="Frecuencia M. Aire Combustión",font=("Helvetica", 8), fill="black", width=60, justify="center")
        CanvasM.create_text(130,370, text="Hz",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")
#Flujos
        #Flujo aire de secado
        CanvasM.create_text(251,260, text="Flujo Aire de Secado",font=("Helvetica", 8), fill="gray", width=60, justify="center")
        CanvasM.create_text(250,260, text="Flujo Aire de Secado",font=("Helvetica", 8), fill="black", width=60, justify="center")
        CanvasM.create_text(290,300, text="m3/s",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")
        #Flujo aire de combustion
        CanvasM.create_text(261,332, text="Flujo Aire de Combustión",font=("Helvetica", 8), fill="gray", width=70, justify="center")
        CanvasM.create_text(260,332, text="Flujo Aire de Combustión",font=("Helvetica", 8), fill="black", width=70, justify="center")
        CanvasM.create_text(290,354, text="m3/s",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")
#Temperaturas

        #Temp. Aire de Entrada
        CanvasM.create_text(331,225, text="Temp. Aire de Entrada",font=("Helvetica", 8), fill="gray", width=60, justify="center")
        CanvasM.create_text(330,225, text="Temp. Aire de Entrada",font=("Helvetica", 8), fill="black", width=60, justify="center")
        CanvasM.create_text(350,250, text="ºC",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        #Temp. Gases de Salida
        CanvasM.create_text(421,125, text="Temp. Gases de Salida",font=("Helvetica", 8), fill="gray", width=60, justify="center")
        CanvasM.create_text(420,125, text="Temp. Gases de Salida",font=("Helvetica", 8), fill="black", width=60, justify="center")
        CanvasM.create_text(450,155, text="ºC",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        #Temp. Gases de Combustión
        CanvasM.create_text(441,350, text="Temp. Gases de Combustión",font=("Helvetica", 8), fill="gray", width=60, justify="center")
        CanvasM.create_text(440,350, text="Temp. Gases de Combustión",font=("Helvetica", 8), fill="black", width=60, justify="center")
        CanvasM.create_text(465,380, text="ºC",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        #Temp. Aire de Salida
        CanvasM.create_text(563,327, text="Temp. Aire de Salida",font=("Helvetica", 8), fill="gray", width=60, justify="center")
        CanvasM.create_text(562,327, text="Temp. Aire de Salida",font=("Helvetica", 8), fill="black", width=60, justify="center")
        CanvasM.create_text(581,367, text="ºC",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        
    #Ventanas para los votones dentro del canvas
        CanvasM.create_window(780,430, window=button1)
        CanvasM.create_window(177,69, window=button2)
        CanvasM.create_window(177,140, window=button3)
        CanvasM.create_window(177,210, window=button4)
        CanvasM.create_window(400,10, window=Label1)
        CanvasM.create_window(125,54, window=button5)#botones arriba/abajo 1
        CanvasM.create_window(125,78, window=button6)        
        CanvasM.create_window(125,128, window=button7)#botones arriba/abajo 2
        CanvasM.create_window(125,153, window=button8)      
        CanvasM.create_window(125,198, window=button9)#botones arriba/abajo 3
        CanvasM.create_window(125,223, window=button10)

#Ventanas Para los Labels
        CanvasM.create_window(50,70, window=Label2)#Temp. deseada aire de salida
        CanvasM.create_window(50,140, window=Label3)#Frecuencia motor aire secado
        CanvasM.create_window(50,210, window=Label4)#Frecuencia motor aire combustion
        CanvasM.create_window(670,90, window=Label5)#Frecuencia motor tornillo
        CanvasM.create_window(100,300, window=Label61)#Frecuencia M. Aire secado
        CanvasM.create_window(100,370, window=Label7)#Frecuencia M. Aire combustion
        CanvasM.create_window(250,300, window=Label8)#Flujo M. Aire secado
        CanvasM.create_window(250,355, window=Label9)#Flujo M. Aire combustion
        CanvasM.create_window(320,250, window=Label10)#Temp aire entrada
        CanvasM.create_window(420,155, window=Label11)#Temp gases de salida
        CanvasM.create_window(435,380, window=Label12)#Temp gases combustion
        CanvasM.create_window(550,365, window=Label13)#Temp aire salida

#lineas decorativas
        CanvasM.create_line(0,0,0,240)
        CanvasM.create_line(0,240,220,240)
        CanvasM.create_line(220,240,220,0)
        CanvasM.create_line(1,241,220,241,fill='gray')
        CanvasM.create_line(221,240,221,0,fill='gray')
        CanvasM.create_line(500,40,500,130)
        CanvasM.create_line(501,40,501,130,fill='gray')
        CanvasM.create_line(500,40,785,40)
        CanvasM.create_line(500,41,785,41,fill='gray')
        CanvasM.create_line(785,40,785,130)
        CanvasM.create_line(786,40,786,130,fill='gray')
        CanvasM.create_line(500,130,785,130)
        CanvasM.create_line(500,131,785,131,fill='gray')
        
        def suma1():
            global cont4
            cont4=cont4+1
            Label2.config(text=cont4)
        def resta1():
            global cont4
            cont4=cont4-1
            Label2.config(text=cont4)
        def suma2():
            global cont5
            cont5=cont5+1
            Label3.config(text=cont5)
        def resta2():
            global cont5
            cont5=cont5-1
            Label3.config(text=cont5)
        def suma3():
            global cont6
            cont6=cont6+1
            Label4.config(text=cont6)
        def resta3():
            global cont6
            cont6=cont6-1
            Label4.config(text=cont6)

        def refresh():

            Label10.config(text=controller.serialReference.getSerialData(1))
            Label11.config(text=controller.serialReference.getSerialData(2))
            Label12.config(text=controller.serialReference.getSerialData(3))
            Label13.config(text=controller.serialReference.getSerialData(4))
            
            self.after(500, refresh)

        refresh()

class ConexionSerial: #/////////////////////////////////////////////////////////////////////////////////////////////////////
    def __init__(self, serialPort = 'COM3', serialBaud = 38400, DataNumBytes=4, NumIn=4):
        self.port = serialPort
        self.baud = serialBaud
        self.dataNumBytes=DataNumBytes
        self.numIn=NumIn
        
        self.rawData= bytearray(self.numIn*self.dataNumBytes)
        self.isRun = True
        self.isReceiving = False
        self.thread = None
        self.dataType = 'f'
        self.data=[]

        for i in range(self.numIn):
            self.data.append(collections.deque([0]*1, maxlen=1))
         
        print('Trying to connect to: ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
        try:
            self.serialConnection = serial.Serial(serialPort, serialBaud, timeout=2)
            print('Connected to ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
        except:
            print("Failed to connect with " + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')

    def readSerialStart(self):
        if self.thread == None:
            self.thread = Thread(target=self.backGroundThread)
            self.thread.start()
            while self.isReceiving != True:
                time.sleep(0.1)               

    def getSerialData(self, g=0):
        privateData= copy.deepcopy(self.rawData[:])
        for i in range(self.numIn):
            data =privateData[(i*self.dataNumBytes):(self.dataNumBytes+i*self.dataNumBytes)]
            value, = struct.unpack('f', data)
            self.data[i].append(value)
        pot1=list(self.data[0])
        pot2=list(self.data[1])
        pot3=list(self.data[2])
        pot4=list(self.data[3])
        
        pot1=pot1[0]
        pot2=pot2[0]
        pot3=pot3[0]
        pot4=pot4[0]

        if g == 1:
            return pot1
        if g == 2:
            return pot2
        if g == 3:
            return pot3
        if g == 4:
            return pot4
                   
    def sendSerialData(self, data):
        self.serialConnection.write(data.encode('utf-8'))
               
    def backGroundThread(self):
        time.sleep(1.0)
        self.serialConnection.reset_input_buffer()
        while (self.isRun):
            self.serialConnection.readinto(self.rawData)
            self.isReceiving = True

    def close(self):
        self.isRun = False
        self.thread.join()
        self.serialConnection.close()
        print('Disconnected...')

def main(): 

    #Para comunicación Serial
    portName='COM5'
    baudRate=38400
    dataNumBytes = 4
    numIn=4
    
    s=ConexionSerial(portName, baudRate, dataNumBytes, numIn)
    s.readSerialStart()
    app=raiz(s)
    app.geometry("800x450")
    app.resizable(0,0)
    app.mainloop()
    s.close()
    
if __name__=='__main__':
    main()
