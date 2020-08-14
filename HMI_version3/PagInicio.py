from Ventanas import Frame

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
