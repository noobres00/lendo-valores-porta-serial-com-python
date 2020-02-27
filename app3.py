import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk



comlist = serial.tools.list_ports.comports()
connected = []

janela = tk.Tk()

janela.title('Teste Serial')
janela.geometry('200x100+100+100')

texto = tk.Label(janela, text='Hoje')
texto.grid(column=0, row=0)

combo = ttk.Combobox(janela)

for element in comlist:
    connected.append(element.device)

combo['values'] = connected

combo.grid(column=0, row=1)
#combo.current(1)

janela.mainloop()

