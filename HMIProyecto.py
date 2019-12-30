
import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import font as tkfont
from PIL import Image, ImageTk

import ctypes
import urllib
import json

#variables contadoras
cont1=0
cont2=0
cont3=0
cont4=0
cont5=0
cont6=0

class raizHMI(tk.Tk):
#Se crea la raiz y el metodo de cambio entre paginas

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

    #imagen boton manual
        self.Imagen1= tk.PhotoImage(file="button_manual.png")
    #imagen boton automatico
        self.Imagen2= tk.PhotoImage(file="button_automatico.png")
    #imagen Unab
        Imagen3= tk.PhotoImage(file="Unab.png")
        self.Imagen3=Imagen3.subsample(11)
    #imagen casa
        Imagen4= tk.PhotoImage(file="Casa.png")
        self.Imagen4= Imagen4.subsample(13)
    #imagen maquina
        load=Image.open('Maquina.png').resize((600,350), Image.ANTIALIAS)
        self.Imagen5= ImageTk.PhotoImage(load)
    #imagen tornillo
        load=Image.open('Tornillo.png').resize((125,70), Image.ANTIALIAS)
        self.Imagen6= ImageTk.PhotoImage(load)
    #imagen boton cargar
        load=Image.open('button_cargar.png').resize((60,27), Image.ANTIALIAS)
        self.Imagen7= ImageTk.PhotoImage(load)
    #Imagen flechas de control subir
        load=Image.open('arrow.png').resize((20,20), Image.ANTIALIAS)
        self.Imagen8= ImageTk.PhotoImage(load)
    #Imagen flechas de control bajar
        load=Image.open('arrowDown.png').resize((20,20), Image.ANTIALIAS)
        self.Imagen9= ImageTk.PhotoImage(load)
        
        tk.Tk.iconbitmap(self, default="UnabCasa.ico")
        tk.Tk.wm_title(self, "Secadora de Café")

        contenedor = tk.Frame(self)
        contenedor.pack(side="top", fill="both", expand=True)
        contenedor.grid_rowconfigure(0, weight=1)
        contenedor.grid_columnconfigure(0, weight=1)

        barraMenu = tk.Menu(contenedor)
        ArchivoMenu= tk.Menu(barraMenu, tearoff=0)
        ArchivoMenu.add_command(label="Salir", command=quit)
        barraMenu.add_cascade(label="Archivo", menu=ArchivoMenu)

        tk.Tk.config(self, menu=barraMenu)

        self.frames = {}
        for F in (PagInicio, Manual, Automatico):
            NombrePag= F.__name__
            frame= F(parent=contenedor, controller=self)
            self.frames[NombrePag]=frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.MostrarMarco("PagInicio")

       
    def MostrarMarco(self,NombrePag):
        frame = self.frames[NombrePag]
        frame.tkraise()


#Se crea la pagina de inicio o presentacion \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class PagInicio(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='white')
        

        #Canvas 
        Fondo = tk.Canvas(self, width=300, height=450, bg="#C9C9C9")
        Fondo.pack(side='left')

        #textos

        #Titulo
        Fondo.create_text(152,90,text="Dosificado automático de cisco en una secadora de café",font=("Helvetica", 21), fill="gray", width=300, justify="left")
        Fondo.create_text(150,90,text="Dosificado automático de cisco en una secadora de café",font=("Helvetica", 21), fill="white", width=300, justify="left")
        #Integrantes
        Fondo.create_text(60,220,text="Integrantes",font=("Helvetica", 13, 'bold'), fill="#240A0A", width=300, justify="left")
        Fondo.create_text(127,250,text="José Fernando Calderón Larrotta",font=("Helvetica", 11), fill="#091029", width=300, justify="left")
        Fondo.create_text(90,270,text="Julian Camilo Alba Gil",font=("Helvetica", 11), fill="#091029", width=300, justify="left")
        #Directores
        Fondo.create_text(55,310,text="Directores",font=("Helvetica", 13, 'bold'), fill="#240A0A", width=300, justify="left")
        Fondo.create_text(120,340,text="MSc. Johann Barragán Gómez",font=("Helvetica", 11), fill="#091029", width=300, justify="left")
        Fondo.create_text(160,360,text="MSc. Camilo Enrique Moncada Guayazán  ",font=("Helvetica", 11), fill="#091029", width=300, justify="left")

        #Parte derecha
        Fondo2 = tk.Canvas(self, width=510, height=450,bg="white")
        Fondo2.pack(side="top")

        #Titulo
        Fondo2.create_text(246,60,text="BIENVENIDO!",font=("Helvetica", 15), fill="gray", width=300, justify="center")
        #sombra titulo
        Fondo2.create_text(245,60,text="BIENVENIDO!",font=("Helvetica", 15), fill="black", width=300, justify="center")

        #texto
        Fondo2.create_text(241,130,text="Sistema de Control de la Secadora de Cisco",font=("Helvetica", 11, 'bold'), fill="gray", width=500, justify="left")
        Fondo2.create_text(240,130,text="Sistema de Control de la Secadora de Cisco",font=("Helvetica", 11, 'bold'), fill="black", width=500, justify="left")

        #Pregunta
        Fondo2.create_text(241,200,text="¿Qué tipo de control desea efectuar?",font=("Helvetica", 11, 'bold'), fill="gray", width=500, justify="left")

        #Boton Manual
        button1 = tk.Button(self,image=controller.Imagen1, command=lambda: controller.MostrarMarco("Manual"), bg='white')
        button1['border']='0'
        button1.pack()

        #Boton Automatico
        button2 = tk.Button(self, image=controller.Imagen2,command=lambda: controller.MostrarMarco("Automatico"), bg='white')
        button2['border']='0'
        button2.pack()

        #Ventanas para los votones dentro del canvas
        Fondo2.create_window(120,290, window=button1)
        Fondo2.create_window(360,290, window=button2)

        #imagen logo unab
        Fondo2.create_image(450, 390, image=controller.Imagen3)

        #linea decorativa
        Fondo.create_line(300,0,300,450)

