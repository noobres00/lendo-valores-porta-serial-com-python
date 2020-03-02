# -*- coding: cp1252 -*-
from tkinter import ttk
from tkinter import *
import serial.tools.list_ports
import tkinter as tk

def selec_port():
    txt_porta_selecionada_selec.configure(text=str(minha_porta.get()))
    inicial = 1
    ser = serial.Serial(combo.get(), 9600, timeout=1)
    print(ser.portstr)
    while inicial <= 2:
        c = ser.read(7)
        a = c.decode()
        print(a)
        inicial = inicial + 1
    txt_valor_peso["text"] = ('valor: ', a)

# objeto lista de portas
comlist = serial.tools.list_ports.comports()
connected = []
for element in comlist:
    connected.append(element.device)

# caracateristicas da janela
janela = tk.Tk()
janela.title('Teste Serial')
janela.geometry('500x300+100+100')
janela.configure(background='white')

#Imagem de logo
#imagem = tk.PhotoImage(file='kinross_logo.png') #nome do arquivo
#imagem = imagem.subsample(2,2)
#labelimagem = tk.Label(image=imagem, background='white')
#labelimagem.place(x=0, y=0, relwidth=1.0)

# textos
txt_lista_portas = tk.Label(janela, text='Portas Disponíveis: ', background='white', font='Arial 8 bold')
#txt_lista_portas.grid(column=0, row=80)
txt_lista_portas.place(x=70, y=80)

txt_porta_selecionada_opt = tk.Label(janela, text='Porta Selecionada: ', background='white', font='Arial 8 bold')
#txt_porta_selecionada_opt.grid(column=0, row=2)
txt_porta_selecionada_opt.place(x=70, y=110)

txt_porta_selecionada_selec = tk.Label(janela, text='...', background='white', font='Arial 8 bold')
#txt_porta_selecionada_selec.grid(column=1, row=2)
txt_porta_selecionada_selec.place(x=240, y=110)

txt_valor_peso = tk.Label(janela, text='', background='white', font='Arial 8 bold')
txt_valor_peso.place(x=270, y=150)

btn_selecionar = tk.Button(janela, text='Selecionar Porta', command=selec_port, background='white', font='Arial 8 bold')
#btn_selecionar.grid(column=2, row=1)
btn_selecionar.place(x=320, y=80)

# combos
minha_porta = tk.StringVar()
combo = ttk.Combobox(janela, width=15, textvariable=minha_porta)
#combo.grid(column=1, row=1)
combo.place(x=195, y=80)
combo['values'] = connected
a = str(connected)
print(minha_porta)
janela.mainloop()
