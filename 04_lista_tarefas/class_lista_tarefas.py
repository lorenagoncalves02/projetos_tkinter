import ttkbootstrap as tk

class Lista_tarefas():
    def __init__(self):
        self.janela = tk.Window(themename="superhero")



    def run(self):
        """Iniciar a janela"""
        self.janela.mainloop()


if __name__ == "__main__":
    lista = Lista_tarefas()
    lista.run()