#Se crea la paginal de Manual /////////////////////////////////////////////////
class Manual(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='white')

        CanvasM=tk.Canvas(self, width=800, height=450, bg='white',)
        CanvasM.pack()
        
        #Imagen de la maquina
        CanvasM.create_image(460,280,image=controller.Imagen5)

        #Imagen del tornillo
        CanvasM.create_image(570,85,image=controller.Imagen6)

        #Boton Casa
        button1 = tk.Button(self,image=controller.Imagen4, command=lambda: controller.MostrarMarco("PagInicio"), bg='white')
        button1['border']='0'
        button1.pack()

        #Boton cargar1
        button2 = tk.Button(self, image=controller.Imagen7,bg='white')
        button2['border']='0'
        button2.pack()
        #Boton cargar2
        button3 = tk.Button(self, image=controller.Imagen7,bg='white')
        button3['border']='0'
        button3.pack()
        #Boton cargar3
        button4 = tk.Button(self, image=controller.Imagen7,bg='white')
        button4['border']='0'
        button4.pack()

        #boton flecha arriba 1
        button5 = tk.Button(self, image=controller.Imagen8,command=lambda: suma1(),bg='white')
        button5['border']='0'
        button5.pack()
        #boton flecha abajo 1
        button6 = tk.Button(self, image=controller.Imagen9,command=lambda: resta1(),bg='white')
        button6['border']='0'
        button6.pack()

        #boton flecha arriba 2
        button7 = tk.Button(self, image=controller.Imagen8,command=lambda: suma2(),bg='white')
        button7['border']='0'
        button7.pack()
        #boton flecha abajo 2
        button8 = tk.Button(self, image=controller.Imagen9,command=lambda: resta2(),bg='white')
        button8['border']='0'
        button8.pack()

        #boton flecha arriba 3
        button9 = tk.Button(self, image=controller.Imagen8,command=lambda: suma3(),bg='white')
        button9['border']='0'
        button9.pack()
        #boton flecha abajo 3
        button10 = tk.Button(self, image=controller.Imagen9,command=lambda: resta3(),bg='white')
        button10['border']='0'
        button10.pack()

        #Franja de titulo
        Label1=tk.Label(self, text='CONTROL MANUAL',bg='#4D4D4D',width=800,height=1,fg='white', font=('Helvetica',10,'bold'),borderwidth=1, relief='solid')
        Label1.pack()

     #Labels escritores****************** modificar
        #Frecuencia motor aire secado
        Label2=tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=cont1)
        Label2.pack()
        #Frecuencia motor aire combustion
        Label3=tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=cont2)
        #Label3.pack()
        #Frecuencia motor aire cisco
        Label4=tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=cont3)
        #Label4.pack()
        #Frecuencia motor tornillo
        Label5=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=cont4)
        Label5.pack()

        #Frecuencia M. Aire Secado
        Label61=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label61.pack()
        #Frecuencia M. Aire Combustion
        Label7=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label7.pack()
        #Flujo aire de secado
        Label8=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label8.pack()
        #Flujo aire de combustion
        Label9=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label9.pack()
        #Temp aire de entrada
        Label10=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label10.pack()
        #Temp gases de salida
        Label11=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label11.pack()
        #Temp Gases de combustion
        Label12=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label12.pack()
        #Temp Aire de salida
        Label13=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label13.pack()

    #LABELS mostradores ***conectar a arduino

        #Frecuencia M. Aire Secado
        Label6=tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label6.pack()

    #textos

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
        
        #Frecuencia motor aire secado
        CanvasM.create_window(50,70, window=Label2)
        #Frecuencia motor aire combustion
        CanvasM.create_window(50,140, window=Label3)
        #Frecuencia motor aire cisco
        CanvasM.create_window(50,210, window=Label4)
        #Frecuencia motor tornillo
        CanvasM.create_window(670,90, window=Label5)
        #Frecuencia M. Aire secado
        CanvasM.create_window(100,300, window=Label61)
        #Frecuencia M. Aire combustion
        CanvasM.create_window(100,370, window=Label7)
        #Flujo M. Aire secado
        CanvasM.create_window(250,300, window=Label8)
        #Flujo M. Aire combustion
        CanvasM.create_window(250,355, window=Label9)
        #Temp aire entrada
        CanvasM.create_window(320,250, window=Label10)
        #Temp gases de salida
        CanvasM.create_window(420,155, window=Label11)
        #Temp gases combustion
        CanvasM.create_window(435,380, window=Label12)
        #Temp aire salida
        CanvasM.create_window(550,365, window=Label13)

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

        
        
