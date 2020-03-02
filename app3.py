
# importa dependencias do projetos

import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk

#-----------------------------------

# funcoes 

def selec_port():
    
    lbl_porta_selecionada_selec.configure(text=str(minha_porta.get()))


#---------------------------------------


# objeto lista de portas
comlist = serial.tools.list_ports.comports()
connected = []
for element in comlist:
    connected.append(element.device)

# ********** objetos tkinter ***************

# caracateristicas da janela
janela = tk.Tk()
janela.title('Teste Serial')
janela.geometry('500x300+100+100')


# labels
lbl_lista_portas = tk.Label(janela, text='Portas Disponiveis: ')
lbl_lista_portas.grid(column=0, row=1)

lbl_porta_selecionada_opt = tk.Label(janela, text='Porta Selecionada: ')
lbl_porta_selecionada_opt.grid(column=0, row=2)

lbl_porta_selecionada_selec = tk.Label(janela, text='...')
lbl_porta_selecionada_selec.grid(column=1, row=2)

btn_selecionar = tk.Button(janela, text='Selecionar Porta', command = selec_port)
btn_selecionar.grid(column=2, row=1)

# textos
txt_prt = tk.Text(janela)
txt_prt.insert(0, "ola....")
txt_prt.insert(1, "ooooo......")
txt_prt.pack()



# combos
minha_porta = tk.StringVar()
combo = ttk.Combobox(janela, width = 15, textvariable = minha_porta)
combo.grid(column=1, row=1)
combo['values'] = connected

# ************************************************************


janela.mainloop()
