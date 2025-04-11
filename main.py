import tkinter as tk
from tkinter import ttk
from modelo import AppBd

class PrincipalBD():
    def __init__(self, win):
        self.appBd = AppBd()
        self.janela = win
        self.config()
        self.mostrarProdutos()

    def config(self):
        

        self.treeProdutos = ttk.Treeview(self.janela, columns =("Codigo do produto", "Nome", "Preço"))
        self.treeProdutos.heading("Codigo do produto", text="id ")
        self.treeProdutos.heading("Nome", text="Nome ")
        self.treeProdutos.heading("Preço", text="Preço ")
        self.treeProdutos.pack()

        self.treeProdutos.column("#0", width=1)
        self.treeProdutos.column("#1", width=200)
        self.treeProdutos.column("#2", width=200)
        self.treeProdutos.column("#3", width=200)
        self.treeProdutos.bind("<Double-1>", self.onDoubleClick)

       
    
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

        self.btn_deletar = tk.Button(self.janela, text='Deletar',command= self.deletarProduto)
        self.btn_deletar.pack()

        self.btn_atualizar = tk.Button(self.janela, text='Atualizar', command= self.atualizarProduto)
        self.btn_atualizar.pack()

        self.btn_limpar = tk.Button(self.janela, text='Limpar', command=self.limparTela)
        self.btn_limpar.pack()

        self.btn_buscar = tk.Button(self.janela, text='Buscar', command=self.buscarProduto)
        self.btn_buscar.pack()


        self.janela.configure(background='pink')

    def cadastrarProduto(self):
        nome = self.entry_nome.get()
        preco = float(self.entry_preco.get())
        self.appBd.inserirdados(nome, preco)
        self.limparTela()
        self.mostrarProdutos()

    def limparTela(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def mostrarProdutos(self):
        self.treeProdutos.delete(*self.treeProdutos.get_children())
        products = self.appBd.select_all_products()

        for product in products:
            self.treeProdutos.insert("", tk.END, values=product)
        print(self.treeProdutos.selection())
    
    def onDoubleClick(self, event):
        self.limparTela()
        self.treeProdutos.selection()
        for n in self.treeProdutos.selection():
            col1, col2, col3 = self.treeProdutos.item(n,'values')
            self.id = col1
            self.entry_nome.insert(tk.END, col2)
            self.entry_preco.insert(tk.END, col3)
    
    def deletarProduto(self):
        if self.id == "":
            print('selecione um produto primeiro')
            return
        else:
            self.appBd.deletar_produto(self.id)
            self.id = ""
            self.limparTela()
            self.mostrarProdutos()
    
    def atualizarProduto(self):
        if self.id == "":
            print('selecione um produto primeiro')
            return
        else:
            nome = self.entry_nome.get()
            preco = self.entry_preco.get()
            self.appBd.atualizar_produto(nome, preco, self.id)
            self.id = ""
            self.limparTela()
            self.mostrarProdutos()

    def buscarProduto(self):
        self.treeProdutos.delete(*self.treeProdutos.get_children())
        self.entry_nome.insert(tk.END, "%")
        nome = self.entry_nome.get().strip()

        nome_completo = "%" + nome + "%"

        if nome_completo == "":
            print("Por favor, insira um nome para a busca.")
            return
        nomesBuscados = self.appBd.fazer_busca(nome_completo)

        if not nomesBuscados:
            print('Nenhum resultado obtido')
        else:
            for nomeBucado in nomesBuscados:
                self.treeProdutos.insert("", tk.END, values=nomeBucado)
            self.limparTela()



janela = tk.Tk()
PrincipalBD(janela)

janela.title("Bem vindo a janela principal")
janela.geometry("900x700")
janela.mainloop()


