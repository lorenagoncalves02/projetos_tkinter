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

        #usuario
        self.titulo = tk.Label(self.janela_cadastro,
                               text = "Digite seu nome de usuário:",
                               font="arial, 15")
        self.titulo.pack(pady=(10,0))

        # criando a caixa de texto do usuário
        self.entry_usuario = tk.Entry(self.janela_cadastro)
        self.entry_usuario.pack()

        #senha
        self.titulo = tk.Label(self.janela_cadastro,
                               text = "Digite sua senha:",
                               font="arial, 15")
        self.titulo.pack(pady=(10,0))

        # criando a caixa de texto de senha
        self.entry_senha = tk.Entry(self.janela_cadastro)
        self.entry_senha.pack()

        tk.Button(self.janela_cadastro, text="Cadastrar", command=self.inserir_usuario).pack()

        self.criar_tabela_usuario()

    def criar_tabela_usuario(self):

        conexao = sqlite3.connect("bd_lista_tarefa.sqlite")

        cursor = conexao.cursor()

        cursor.execute("""
                            CREATE TABLE IF NOT EXISTS usuario(
                            nome VARCHAR(80),
                            usuario VARCHAR(20) primary key,
                            senha VARCHAR(20))
                       """)
        conexao.commit()
        conexao.close()

    def inserir_usuario(self):
        try:
            #pegar os textos do campo de entrada
            nome = self.entry_nome.get()
            usuario = self.entry_usuario.get()
            senha = self.entry_senha.get()
            
            conexao = sqlite3.connect("bd_lista_tarefa.sqlite")

            cursor = conexao.cursor()

            cursor.execute("""
                            INSERT INTO usuario (nome, usuario, senha)
                            VALUES (?, ?, ?)
                        """,
                        (nome, usuario, senha)
                        )
            
            conexao.commit()
            conexao.close()

            messagebox.showinfo("SUCESSO","Usuário cadastrado com sucesso!")
        #apagar o texto depois que cadastrar
            self.entry_nome.delete(0,'end')
            self.entry_usuario.delete(0,'end')
            self.entry_senha.delete(0,'end')

        except:
            messagebox.showerror("ERRO", "Erro ao cadastrar")

    def run(self):
        self.janela_cadastro.mainloop()

        

# chamando sem nenhuma janela pai, so p testar
if __name__ == "__main__":

    janela_cadastro = Janela_cadastro("fghdfv")
    janela_cadastro.run()
