import tkinter as tk
from classe_bot_gemini import Gemini_Bot
# o as é pra mudar o nome, basicamente dar um apelido
# e chamar ele do jeito que eu quiser

class Janela_chat():



    def __init__(self):
        self.janela = tk.Tk()

        self.janela.title("Janela da Lolo")
        self.janela.geometry("800x600")

        self.janela.resizable(True,True)
        self.janela.configure(bg="#660d0d")


        self.janela.iconbitmap("03_bot_gemini/flor.ico")


        self.label_especialista = tk.Label(self.janela, text = "Sou especialista em atrasos.", 
               background="#7d1c1c", 
               foreground="#FFFFFF",
               font="Times-New-Roman")
        self.label_especialista.pack(pady=(100,0))


        self.label_nome = tk.Label(self.janela,
                text="Digite a sua dúvida:",
                background="#7d1c1c", 
                foreground="#FFFFFF",
                font="Times-New-Roman")
        self.label_nome.pack(pady=20)


        self.entry_pergunta = tk.Entry(self.janela)
        self.entry_pergunta.pack()


        self.botao_enviar = tk.Button(self.janela,
                 text="Enviar",
                 command= self.responder,
                 height=2)
        self.botao_enviar.pack(pady=20)


        self.resposta = tk.Label(self.janela,
                                 text = "RESPOSTA:"
                                 )
        self.resposta.pack(pady=(0,0))


        #criando o objeto robo(instanciando a classe)
        self.robo = Gemini_Bot()
       


    def responder(self):
        pergunta = self.entry_pergunta.get()
        resposta = self.robo.enviar_mensagem(pergunta)
        self.resposta.config(text = resposta)

        


    def run(self):
        self.janela.mainloop()


if __name__ == "__main__":
    chat = Janela_chat()
    chat.run()