import tkinter as Tk
from tkinter.ttk import Frame

import var

class PagInicio(Frame):
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


        #Botones toma de datos

        if var.tomarDatos == True:
            button3 = Tk.Button(self,image=controller.Imagen17, bg='white',command=lambda: iniciar()) # boton toma de datos
            button3['border']='0'
            button3.pack()
            Fondo2.create_window(70,350, window=button3)
            
            Label1=Tk.Label(self,bg='white',width=7,height=1, font=('Helvetica',10, 'bold'), text="Listo?")
            Label1.pack()
            Fondo2.create_window(165,370, window=Label1)
        
            button4 = Tk.Button(self,image=controller.Imagen18, bg='white',command=lambda: parar()) # boton detener toma de datos
            button4['border']='0'
            button4.pack()
            Fondo2.create_window(70,390, window=button4)

            button5 = Tk.Button(self,image=controller.Imagen19, bg='white',command=lambda: send_F()) # enviar frecuencia
            button5['border']='0'
            button5.pack()
            Fondo2.create_window(70,430, window=button5)

            self.entry1=Tk.Entry(self, width=5)
            self.entry1.insert(0, '1.0')
            self.entry1.pack()
            Fondo2.create_window(165,430, window=self.entry1)

        def send_F():
            controller.serialReference.sendSerialData('F' + self.entry1.get() + '%')
            var.MFV=self.entry1.get()
        
        def iniciar():
            controller.serialReference.sendSerialData('M')
            controller.serialReference.sendSerialData('E')
            controller.serialReference.sendSerialData('V')
            refresh()
        def parar():
            controller.serialReference.sendSerialData('M')
            controller.serialReference.sendSerialData('E')
            controller.serialReference.sendSerialData('V')
            controller.workbook.cerrarLibro()
            controller.destroy()
    
        def refresh():
            Label1.config(text=str(var.row))
            var.TE=controller.serialReference.getSerialData(1.1)
            var.TG=controller.serialReference.getSerialData(2.2)
            var.TC=controller.serialReference.getSerialData(3.3)
            var.TS=controller.serialReference.getSerialData(4.4)
            
            controller.workbook.worksheet.write(var.row, 0, var.TE) 
            controller.workbook.worksheet.write(var.row, 1, var.TG) 
            controller.workbook.worksheet.write(var.row, 2, var.TC) 
            controller.workbook.worksheet.write(var.row, 3, var.TS) 
            controller.workbook.worksheet.write(var.row, 4, var.MFV) #se escribe frecuencia en excel
            print(str(var.row),str(var.TE),str(var.TG),str(var.TC),str(var.TS),str(var.MFV),sep=" ",end="\n")
            controller.workbook.GrafValores(var.row)
            var.row +=1
            self.after(500, refresh)
            

