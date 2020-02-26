from tkinter import *

def teste_botao():
    print('botao pressionado')

    
janela = Tk()
janela.title('Teste Serial')
janela.geometry('500x500')

texto1 = Label(text='primeiro texto')
texto1.pack()

botao = Button(text='botao 01', command = teste_botao).pack()


janela.mainloop()
