from tkinter import *
from tkinter import ttk
root = Tk()
button = ttk.Button(root, text = "Click Me")
button.pack()
def callback():
    print("Clicked")


button.config(command = callback)
