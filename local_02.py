import tkinter as tk
from tkinter import ttk
 
 
 
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self) 
        self.title("Tkinter Label Frame")
        self.minsize(600,400)
 
 
        self.labelFrame = ttk.LabelFrame(self, text = "Label Frame")
        self.labelFrame.grid(column = 0, row = 7, padx = 20, pady = 40)
 
 
        self.labels()
 
 
 
    def labels(self):
        ttk.Label(self.labelFrame, text = "Label One" ).grid(column = 0, row = 0, sticky = tk.W)
        ttk.Label(self.labelFrame, text = "Label Two").grid(column = 0, row = 1,sticky = tk.W)
        ttk.Label(self.labelFrame, text = "Label Three").grid(column = 0, row = 2, sticky = tk.W)
 
 
app = App()
app.mainloop()
