import tkinter as tk
from tkinter import ttk
import Controller
from sections import *
from appStyle import *

# theme
import sv_ttk
class GroundControl():
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg='#1c1c1c')
        self.root.title("BLUR Ground Control")
        self.root.minsize(480, 350)
        # sv_ttk.set_theme('dark', self.root)
        appStyle(self.root)
        

        self.controller = Controller.Controler()
        self.layout()


    def layout(self):
        mainframe = ttk.Frame(self.root,style='main.TFrame')
        mainframe.columnconfigure(3)
        mainframe.rowconfigure(3)
        mainframe.grid(column=0, row=0)
        
        headerLabel = ttk.Label(mainframe, text="BLUR GROUND CONTROL", anchor='center')
        headerLabel.configure(font=('Segoe UI', 20, 'bold'))
        headerLabel.grid(column=0, row=0, columnspan=3)

        # COM PORT CONNECTION AREA
        Connection(mainframe, self.controller, 1, 1)

        # STATE WINDOW WITH CRITICAL TELEMETRY
        State(mainframe, self.controller, 0, 1)


    def mainloop(self):
        self.root.mainloop()