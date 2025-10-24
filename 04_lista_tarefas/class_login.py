import ttkbootstrap as tk
import tkinter.messagebox
import tkinter
from class_cadastro import Janela_cadastro
import sqlite3

class Login():

    def __init__(self, janela_pai):
        self.janela_pai = janela_pai

        self.janela = tk.Toplevel(janela_pai)
        self.janela.title("Login")

        self.janela.geometry("800x600") # arrumar o tamanho da tela
        self.janela.resizable(True, True)

        # configurando para que quando feche o login, ele encerre o programa
        self.janela.protocol("WM_DELETE_WINDOW", self.sair)

#-------------------------------------------------------------------------------
        self.titulo = tk.Label(self.janela,
                               text = "Login",
                               font="arial, 40")
        self.titulo.pack(pady=(95,0))
#-------------------------------------------------------------------------------
        self.usuario = tk.Label(self.janela,
                                text = "usuario",
                                font= "arial, 20")
        self.usuario.pack(pady=(15,0))
#-------------------------------------------------------------------------------
        self.colocar_usuario = tk.Entry(self.janela)
        self.colocar_usuario.pack(pady=(5,0))
#-------------------------------------------------------------------------------
        self.senha = tk.Label(self.janela,
                              text = "senha",
                              font= "arial, 20")
        self.senha.pack(pady=(20,0))
#-------------------------------------------------------------------------------
        self.colocar_senha = tk.Entry(self.janela,
                                      text = "arial,15",
                                      show=("*"))
        self.colocar_senha.pack(pady=(5,20))
#----------------------------------------------w--------------------------------

        frame_botao = tk.Frame(self.janela)
        frame_botao.pack()


        tk.Button(frame_botao,
                text = "logar",
                command= self.login_entrar).pack(side="left",padx=20)
        tk.Button(frame_botao,
                  text= "sair",
                  command=self.sair).pack(side="right",padx=20)
        
        tk.Button(self.janela,
                  text="cadastrar",
                  style="primary",
                  command=self.abrir_tela_cadastro).pack(pady=10)

#-------------------------------------------------------------------------------
    def login_entrar(self):
        usuario = (self.colocar_usuario.get())
        senha = (self.colocar_senha.get())

        conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")
        cursor = conexao.cursor()

        cursor.execute(
                """
                SELECT nome, usuario FROM usuario
                WHERE usuario = ? AND senha = ?;
                """,
                [usuario,senha]
            )
 
        resultado = cursor.fetchone()

        conexao.close()

        #se o resultado for diferente de 
        if resultado:
            tkinter.messagebox.showinfo(title = "Login efetuado",message=f"Bem-vindo, {usuario}. Pressione 'ok' para continuar")
            self.janela.destroy()
            #reexiba a janela principal
            self.janela_pai.deiconify()
        #     janela_tarefas = Lista_tarefas()
        #     janela_tarefas.run()

        else:
            tkinter.messagebox.showerror(title= "ERRO", message="valores incorretos")

    def abrir_tela_cadastro(self):
        Janela_cadastro(self.janela)

    def sair(self):
        self.resposta = tkinter.messagebox.askyesno(title= "SAIR", message="Você deseja mesmo sair?")

        if self.resposta == True:
            exit()


    def run(self):
        """Iniciar a janela"""
        self.janela.mainloop()
