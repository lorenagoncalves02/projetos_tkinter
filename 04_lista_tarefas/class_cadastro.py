import ttkbootstrap as tk
import tkinter as tki
from tkinter import messagebox
from tkinter import Listbox
import sqlite3

class Janela_cadastro():
    def __init__(self, janela_pai):

        self.janela_cadastro = tk.Toplevel(janela_pai)

        self.janela_cadastro.title("Tarefas")

        self.janela_cadastro.geometry("800x600") # arrumar o tamanho da tela
        self.janela_cadastro.resizable(True, True)

        self.titulo = tk.Label(self.janela_cadastro,
                               text = "CADASTRO DE USUÁRIO",
                               font="arial, 15")
        self.titulo.pack(pady=(10,0))

        self.titulo = tk.Label(self.janela_cadastro,
                               text = "Digite seu nome completo:",
                               font="arial, 15")
        self.titulo.pack(pady=(10,0))

        #criando a caixa de texto do nome
        self.entry_nome = tk.Entry(self.janela_cadastro)
        self.entry_nome.pack()

        # criando a caixa de texto do usuário
        self.entry_usuario = tk.Entry(self.janela_cadastro)
        self.entry_usuario.pack()

        # criando a caixa de texto de senha
        self.entry_senha = tk.Entry(self.janela_cadastro)
        self.entry_senha.pack

        tk.Button(self.janela_cadastro, text="Cadastrar")

        self.criar_tabela_usuario()

    def criar_tabela_usuario(self):

        conexao = sqlite3.connect("./bd_lista_tarefas.sqlite")

        cursor = conexao.cursor()

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS usuario (
                            nome VARCHAR(80),
                            usuario VARCHAR(20),
                            senha VARCHAR(20))
                       """)
        
        conexao.commit()
        conexao.close()

    def inserir_usuario(self):
        
        conexao = sqlite3.connect("./bd_lista_tarefas.sqlite")

        cursor = conexao.cursor()

        nome = self.entry_nome
        usuario = self.entry_usuario
        senha = self.entry_senha

        cursor.execute("""
                        INSERT INTO usuario (nome, usuario, senha)
                        VALUES (?, ?, ?)
                       """,
                       (nome, usuario, senha)
                       )
        
        conexao.commit()
        conexao.close


    def run(self):
        self.janela_cadastro.mainloop()

# chamando sem nenhuma janela pai, so p testar
if __name__ == "__main__":

    janela_cadastro = Janela_cadastro("u65d75")
    janela_cadastro.run()
    
