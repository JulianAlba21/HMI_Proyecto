import tkinter as Tk
from tkinter.ttk import Frame

#se importan variables
import var

class Manual(Frame):

    def __init__(self, parent, controller):
        Tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='white')

        CanvasM=Tk.Canvas(self, width=800, height=450, bg='white',)
        CanvasM.pack()
        CanvasM.create_image(472,230,image=controller.Imagen5)#Imagen de la maquina
     
        
#BOTONES
        
        #Boton Casa
        button1 = Tk.Button(self,image=controller.Imagen4, command=lambda: B_casa(), bg='white')
        button1['border']='0'
        button1.pack()
        CanvasM.create_window(780,430, window=button1)

        def B_casa():
            var.M=False
            var.A=False
            var.read=False
            controller.serialReference.sendSerialData('E') #se inhabilita enviada de datos desde arduino
            
            button5.config(image=controller.Imagen10)
            button6.config(image=controller.Imagen12)
            controller.serialReference.sendSerialData('F' + str(0) + '%') #se envia valor cero de frecuencia al variador

            if var.V==False:
                pass
            else:
                controller.serialReference.sendSerialData('V')
                var.V=False

            controller.MostrarMarco("PagInicio")
                
        #Boton cargar1/ frecuencia variador
        button2 = Tk.Button(self, image=controller.Imagen7,command=lambda: send_MFV(),bg='white')
        button2['border']='0'
        button2.pack()
        CanvasM.create_window(177,140, window=button2)
        
        def send_MFV():
            Label4.config(text=var.MFV)
            controller.serialReference.sendSerialData('F' + str(var.MFV) + '%')            
        
        #boton flecha arriba 1
        button3 = Tk.Button(self, image=controller.Imagen8,command=lambda: suma(),bg='white')
        button3['border']='0'
        button3.pack()
        CanvasM.create_window(125,128, window=button3)
        
        #boton flecha abajo 1
        button4 = Tk.Button(self, image=controller.Imagen9,command=lambda: resta(),bg='white')
        button4['border']='0'
        button4.pack()
        CanvasM.create_window(125,152, window=button4)

        def suma():
            var.MFV=var.MFV+1
            Label2.config(text=var.MFV)
        def resta():
            var.MFV=var.MFV-1
            Label2.config(text=var.MFV)

        #Boton encendido/apagado variador
        button5 = Tk.Button(self, image=controller.Imagen10,command=lambda: send_EV(),bg='white')
        button5['border']='0'
        button5.pack()
        CanvasM.create_window(100,70, window=button5)

        def send_EV():#enviar estado variador
            controller.serialReference.sendSerialData('V')
            if var.V == False:
                button5.config(image=controller.Imagen6)
                button6.config(image=controller.Imagen11)
                var.V=True
            elif var.V == True:
                button5.config(image=controller.Imagen10)
                button6.config(image=controller.Imagen12)
                var.V=False

        #boton falso, usado para cambio de imagenes
        button6 = Tk.Button(self, image=controller.Imagen12,bg='white')
        button6['border']='0'
        button6.pack()
        CanvasM.create_window(565,333, window=button6)

#LABELS
        
        #Franja de titulo
        Label1=Tk.Label(self, text='CONTROL MANUAL',bg='#4D4D4D',width=800,height=1,fg='white', font=('Helvetica',10,'bold'),borderwidth=1, relief='solid')
        Label1.pack()
        CanvasM.create_window(400,10, window=Label1)

    #VENTANA DE CONTROL
        
        #Frecuencia variador
        Label2=Tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=var.MFV)
        Label2.pack()
        CanvasM.create_window(50,140, window=Label2)

    #EN IMAGEN
        
        #Frecuencia motor cisco
        Label4=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=var.MFV)
        Label4.pack()
        CanvasM.create_window(620,360, window=Label4)

        #Temp aire de entrada
        Label10=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid',text=var.TE)
        Label10.pack()
        CanvasM.create_window(300,225, window=Label10)#Temp aire entrada
        
        #Temp gases
        Label11=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid',text=var.TG)
        Label11.pack()
        CanvasM.create_window(505,140, window=Label11)#Temp gases
        
        #Temp camara
        Label12=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid',text=var.TC)
        Label12.pack()
        CanvasM.create_window(475,385, window=Label12)
        
        #Temp Aire de salida
        Label13=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid',text=var.TS)
        Label13.pack()
        CanvasM.create_window(630,300, window=Label13)


