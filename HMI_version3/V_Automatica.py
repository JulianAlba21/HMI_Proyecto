import tkinter as Tk
from tkinter.ttk import Frame

#importar variables
import var

class Automatico(Frame):

    def __init__(self, parent, controller):
        Tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='white')
        
        CanvasM=Tk.Canvas(self, width=800, height=450, bg='white')
        CanvasM.pack()
        
        CanvasM.create_image(472,230,image=controller.Imagen5)

#BOTONES
        
        #Boton Casa
        button1 = Tk.Button(self,image=controller.Imagen4, command=lambda: B_casa(), bg='white')
        button1['border']='0'
        button1.pack()
        CanvasM.create_window(780,430, window=button1)

        def B_casa():
            var.M=False
            var.A=False
            var.LQR=False
            var.PID=False
            var.read=False

            controller.serialReference.sendSerialData('E') #se inhabilita enviada de datos desde arduino
            
            button5.config(image=controller.Imagen10)
            button6.config(image=controller.Imagen12)
            button7.config(image=controller.Imagen14)
            button8.config(image=controller.Imagen16)
            if var.V==False:
                pass
            else:
                controller.serialReference.sendSerialData('V')
                var.V=False
            controller.MostrarMarco("PagInicio")
                
        #Boton cargar1/ SetPoint
        button2 = Tk.Button(self, image=controller.Imagen7,command=lambda: send_SP(),bg='#DAE3E9')
        button2['border']='0'
        button2.pack()
        CanvasM.create_window(177,183, window=button2)

        def send_SP():
            controller.serialReference.sendSerialData('S' + str(var.SP) + '%')
                
        #boton flecha arriba
        button3 = Tk.Button(self, image=controller.Imagen8,command=lambda: sumaSP(),bg='#DAE3E9')
        button3['border']='0'
        button3.pack()
        CanvasM.create_window(125,175, window=button3)
        
        #boton flecha abajo
        button4 = Tk.Button(self, image=controller.Imagen9,command=lambda: restaSP(),bg='#DAE3E9')
        button4['border']='0'
        button4.pack()
        CanvasM.create_window(125,197, window=button4)

        def sumaSP():
            var.SP=var.SP+1
            Label2.config(text=var.SP)
        def restaSP():
            var.SP=var.SP-1
            Label2.config(text=var.SP)

        #Boton encendido/apagado variador
        button5 = Tk.Button(self, image=controller.Imagen10,command=lambda: send_EV(),bg='white')
        button5['border']='0'
        button5.pack()
        CanvasM.create_window(100,65, window=button5)

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

        #boton LQR
        button7 = Tk.Button(self, image=controller.Imagen14,bg='white', command=lambda: control('LQR'))
        button7['border']='0'
        button7.pack()
        CanvasM.create_window(65,125, window=button7)

        #boton PID
        button8 = Tk.Button(self, image=controller.Imagen16,bg='white',command=lambda: control('PID'))
        button8['border']='0'
        button8.pack()
        CanvasM.create_window(135,125, window=button8)
        
        def control(est):
            if est=='LQR':
                if var.LQR == False:
                    button7.config(image=controller.Imagen13)
                    var.LQR=True
                    controller.serialReference.sendSerialData('L')
                    button8.config(image=controller.Imagen16)
                    var.PID=False
                    controller.serialReference.sendSerialData('N')
                elif var.LQR == True:
                    controller.serialReference.sendSerialData('L')
                    button7.config(image=controller.Imagen14)
                    var.LQR=False

            if est=='PID':
                if var.PID == False:
                    controller.serialReference.sendSerialData('N')
                    button8.config(image=controller.Imagen15)
                    var.PID=True
                    controller.serialReference.sendSerialData('L')
                    button7.config(image=controller.Imagen14)
                    var.LQR=False
                elif var.PID == True:
                    controller.serialReference.sendSerialData('N')
                    button8.config(image=controller.Imagen16)
                    var.PID=False

        #Cuadrado azul de set point
        CanvasM.create_rectangle(0,145,220,210,fill='#DAE3E9')

#VENTANA PID
        
        #boton cargar P
        button9 = Tk.Button(self, image=controller.Imagen7,bg='white',command=lambda: send_P())
        button9['border']='0'
        button9.pack()
        CanvasM.create_window(768,60, window=button9)
        def send_P():
            controller.serialReference.sendSerialData('P' + str(var.P) + '%')
        
        #boton flecha arriba P
        button10 = Tk.Button(self, image=controller.Imagen8,bg='white', command=lambda:sumaP())
        button10['border']='0'
        button10.pack()
        CanvasM.create_window(725,50, window=button10)
        #boton flecha abajo P
        button11 = Tk.Button(self, image=controller.Imagen9,bg='white', command=lambda:restaP())
        button11['border']='0'
        button11.pack()
        CanvasM.create_window(725,73, window=button11)

        def sumaP():
            var.P=var.P+1
            Label3.config(text=var.P)
        def restaP():
            var.P=var.P-1
            Label3.config(text=var.P)

        #boton cargar I
        button12 = Tk.Button(self, image=controller.Imagen7,bg='white',command=lambda:send_I())
        button12['border']='0'
        button12.pack()
        CanvasM.create_window(768,110, window=button12)

        def send_I():
            controller.serialReference.sendSerialData('I' + str(var.I) + '%')
        
        #boton flecha arriba I
        button13 = Tk.Button(self, image=controller.Imagen8,bg='white', command=lambda:sumaI())
        button13['border']='0'
        button13.pack()
        CanvasM.create_window(725,100, window=button13)
        #boton flecha abajo I
        button14 = Tk.Button(self, image=controller.Imagen9,bg='white', command=lambda:restaI())
        button14['border']='0'
        button14.pack()
        CanvasM.create_window(725,122, window=button14)

        def sumaI():
            var.I=var.I+1
            Label4.config(text=var.I)
        def restaI():
            var.I=var.I-1
            Label4.config(text=var.I)

        #boton cargar D
        button15 = Tk.Button(self, image=controller.Imagen7,bg='white', command=lambda:send_D())
        button15['border']='0'
        button15.pack()
        CanvasM.create_window(768,160, window=button15)
        def send_D():
            controller.serialReference.sendSerialData('D' + str(var.D) + '%')
        #boton flecha arriba D
        button16 = Tk.Button(self, image=controller.Imagen8,bg='white', command=lambda:sumaD())
        button16['border']='0'
        button16.pack()
        CanvasM.create_window(725,150, window=button16)
        #boton flecha abajo D
        button17 = Tk.Button(self, image=controller.Imagen9,bg='white', command=lambda:restaD())
        button17['border']='0'
        button17.pack()
        CanvasM.create_window(725,172, window=button17)

        def sumaD():
            var.D=var.D+1
            Label5.config(text=var.D)
        def restaD():
            var.D=var.D-1
            Label5.config(text=var.D)

