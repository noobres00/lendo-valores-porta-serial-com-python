# -*- coding: cp1252 -*-
import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk

#class app(tk.Tk()


def selec_port():
    
    txt_porta_selecionada_selec.configure(text=str(minha_porta.get()))
    

# objeto lista de portas
comlist = serial.tools.list_ports.comports()
connected = []
for element in comlist:
    connected.append(element.device)




# caracateristicas da janela
janela = tk.Tk()
janela.title('Teste Serial')
janela.geometry('500x300+100+100')

# textos
txt_lista_portas = tk.Label(janela, text='Portas Disponíveis: ')
txt_lista_portas.grid(column=0, row=1)

txt_porta_selecionada_opt = tk.Label(janela, text='Porta Selecionada: ')
txt_porta_selecionada_opt.grid(column=0, row=2)

txt_porta_selecionada_selec = tk.Label(janela, text='...')
txt_porta_selecionada_selec.grid(column=1, row=2)

btn_selecionar = tk.Button(janela, text='Selecionar Porta', command = selec_port)
btn_selecionar.grid(column=2, row=1)




# combos
minha_porta = tk.StringVar()
combo = ttk.Combobox(janela, width = 15, textvariable = minha_porta)
combo.grid(column=1, row=1)
combo['values'] = connected



janela.mainloop()
