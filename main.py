import tkinter as tk
from tkinter import ttk
from modelo import AppBd

class PrincipalBD():
    def __init__(self, win):
        self.appBd = AppBd()
        self.janela = win
        self.treeProdutos = ttk.Treeview(self.janela, columns =("Codigo do produto", "Nome", "Preço"))
        self.treeProdutos.heading("Codigo do produto", text="id ")
        self.treeProdutos.heading("Nome", text="Nome ")
        self.treeProdutos.heading("Preço", text="Preço ")
        self.treeProdutos.pack()

        self.treeProdutos.column("#0", width=1)
        self.treeProdutos.column("#1", width=200)
        self.treeProdutos.column("#2", width=200)
        self.treeProdutos.column("#3", width=200)
    
        self.nome = tk.Label(self.janela, text='Nome: ')
        self.nome.pack()
        self.entry_nome = tk.Entry(self.janela)
        self.entry_nome.pack()

        self.preco = tk.Label(self.janela, text='Preço: ')
        self.preco.pack()
        self.entry_preco = tk.Entry(self.janela)
        self.entry_preco.pack()

        self.btn_cadastrar = tk.Button(self.janela, text='Cadastrar', command= self.cadastrarProduto)
        self.btn_cadastrar.pack()

        self.btn_deletar = tk.Button(self.janela, text='Deletar')
        self.btn_deletar.pack()

        self.btn_atualizar = tk.Button(self.janela, text='Atualizar')
        self.btn_atualizar.pack()


        win.configure(background='pink')

    def cadastrarProduto(self):
        nome = self.entry_nome.get()
        preco = float(self.entry_preco.get())
        self.appBd.inserirdados(nome, preco)

janela = tk.Tk()
PrincipalBD(janela)

janela.title("Bem vindo a janela principal")
janela.geometry("900x700")
janela.mainloop()


