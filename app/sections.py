import tkinter as tk
from tkinter import ttk
import Controller

class Section():
    def __init__(self, root: tk.Tk, controller: Controller, column: int, row: int):
        self.controller = controller
        self.frame = ttk.Frame(root)
        self.frame.grid(column=column, row=row, padx=10, pady=10)
        self.frame['relief'] = 'ridge'
        self.layout(self.frame)
        

class Connection(Section):
    def layout(self, frame: ttk.Frame):
        frame.columnconfigure(3)
        frame.rowconfigure(3)

        comLabel = ttk.Label(frame, text="BLUETOOTH CONNECTION", style='sectionLabel.TLabel')
        comLabel.grid(column=0, row=0, columnspan=2, padx=10)
        comNumber = tk.IntVar(value=4)
        comSelect = ttk.Entry(frame, textvariable=comNumber, width=10)
        comSelect.grid(column=0, row=1, padx=(10,0))
    
        connectButton = ttk.Button(frame, text="Connect",  
                                   command=lambda:self.controller.Connect(comNumber.get()))
        connectButton.grid(column=1, row=1, padx= 10, pady=10)
        comStatusLabel = ttk.Label(frame, textvariable=self.controller.connectionStatus)
        comStatusLabel.grid(column=0, row=2, columnspan=2, pady=(0,5))


class State(Section):
    def layout(self, frame: ttk.Frame):
        frame.rowconfigure(3)
        frame.columnconfigure(1)

        headerLabel = ttk.Label(frame, text="STATE", style='sectionLabel.TLabel')
        headerLabel.grid(column=0, row=0, padx=10)

        stateLabel = ttk.Label(frame, width=12 , textvariable=self.controller.state, style='stateLabel.TLabel', anchor='center')
        stateLabel.grid(column=0, row=1, padx=10)

        telemetryFrame = ttk.Frame(frame, width=stateLabel.winfo_width(), height=20)
        telemetryFrame.columnconfigure(3)
        telemetryFrame.rowconfigure(2)
        telemetryFrame.grid(column=0, row=2)

        line = tk.Canvas(telemetryFrame, width=1, height=150)
        line.grid(column=1, row = 0, rowspan=5)

        battVoltageLabel = ttk.Label(telemetryFrame, textvariable=self.controller.battVoltageLabel)
        battVoltageLabel.grid(column=0, row=0)

        throttleLabel = ttk.Label(telemetryFrame, textvariable=self.controller.throttleLabel)
        throttleLabel.grid(column=2, row=0)

        speedLabel = ttk.Label(telemetryFrame,  textvariable=self.controller.speedLabel)
        speedLabel.grid(column=0, row=1) 

        distanceLabel = ttk.Label(telemetryFrame, textvariable=self.controller.distanceLabel)
        distanceLabel.grid(column=2, row=1)

        accXLabel = ttk.Label(telemetryFrame, text="Acc X:")
        accXLabel.grid(column=0, row=2)

        accYLabel = ttk.Label(telemetryFrame, text="Acc Y:")
        accYLabel.grid(column=2, row=2)

        accZLabel = ttk.Label(telemetryFrame, text="Acc Z:")
        accZLabel.grid(column=0, row=3)

        gyroZLabel = ttk.Label(telemetryFrame, text="Gyro Z:")
        gyroZLabel.grid(column=2, row=3)

        gyroXLabel = ttk.Label(telemetryFrame, text="Gyro X:")
        gyroXLabel.grid(column=0, row=4)

        gyroYLabel = ttk.Label(telemetryFrame, text="Gyro Y:")
        gyroYLabel.grid(column=2, row=4)