from tkinter import *

def teste_botao():
    print('botao pressionado')

    
janela = Tk()
janela.title('Teste Serial')
janela.geometry('500x500')

texto1 = Label(text='primeiro texto')
texto1.pack()

texto2 = Label(text='segundo texto')
texto2.pack()

botao1 = Button(text='botao 01', command = teste_botao).pack()
botao2 = Button(text='botao 02', command = teste_botao).pack()


janela.mainloop()
