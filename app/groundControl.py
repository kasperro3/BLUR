import tkinter as tk
from tkinter import ttk
import actions

class GroundControl():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BLUR Ground Control")
        self.root.minsize(520, 350)
        s = ttk.Style(self.root)
        s.theme_use("winnative")
        self.layout()


    def layout(self):
        mainframe = ttk.Frame(self.root)
        mainframe.columnconfigure(3)
        mainframe.rowconfigure(3)
        
        headerLabel = ttk.Label(mainframe, text="BLUR GROUND CONTROL")
        headerLabel.configure(background='green')
        headerLabel.grid(column=0, row=0, columnspan=3)

        forwardButton = ttk.Button(mainframe, text='Forward', command=actions.Forward)
        forwardButton.grid(column=1, row = 1)

        mainframe.grid(column=0, row=0)
        

    def mainloop(self):
        self.root.mainloop()