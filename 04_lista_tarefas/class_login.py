import ttkbootstrap as tk
import tkinter.messagebox
from class_lista_tarefas import Lista_tarefas

class Login():

    def __init__(self):
        self.janela = tk.Window(themename= "morph")
        self.janela.title("Login")

        self.janela.geometry("800x600") # arrumar o tamanho da tela
        self.janela.resizable(True, True)

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

        frame_botao = tk.Frame()
        frame_botao.pack()


        tk.Button(frame_botao,
                text = "logar",
                command= self.login_entrar).pack(side="left",padx=20)
        tk.Button(frame_botao,
                  text= "sair",
                  command=self.sair).pack(side="right",padx=20)
#-------------------------------------------------------------------------------
    def login_entrar(self):
        usuario = self.colocar_usuario.get()
        senha = self.colocar_senha.get()


        if usuario == "Lorena" or senha == "1234":
            tkinter.messagebox.showinfo(title = "Login efetuado",message=(f"Bem-vindo, {usuario}. Pressione 'ok' para continuar"))
            self.janela.destroy()
            janela_tarefas = Lista_tarefas()
            janela_tarefas.run()


        else:
            tkinter.messagebox.showerror(title= "ERRO", message="valores incorretos")

    def sair(self):
        self.sair = tkinter.messagebox.askyesno(title= "SAIR", message="Você deseja mesmo sair?")

        if self.sair == True:
            exit()



    def run(self):
        """Iniciar a janela"""
        self.janela.mainloop()


if __name__ == "__main__":
    login = Login()
    login.run()