#LABELS
        #Franja de titulo
        Label1=Tk.Label(self, text='CONTROL AUTOMÁTICO',bg='#ED7D31',width=800,height=1,fg='white', font=('Helvetica',10,'bold'),borderwidth=1, relief='solid')
        Label1.pack()
        CanvasM.create_window(400,10, window=Label1)

    #VENTANA DE CONTROL
        
        #SetPoint Variador
        Label2=Tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=var.SP)
        Label2.pack()
        CanvasM.create_window(50,185, window=Label2)

    #VENTANA PID

        #variable proporcional
        Label3=Tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=var.P)
        Label3.pack()
        CanvasM.create_window(680,60, window=Label3)

        #variable integral
        Label4=Tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=var.I)
        Label4.pack()
        CanvasM.create_window(680,110, window=Label4)

        #variable derivativa
        Label5=Tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=var.D)
        Label5.pack()
        CanvasM.create_window(680,160, window=Label5)

    #EN IMAGEN
        
        #Frecuencia motor cisco
        Label6=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=var.LFV)
        Label6.pack()
        CanvasM.create_window(620,360, window=Label6)

        #Temp aire de entrada
        Label10=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=var.TE)
        Label10.pack()
        CanvasM.create_window(300,225, window=Label10)#Temp aire entrada
        
        #Temp gases de salida
        Label11=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=var.TG)
        Label11.pack()
        CanvasM.create_window(505,140, window=Label11)#Temp gases
        
        #Temp camara
        Label12=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=var.TC)
        Label12.pack()
        CanvasM.create_window(475,385, window=Label12)#Temp Camara
        
        #Temp Aire salida
        Label13=Tk.Label(self,bg='white',width=5,height=1, font=('Helvetica',10, 'bold'),fg='black', borderwidth=1, relief='solid', text=var.TS)
        Label13.pack()
        CanvasM.create_window(630,300, window=Label13)#Temp Aire Salda


#TEXTOS

    #VENTANA DE CONTROL

        #Encendido/Apagado Variador
        CanvasM.create_text(101,35, text="Encendido/Apagado Variador",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(100,35, text="Encendido/Apagado Variador",font=("Helvetica", 10), fill="black", width=500, justify="left")

        #Tipo de control
        CanvasM.create_text(61,95, text="Tipo de Control",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(60,95, text="Tipo de Control",font=("Helvetica", 10), fill="black", width=500, justify="left")
        
        #SetPoint temperatura
        CanvasM.create_text(76,155, text="SetPoint temperatura",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(75,155, text="SetPoint temperatura",font=("Helvetica", 10), fill="black", width=500, justify="left")
        CanvasM.create_text(90,185, text="ºC",font=("Helvetica", 10, 'bold'), fill="black", width=500, justify="left")

    #VENTANA DE PID

        #Variables PID
        CanvasM.create_text(701,30, text="Variables PID",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(700,30, text="Variables PID",font=("Helvetica", 10), fill="black", width=500, justify="left")
        #Proporcional P
        CanvasM.create_text(641,60, text="kp",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(640,60, text="kp",font=("Helvetica", 10), fill="black", width=500, justify="left")
        #Integral I
        CanvasM.create_text(641,110, text="ki",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(640,110, text="ki",font=("Helvetica", 10), fill="black", width=500, justify="left")
        #Derivativo D
        CanvasM.create_text(641,160, text="kd",font=("Helvetica", 10), fill="gray", width=500, justify="left")
        CanvasM.create_text(640,160, text="kd",font=("Helvetica", 10), fill="black", width=500, justify="left")

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
        CanvasM.create_line(0,210,220,210)
        CanvasM.create_line(220,210,220,0)
        CanvasM.create_line(1,211,220,211,fill='gray')
        CanvasM.create_line(221,210,221,0,fill='gray')

    #LINEAS PID
        CanvasM.create_line(630,0,630,190)
        CanvasM.create_line(630,190,800,190)  

        
        def refresh():

            Label10.config(text=controller.serialReference.getSerialData(1))
            Label11.config(text=controller.serialReference.getSerialData(2))
            Label12.config(text=controller.serialReference.getSerialData(3))
            Label13.config(text=controller.serialReference.getSerialData(4))
           
            self.after(500, refresh)

        refresh()
