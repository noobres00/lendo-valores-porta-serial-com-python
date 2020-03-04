import tkinter as tk
import tkinter
from tkinter.ttk import *
import serial.tools.list_ports
import requests
from time import sleep

inicia_contagem = True

# objeto lista de portas
comlist = serial.tools.list_ports.comports()
portas = []
for element in comlist:
    portas.append(element.device)

def checaPorta():
    inicia_contagem = False
    lbl_prt.configure(text = port_selec.get())
    porta_selecionada = port_selec.get()

    url = 'http://localhost:1880/python'
    myobj = {'porta_seleciona': porta_selecionada}

    requests.post(url, data = myobj)

    #print(x.text)


principal = tk.Tk() 
principal.geometry('500x300+100+100')
principal.title('Leitura Porta Serial')

#labels
lbl_prt_dis = tk.Label(principal, text = 'Portas Disponiveis: ', font = 8)
lbl_prt_dis.grid(column = 0, row = 0)

lbl_prt_sel = tk.Label(principal, text = 'Porta Selecionada: ', font = 8)
lbl_prt_sel.grid(column = 0, row = 1)

lbl_prt = tk.Label(principal, text = '...', font = 8)
lbl_prt.grid(column = 1, row = 1)

port_selec = tk.StringVar()
cbb = Combobox(principal, textvariable = port_selec)
cbb.grid(column = 1, row =0)
cbb['values'] = portas

btn1 = tk.Button(principal, text = 'Selecionar Porta', command = checaPorta, font = 8)
btn1.grid(column = 0, row = 2)

#btn2 = tk.Button(principal, text = 'Pa', command = conta, font = 8)
#btn2.grid(column = 0, row = 3)

#lbl_link = tk.Label(principal, text = 'Link: ', font = 8)
#lbl_link.grid(column = 0, row = 3)
#
#txt = Entry(principal,width=50)
#txt.grid(column = 1, row = 3)


principal.mainloop() 

inicia_contagem = True
while inicia_contagem:

    print('contando')
    sleep(10)