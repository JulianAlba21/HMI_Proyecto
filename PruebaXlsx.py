from threading import Thread
import serial
import time
import collections
import struct
import copy
import tkinter as Tk
from tkinter.ttk import Frame

import xlsxwriter

val1=0
val2=0
val3=0
val4=0
frec=0

row=1

class ventana(Frame):
    def __init__(self, master, Serial, worksheet):
        
        Frame.__init__(self,master)
        self.master=master
        self.serial=Serial
        self.worksheet=worksheet
        self.master.title('recolección')
        frame1= Frame(self.master)
        frame1.pack(side=Tk.RIGHT)
        
        Button1=Tk.Button(frame1, text='Empezar Toma de Datos', command = lambda: cargar())
        Button1.grid(row=0, column=0, padx=5, pady=5)
        Label1=Tk.Label(frame1,text='Listo?')
        Label1.grid(row=1, column=0, padx=5, pady=5)

        Button2=Tk.Button(frame1, text='Enviar PWM a variador', command = lambda: send_PWM())
        Button2.grid(row=2, column=0, padx=5, pady=5)
        self.entry1=Tk.Entry(frame1, width=5)
        self.entry1.insert(0, '1.0')
        self.entry1.grid(row=3, column=0, padx=5, pady=5)

        def send_PWM():
            self.serial.sendSerialData('F' + self.entry1.get() + '%')
            global frec

            frec=self.entry1.get()
            
            print('se envio valor = '+ self.entry1.get())
        

        def cargar():
            self.serial.sendSerialData('M')
            self.serial.sendSerialData('E')
            refresh()
    
        def refresh():

            global val1
            global val2
            global val3
            global val4
            global frec
            global row

            Label1.config(text=str(row))          

            self.serial.getSerialData()
            self.worksheet.write(row, 0, val1) #se escribe valor 1 en excel
            self.worksheet.write(row, 1, val2) #se escribe valor 2 en excel
            self.worksheet.write(row, 2, val3) #se escribe valor 3 en excel
            self.worksheet.write(row, 3, val4) #se escribe valor 4 en excel
            self.worksheet.write(row, 4, frec) #se escribe frecuencia en excel

            row +=1
            
            self.master.after(100, refresh)

            
        
class ConexionSerial:
    def __init__(self, serialPort='COM10', serialBaud=38400, DataNumBytes=4, NumIn=4):
        self.port= serialPort
        self.baud = serialBaud
        self.dataNumBytes= DataNumBytes
        self.numIn=NumIn
        self.rawData= bytearray(self.numIn*self.dataNumBytes)
        self.dataType = 'f'
        self.thread = None
        self.isRun= True
        self.isReceiving=False
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

    def backGroundThread(self):
        time.sleep(1.0)
        self.serialConnection.reset_input_buffer()
        while (self.isRun):
            self.serialConnection.readinto(self.rawData)
            self.isReceiving = True

    def sendSerialData(self, data):
        self.serialConnection.write(data.encode('utf-8'))

    def close(self):
        self.isRun = False
        self.thread.join()
        self.serialConnection.close()
        print('Disconnected...')

    def getSerialData(self):
        privateData= copy.deepcopy(self.rawData[:])
        for i in range(self.numIn):
            data =privateData[(i*self.dataNumBytes):(self.dataNumBytes+i*self.dataNumBytes)]
            value, = struct.unpack('f', data)
            self.data[i].append(value)
        valor1=list(self.data[0])
        valor2=list(self.data[1])
        valor3=list(self.data[2])
        valor4=list(self.data[3])

        global val1
        global val2
        global val3
        global val4
        global frec
        
        val1=valor1[0]
        val2=valor2[0]
        val3=valor3[0]
        val4=valor4[0]

        print(str(val1) + ' ' + str(val2) + ' ' + str(val3) + ' ' + str(val4)+ ' '+ str(frec))
     

def main():

    portName='COM10'
    baudRate=57600
    dataNumBytes = 4
    NumIn=4
    s=ConexionSerial(portName, baudRate, dataNumBytes, NumIn)
    s.readSerialStart()

    workbook= xlsxwriter.Workbook('Datos.xlsx')
    worksheet=workbook.add_worksheet()
    worksheet.set_column('G:G',60)
    worksheet.set_zoom(150)

    worksheet.write_string('A1', 'Valor1') #se escribe w valor 1 en excel
    worksheet.write_string('B1', 'Valor2') #se escribe w valor 2 en excel
    worksheet.write_string('C1', 'Valor3') #se escribe w valor 3 en excel
    worksheet.write_string('D1', 'Valor4') #se escribe w valor 4 en excel
    worksheet.write_string('E1', 'Frecuencia') #se escribe w Freceuncia en excel
    worksheet.write_string('F1', 'Val1') #se escribe valor 1 en excel
    worksheet.write_string('F2', 'Val2') #se escribe valor 2 en excel
    worksheet.write_string('F3', 'Val3') #se escribe valor 3 en excel
    worksheet.write_string('F4', 'Val4') #se escribe valor 4 en excel
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
    worksheet.write_string('F5', 'Frec') #se escribe Frecuencia en excel
=======
>>>>>>> master
>>>>>>> Stashed changes

    root=Tk.Tk()
    app=ventana(root, s, worksheet)
    root.mainloop()

    global row

    worksheet.add_sparkline('G1',{'range':'Sheet1!A1:A'+str(row), 'series_color':'#00FEF2'})
    worksheet.add_sparkline('G2',{'range':'Sheet1!B1:B'+str(row), 'series_color':'#FCF103'})
    worksheet.add_sparkline('G3',{'range':'Sheet1!C1:C'+str(row), 'series_color':'#FF0000'})
    worksheet.add_sparkline('G4',{'range':'Sheet1!D1:D'+str(row), 'series_color':'#5A1280'})
    worksheet.add_sparkline('G5',{'range':'Sheet1!E1:E'+str(row), 'series_color':'#5A1280'})
    
    workbook.close()
    s.close
    

    
if __name__=='__main__':
    main()
