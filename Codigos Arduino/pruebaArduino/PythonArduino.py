import serial
import time

arduino=serial.Serial('COM5', 9600)
time.sleep(2)

while 1:

    datoSerial=input()

    if datoSerial == '1':
        arduino.write(b'1')
        print("Led ON")

    elif datoSerial == '0':
        arduino.write(b'0')
        print("Led OFF")
