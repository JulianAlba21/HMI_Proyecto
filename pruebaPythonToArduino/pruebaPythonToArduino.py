from threading import Thread
import serial
import re
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import struct
import copy
import tkinter as Tk
from tkinter.ttk import Frame
import pandas as pd

class serialPlot:
    def __init__(self, serialPort = 'COM5', serialBaud = 38400):
        self.port = serialPort
        self.baud = serialBaud

        self.rawData= bytearray(4*2)
        self.isRun = True
        self.isReceiving = False
        self.thread = None
        self.dataType = 'f'
        self.data=[]

        self.lines = []

        for i in range(2):
            self.data.append(collections.deque([0]*1, maxlen=1))
         
        print('Trying to connect to: ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
        try:
            self.serialConnection = serial.Serial(serialPort, serialBaud, timeout=2)
            print('Connected to ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
        except:
            print("Failed to connect with " + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')

    def sendSerialData(self, data):
        self.serialConnection.write(data.encode('utf-8'))

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
            
                       
    def getSerialData(self, g=0):
        privateData= copy.deepcopy(self.rawData[:])
        for i in range(2):
            data =privateData[(i*4):(4+i*4)]
            value, = struct.unpack('f', data)
            self.data[i].append(value)
        valor1=list(self.data[0])
        valor2=list(self.data[1])
        valor1=valor1[0]
        valor2=valor2[0]

        if g == 1:
            return valor1
        if g == 2:
            return valor2

    def close(self):
        self.isRun = False
        self.thread.join()
        self.serialConnection.close()
        print('Disconnected...')

class window(Frame):
    def __init__(self, master, SerialReference):
        Frame.__init__(self, master)
        self.entry=None
        self.master=master
        self.serialReference=SerialReference
        self.initWindow()

    def initWindow(self):
        self.master.title("prueba")
        frame1= Frame(self.master)
        frame1.pack(side=Tk.RIGHT)

        #valor 1

        lbl1=Tk.Label(frame1, text="valor1")
        lbl1.grid(row=0,column=0, sticky=Tk.W, padx=5, pady=5)
        self.entry1 =Tk.Entry(frame1, width=5)
        self.entry1.insert(1,'1.0')
        self.entry1.grid(row=0, column=1, padx=5, pady=5)
        SendButton1 = Tk.Button(frame1, text='Set valor1', command=self.sendKpToMCU, width=7)
        SendButton1.grid(row=0, column=2, padx=5, pady=5)

        lbl2=Tk.Label(frame1, text="R_v1")
        lbl2.grid(row=1,column=0, sticky=Tk.W, padx=5, pady=5)
        self.Lbl3=Tk.Label(frame1, width=5, bg='white', text=str(self.serialReference.getSerialData(1)))
        self.Lbl3.grid(row=1, column=1, padx=5, pady=5)
        SendButton2 = Tk.Button(frame1, text='obt valor1', command=self.showKP, width=7)
        SendButton2.grid(row=1, column=2, padx=5, pady=5)

        #valor 2

        lbl4=Tk.Label(frame1, text="valor2")
        lbl4.grid(row=2,column=0, sticky=Tk.W, padx=5, pady=5)
        self.entry2 =Tk.Entry(frame1, width=5)
        self.entry2.insert(1,'1.0')
        self.entry2.grid(row=2, column=1, padx=5, pady=5)
        SendButton1 = Tk.Button(frame1, text='Set valor2', command=self.sendV2ToMCU, width=7)
        SendButton1.grid(row=2, column=2, padx=5, pady=5)

        lbl5=Tk.Label(frame1, text="R_v2")
        lbl5.grid(row=3,column=0, sticky=Tk.W, padx=5, pady=5)
        self.Lbl6=Tk.Label(frame1, width=5, bg='white', text=str(self.serialReference.getSerialData(2)))
        self.Lbl6.grid(row=3, column=1, padx=5, pady=5)
        SendButton2 = Tk.Button(frame1, text='obt valor2', command=self.showV2, width=7)
        SendButton2.grid(row=3, column=2, padx=5, pady=5)

    def sendKpToMCU(self):
        self.serialReference.sendSerialData('K' + self.entry1.get() + '%')     # '%' is our ending marker
        print('enviado valor1')

    def sendV2ToMCU(self):
        self.serialReference.sendSerialData('S' + self.entry2.get() + '%')     # '%' is our ending marker
        print('enviado valor2')
        
    def showKP(self):
        self.Lbl3.config(text=str(self.serialReference.getSerialData(1)))

    def showV2(self):
        self.Lbl6.config(text=str(self.serialReference.getSerialData(2)))
        
def main():

    portName='COM5'
    baudRate= 38400
    s=serialPlot(portName, baudRate)
    s.readSerialStart()

    root=Tk.Tk()
    app=window(root, s)

    root.mainloop()
    s.close()

if __name__=='__main__':
    main()
    
