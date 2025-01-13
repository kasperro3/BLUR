import time
import serial

serialPort = serial.Serial("COM4", 9600, 8, "N",1,1)

while 1:
    data = serialPort.readline()
    print(data.decode('utf-8').removesuffix("\n"))
    serialPort.write("DataFromPC".encode('utf-8'))
    
    time.sleep(2)






