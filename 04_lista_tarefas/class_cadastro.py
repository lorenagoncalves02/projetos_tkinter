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

        # criando a caixa de texto do usuário
        entry_usuario = tk.Entry(self.janela_cadastro)
        entry_usuario.pack()

        # criando a caixa de texto de senha
        entry_senha = tk.Entry(self.janela_cadastro)
        entry_senha.pack

    def run(self):
        self.janela_cadastro.mainloop()

# chamando sem nenhuma janela pai, so p testar
if __name__ == "__main__":
    janela_cadastro = Janela_cadastro()
    janela_cadastro.run()
    
        