#se crea la pagina Automatico //////////////////////////////////////////////////
class Automatico(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='white')
        CanvasM=tk.Canvas(self, width=800, height=450, bg='white')
        CanvasM.pack()

        #Imagen de la maquina
        CanvasM.create_image(460,280,image=controller.Imagen5)
        #Imagen del tornillo
        CanvasM.create_image(570,85,image=controller.Imagen6)

        #Boton Casa
        button1 = tk.Button(self,image=controller.Imagen4, command=lambda: controller.MostrarMarco("PagInicio"), bg='white')
        button1['border']='0'
        button1.pack()

        #Boton cargar1
        button2 = tk.Button(self, image=controller.Imagen7,bg='#DAE3E9')
        button2['border']='0'
        button2.pack()
        #Boton cargar2
        button3 = tk.Button(self, image=controller.Imagen7,bg='white')
        button3['border']='0'
        button3.pack()
        #Boton cargar3
        button4 = tk.Button(self, image=controller.Imagen7,bg='white')
        button4['border']='0'
        button4.pack()

        #Boton Casa
        button1 = tk.Button(self,image=controller.Imagen4, command=lambda: controller.MostrarMarco("PagInicio"), bg='white')
        button1['border']='0'
        button1.pack()

        #Franja de titulo
        Label1=tk.Label(self, text='CONTROL AUTOMÁTICO',bg='#ED7D31',width=800,height=1,fg='white', font=('Helvetica',10,'bold'),borderwidth=1, relief='solid')
        Label1.pack()

        #Cuadrado azul de set point
        CanvasM.create_rectangle(0,0,220,90,fill='#DAE3E9')
        
     #Labels escritores****************** modificar
        #Tem. Deseada del Aire de Salida
        Label2=tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label2.pack()
        #Frecuencia motor Aire de secado
        Label3=tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        #Label3.pack()
        #Frecuencia motor aire de combustion
        Label4=tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        #Label4.pack()
        #Frecuencia motor tornillo
        Label5=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label5.pack()

        #Frecuencia M. Aire Secado
        Label61=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label61.pack()
        #Frecuencia M. Aire Combustion
        Label7=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label7.pack()
        #Flujo aire de secado
        Label8=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label8.pack()
        #Flujo aire de combustion
        Label9=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label9.pack()
        #Temp aire de entrada
        Label10=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label10.pack()
        #Temp gases de salida
        Label11=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label11.pack()
        #Temp Gases de combustion
        Label12=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label12.pack()
        #Temp Aire de salida
        Label13=tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label13.pack()

    #LABELS mostradores ***conectar a arduino

        #Frecuencia M. Aire Secado
        Label6=tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid')
        Label6.pack()

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

#Ventanas Para los Labels
        
        #Temp. deseada aire de salida
        CanvasM.create_window(50,70, window=Label2)
        #Frecuencia motor aire secado
        CanvasM.create_window(50,140, window=Label3)
        #Frecuencia motor aire combustion
        CanvasM.create_window(50,210, window=Label4)
        #Frecuencia motor tornillo
        CanvasM.create_window(670,90, window=Label5)
        #Frecuencia M. Aire secado
        CanvasM.create_window(100,300, window=Label61)
        #Frecuencia M. Aire combustion
        CanvasM.create_window(100,370, window=Label7)
        #Flujo M. Aire secado
        CanvasM.create_window(250,300, window=Label8)
        #Flujo M. Aire combustion
        CanvasM.create_window(250,355, window=Label9)
        #Temp aire entrada
        CanvasM.create_window(320,250, window=Label10)
        #Temp gases de salida
        CanvasM.create_window(420,155, window=Label11)
        #Temp gases combustion
        CanvasM.create_window(435,380, window=Label12)
        #Temp aire salida
        CanvasM.create_window(550,365, window=Label13)

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
        
# Se asigna el tamano de la ventana y se incia el ciclo
if __name__ == "__main__":
    app=raizHMI()
    app['bg']='white'
    app.geometry("800x450")
    app.resizable(0,0)
    app.mainloop()
