from tkinter import ttk

bgColor = '#1c1c1c'
bgAccentColor = '#3d3c3c'
redStateColor = '#b03737'
greenStateColor = ''
blueStateColor = ''

def appStyle(root) -> ttk.Style:
    style = ttk.Style(root)

    # TFrame
    style.configure('TFrame', background=bgColor, foreground='white')

    # TLabel
    style.configure('TLabel', background=bgColor, foreground='white', padding='5')
    # state
    style.configure('stateLabel.TLabel', relief='ridge', padding=10, font=('Helvetica', 20, 'bold'), background=redStateColor,  anchor='center')
    style.configure('sectionLabel.TLabel', font=('Segoe UI', 10, 'bold'), anchor='center')

    # TButton
    style.configure('TButton', background=bgColor)

    # Canvas
    style.configure('Canvas', bg=bgColor)


    return style