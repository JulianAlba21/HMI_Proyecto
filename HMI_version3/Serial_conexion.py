from threading import Thread
import serial
import collections
import struct
import copy
import ctypes
import urllib
import json
import pandas as pd

import time

import var

class ConexionSerial():
    def __init__(self, serialPort = 'COM3', serialBaud = 38400, DataNumBytes=4, NumIn=4):
        self.port = serialPort
        self.baud = serialBaud
        self.dataNumBytes=DataNumBytes
        self.numIn=NumIn
        
        self.rawData= bytearray(self.numIn*self.dataNumBytes)
        self.isRun = True
        self.isReceiving = False
        self.thread = None
        if self.dataNumBytes == 2:
            self.dataType = 'h'     # 2 byte integer
        elif self.dataNumBytes == 4:
            self.dataType = 'f'     # 4 byte float
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
                time.sleep(0.5)           #espere tantos segundos    

    def getSerialData(self, g=0):
        privateData= copy.deepcopy(self.rawData[:])
        for i in range(self.numIn):
            data =privateData[(i*self.dataNumBytes):(self.dataNumBytes+i*self.dataNumBytes)]
            value, = struct.unpack(self.dataType, data)
            self.data[i].append(value)
        var.LTE=list(self.data[0])
        var.LTG=list(self.data[1])
        var.LTC=list(self.data[2])
        var.LTS=list(self.data[3])
        
        var.LTE=var.LTE[0]
        var.LTG=var.LTG[0]
        var.LTC=var.LTC[0]
        var.LTS=var.LTS[0]

        if g == 1:
            return int(var.LTE)
        if g == 2:
            return int(var.LTG)
        if g == 3:
            return int(var.LTC)
        if g == 4:
            return int(var.LTS)

        #envio de valores a excel

        if g == 1.1:
            return var.LTE
        if g == 2.2:
            return var.LTG
        if g == 3.3:
            return var.LTC
        if g == 4.4:
            return var.LTS
                   
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
