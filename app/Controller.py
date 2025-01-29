import bluetooth
import serial
import tkinter as tk

class Controler():
    def __init__(self):
        self.connectionStatus = tk.StringVar(value="Initiate connection")
        self.isConnected = False
        self.state = tk.StringVar(value="Armed")
        self.battVoltageLabel = tk.StringVar(value="Voltage: ")
        self.speedLabel = tk.StringVar(value="Speed: ")
        self.distanceLabel = tk.StringVar(value="Distnace: ")
        self.throttleLabel = tk.StringVar(value="Throttle: ")

    
    # Connecting to bluetooth device
    # Devices need to be paired first (use pairBluetooth.py)
    def Connect(self, comNumber:int) -> int:
        self.connectionStatus.set("Initiated")
        try:
            self.__serialPort = serial.Serial("COM" + str(comNumber), 9600, 8, "N", 1, 1)
        except:
            self.connectionStatus.set("Can't open COM" + str(comNumber))
            return 1
        
        self.connectionStatus.set("Connected to COM" + str(comNumber))
        self.isConnected = True
        return 0
    
    
    # can be run on close and on demand
    def Disconnect(self) -> int:
        if self.__serialPort.is_open:
            try:
                self.__serialPort.close()
            except:
                self.connectionStatus.set("Disconnect failure")
                return 1
            
            self.isConnected = False
            self.connectionStatus.set("Initiate connection")
            return 0


def BluetoothSearch() -> list[list[str,str]]:
    return bluetooth.discover_devices(lookup_names=True)