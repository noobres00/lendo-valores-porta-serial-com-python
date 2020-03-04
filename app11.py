#TI Industrial
#Kinross Paracatu
#Denis Nobre / Misael Silva
#2020
#--------------------------------

from tkinter import ttk
import tkinter as tk
import threading
from tkinter import *
import serial.tools.list_ports
from mettler_toledo_device import MettlerToledoDevice
import requests
from websocket import create_connection

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.janela.quit()

    def run(self):
        self.janela = tk.Tk()
        self.janela.protocol("WM_DELETE_WINDOW", self.callback)
        self.janela.title('Leitura Dados Balança - Kinross Paracatu')
        self.janela.geometry('500x350+100+100')
        self.janela.configure(background='#fff')
        self.janela.resizable(0,0)
        self.AddWidgets()
        self.janela.mainloop()

    def enviaDados(self):
        
        #local de destino de envio dos dados
        url = 'http://ptu-autcp-01:8080/recebePeso'
        #formata a mensagem
        myobj = {'peso': self.txt_label_peso['text'], 'barra': self.txt_label_numero_barra['text']}

        #envia dados
        requests.post(url, data = myobj)

        #desabilita botao enviar valores
        self.enviarValor['state'] = 'disabled'
        #habilita botao para gerar numero da barra
        self.gerarNumero['state'] = 'normal'
        #limpa texto numero da barra
        self.txt_label_numero_barra['text'] = ''

    def geraNumero(self):

        #cria conexao com o webservice
        ws = create_connection("ws://localhost:1880/ws/teste")
        #envia comando para o webservice entender o que esta sendo requisitado
        ws.send("gera_numero")
        #recebe o numero da ultima barra e adiciona um
        result =  int(ws.recv()) + 1
        #encerra conexao com o webservice
        ws.close()
        #escreve o valor do numero novo da barra para o usuario

        #tem que verificar, nao ficou legal
        self.txt_label_numero_barra['text'] = (result)
        if self.txt_label_numero_barra['text'] == result:
            self.enviarValor['state'] = 'normal'

        self.gerarNumero['state'] = 'disabled'



    def AddWidgets(self):
        self.TopFrame = Frame(self.janela, background='#cdad00', width=500, height=10, bd=5, relief='flat')
        self.TopFrame.place(x=0, y=0)

        self.Topfram2 = Frame(self.janela, background='#cdad00', width=10, height=500, bd=5, relief='flat')
        self.Topfram2.place(x=0, y=0)

        self.Topfram3 = Frame(self.janela, background='#cdad00', width=10, height=500, bd=5, relief='flat')
        self.Topfram3.place(x=490, y=0)

        self.Topfram4 = Frame(self.janela, background='#cdad00', width=500, height=10, bd=5, relief='flat')
        self.Topfram4.place(x=0, y=340)

        self.imagem = tk.PhotoImage(file='kinross_logo.png')  # nome do arquivo
        self.imagem = self.imagem.subsample(2, 2)

        self.labelimagem = tk.Label(image=self.imagem, bd=0 ,relief='flat')
        self.labelimagem.place(x=120, y=20)

        #LABELS
        self.txt_label_peso = tk.Label(self.janela, text='...', background='white', font='Arial 18 bold')
        self.txt_label_peso.place(x=180, y=150)

        self.txt_label_numero_barra = tk.Label(self.janela, text='...', background='white', font='Arial 18 bold')
        self.txt_label_numero_barra.place(x=180, y=200)

        self.txt_label_portas = tk.Label(self.janela, text = 'Portas Disponíveis: ', background = 'white', font = 'Arial 8 bold')
        self.txt_label_portas.place(x = 45, y = 100)

        self.txt_porta_selecionada_opt = tk.Label(self.janela, text='Porta Selecionada: ', background='white',
                                             font='Arial 8 bold')
        self.txt_porta_selecionada_opt.place(x=150, y=350)

        self.txt_porta_selecionada_selec = tk.Label(self.janela, text='...', background='white', font='Arial 8 bold')

        self.txt_porta_selecionada_selec.place(x=270, y=350)

        #BUTTONS
        self.ObterValor = Button(self.janela, text='Obter Peso', width=9, height=1, bd=5, relief='flat', background='#cdad00',
                                 activebackground='#8b7500', activeforeground='#8b7500', foreground='#000', command=self.Obter)
        self.ObterValor.place(x=45, y=150)

        self.gerarNumero = Button(self.janela, text='Gerar Numero', width=9, height=1, bd=5, relief='flat', background='#cdad00', 
                                 activebackground='#8b7500', activeforeground='#8b7500', foreground='#000', command=self.geraNumero)
        self.gerarNumero.place(x=45, y=200)

        self.enviarValor = Button(self.janela, text='Enviar Peso', width=9, height=1, bd=5, relief='flat', background='#cdad00', state = DISABLED,
                                 activebackground='#8b7500', activeforeground='#8b7500', foreground='#000', command=self.enviaDados)
        self.enviarValor.place(x=45, y=250)

        self.btn_obter = tk.Button(self.janela, text='Conectar', width=8, height=1, bd=5, relief='flat', background='#cdad00',
                                   activebackground='#8b7500', activeforeground='#8b7500', foreground='#000', command=self.selec_port)
        self.btn_obter.place(x=330, y=90)


        self.comlist = serial.tools.list_ports.comports()
        self.connected = []
        for element in self.comlist:
            self.connected.append(element.device)
        self.minha_porta = tk.StringVar()
        self.combo = ttk.Combobox(self.janela, width=15, textvariable=self.minha_porta, background='white', font='Arial 8 bold')
        self.combo.place(x=180, y=100)
        self.combo['values'] = self.connected

    def selec_port(self):

        self.txt_porta_selecionada_selec.configure(text=str(self.minha_porta.get()))
        self.txt_porta_selecionada_selec['text']= self.combo.get()
        #self.ser = serial.Serial(self.combo.get(), 9600, timeout=1)
        self.dev = MettlerToledoDevice(port=self.combo.get()) # Windows specific port

    def Obter(self):

        self.txt_label_peso['text'] = self.dev.get_weight_stable()

app = App()




