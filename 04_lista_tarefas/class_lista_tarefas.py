import ttkbootstrap as tk
from tkinter import Listbox

class Lista_tarefas():
    def __init__(self):
        self.janela = tk.Window(themename="morph")

        self.janela.title("Tarefas")

        self.janela.geometry("800x600") # arrumar o tamanho da tela
        self.janela.resizable(True, True)

        self.titulo = tk.Label(self.janela,
                               text = "Lista de Tarefas",
                               font="arial, 40")
        self.titulo.pack(pady=(95,0))
#-------------------------------------------------------------------------------
        self.botao_adicionar = tk.Button(text= "adicionar").pack(side="left",padx=20)



    def run(self):
        """Iniciar a janela"""
        self.janela.mainloop()


if __name__ == "__main__":
    lista = Lista_tarefas()
    lista.run()

