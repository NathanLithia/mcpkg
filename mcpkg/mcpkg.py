import subprocess
import sys
import importlib.util
from tkinter.filedialog import askopenfilename
from tkinter import *

def compilepack():
    print("compile button pressed")

def selectpack():
    print("filedialog opened")
    filedialog.askopenfilename()

window = Tk()
window.geometry('325x100')
window.resizable(False, False)
window.title('MCPKG by NathanLithia')

w = Text(window, width = 35, height=1)
w.place(x = 20,y = 30)

selectbutton = Button(window, text = "Select MCPKG", command = selectpack, width = 15)
selectbutton.place(x = 175 ,y = 60)
compilebutton = Button(window, text = "Compile", command = compilepack, width = 15)
compilebutton.place(x = 30,y = 60)

window.mainloop()