#TEXTOS

    #VENTANA DE CONTROL

        #Encendido/Apagado Variador
        CanvasM.create_text(101,35, text="Encendido/Apagado Variador",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(100,35, text="Encendido/Apagado Variador",font=("Helvetica", 10), fill="black", width=500, justify="left")
        
        
        #Frecuencia Variador
        CanvasM.create_text(76,105, text="Frecuencia Variador",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(75,105, text="Frecuencia Variador",font=("Helvetica", 10), fill="black", width=500, justify="left")
        CanvasM.create_text(90,140, text="Hz",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")        

    #EN IMAGEN

        #Frecuencia variador
        CanvasM.create_text(626,385, text="Frecuencia M. Cisco",font=("Helvetica", 8), fill="gray", width=55, justify="center")
        CanvasM.create_text(625,385, text="Frecuencia M. Cisco",font=("Helvetica", 8), fill="black", width=55, justify="center")
        CanvasM.create_text(652,360, text="Hz",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")    

        #TEMPERATURAS

        #Temp. Aire de Entrada
        CanvasM.create_text(306,200, text="Temp. Aire de Entrada",font=("Helvetica", 8), fill="gray", width=60, justify="center")
        CanvasM.create_text(305,200, text="Temp. Aire de Entrada",font=("Helvetica", 8), fill="black", width=60, justify="center")
        CanvasM.create_text(330,225, text="ºC",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        #Temp. Gases de Salida
        CanvasM.create_text(506,110, text="Temp. Gases de Salida",font=("Helvetica", 8), fill="gray", width=60, justify="left")
        CanvasM.create_text(505,110, text="Temp. Gases de Salida",font=("Helvetica", 8), fill="black", width=60, justify="left")
        CanvasM.create_text(535,140, text="ºC",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        #Temp. Gases de Combustión
        CanvasM.create_text(523,417, text="Temp. Gases de Combustión",font=("Helvetica", 8), fill="gray", width=60, justify="left")
        CanvasM.create_text(522,417, text="Temp. Gases de Combustión",font=("Helvetica", 8), fill="black", width=60, justify="left")
        CanvasM.create_text(505,385, text="ºC",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

        #Temp. Aire de Salida
        CanvasM.create_text(631,275, text="Temp. Aire de Salida",font=("Helvetica", 8), fill="gray", width=60, justify="center")
        CanvasM.create_text(630,275, text="Temp. Aire de Salida",font=("Helvetica", 8), fill="black", width=60, justify="center")
        CanvasM.create_text(660,300, text="ºC",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")


    #TABLA FLUJOS AIRE DE SECADO Y COMPUERTA

        CanvasM.create_text(85,240, text="Flujo Aire de secado según posición de compuerta",font=("Helvetica", 8, 'bold'), fill="black", width=200, justify="left")
        CanvasM.create_text(58,270, text="Pos.  Flujo [kg/s] ",font=("Helvetica", 8, 'bold'), fill="black", width=200, justify="left")
        CanvasM.create_text(18,310, text="0 1 2 3 ",font=("Helvetica", 8, 'bold'), fill="black", width=10, justify="left")
        CanvasM.create_text(70,310, text="0.02864  0.04247  0.12722  0.24733",font=("Helvetica", 8, 'bold'), fill="black", width=50, justify="left")

        CanvasM.create_text(228,332, text="0",font=("Helvetica", 8, 'bold'), fill="black", width=50, justify="left")
        CanvasM.create_text(208,332, text="1",font=("Helvetica", 8, 'bold'), fill="black", width=50, justify="left")
        CanvasM.create_text(195,317, text="2",font=("Helvetica", 8, 'bold'), fill="black", width=50, justify="left")
        CanvasM.create_text(195,300, text="3",font=("Helvetica", 8, 'bold'), fill="black", width=50, justify="left")



    #LINEAS VENTANA DE CONTROL
        CanvasM.create_line(0,0,0,240)
        CanvasM.create_line(0,180,220,180)
        CanvasM.create_line(220,180,220,0)
        CanvasM.create_line(1,181,220,181,fill='gray')
        CanvasM.create_line(221,180,221,0,fill='gray')


        def refresh():

            Label10.config(text=controller.serialReference.getSerialData(1))
            Label11.config(text=controller.serialReference.getSerialData(2))
            Label12.config(text=controller.serialReference.getSerialData(3))
            Label13.config(text=controller.serialReference.getSerialData(4))
           
            self.after(500, refresh)

        refresh()
