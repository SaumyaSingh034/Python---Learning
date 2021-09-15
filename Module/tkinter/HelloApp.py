from tkinter import *;
from tkinter import ttk

class HelloApp:
    def __init__(self,master):

        self.label = ttk.Label(master, text = "Hello, Tkinter!")
        self.label.grid(row = 0, column = 0, columnspan = 2)

        ttk.Button(master,text = "Texas",
                   command = self.texas_hello).grid(row = 1, column = 0)

        ttk.Button(master, text = "Huwaiiee",
                   command = self.huwaiiee_hello).grid(row = 1, column = 1)


    def texas_hello(self):
        self.label.config(text = "Texas Hello")

    def huwaiiee_hello(self):
        self.label.config(text = "Huwaiiee Hello")

def main():
    root = Tk();
    app = HelloApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
        
