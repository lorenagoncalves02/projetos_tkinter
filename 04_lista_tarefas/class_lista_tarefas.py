import ttkbootstrap as tk
import tkinter as tki
from tkinter import messagebox
from tkinter import Listbox
from tkinter import END

class Lista_tarefas():
    def __init__(self):
        self.janela = tk.Window(themename="morph")

        self.janela.title("Tarefas")

        self.janela.geometry("800x600") # arrumar o tamanho da tela
        self.janela.resizable(True, True)

        self.titulo = tk.Label(self.janela,
                               text = "Lista de Tarefas",
                               font="arial, 15")
        self.titulo.pack(pady=(10,0))
#---------------------------------------------------------------------------------------
        
        frame_adicionar = tk.Frame(self.janela)
        frame_adicionar.pack()

    #campo de entrada pra adicionar uma tarefa
        self.entry_adicionar = tk.Entry(frame_adicionar, width=55)
        self.entry_adicionar.pack(side="right",pady=(15,30), fill="x", expand = True)

        self.botao_adicionar = tk.Button(frame_adicionar,
                                         command=self.adicionar_tarefa,
                                         text= "adicionar").pack(side="left",padx=15,pady=(15,30))
#------------------------------------------------------------------------------------------
        #fazer a caixa pra lista de tarefas
        self.caixa_de_tarefas = tki.Listbox(self.janela,
                                            width= 55,
                                            height= 15)
        self.caixa_de_tarefas.pack(pady=(0,5))

#------------------------------------------------------------------------------------------
        frame_excluir = tk.Frame(self.janela)
        frame_excluir.pack()

        #botao p excluir a tarefa
        self.botao_excluir = tk.Button(frame_excluir,
                                       text= "excluir tarefa",
                                       command=self.excluir_tarefa)
        self.botao_excluir.pack(side="left", padx=(0,80),pady=(10,0))

        self.botao_concluir = tk.Button(frame_excluir,
                                        command=self.concluir_tarefa,
                                        text="concluir tarefa")
        self.botao_concluir.pack(side="right",padx=(70,0),pady=(10,0))
        



        # funçao p botao de adicionar
    def adicionar_tarefa(self):
        tarefa = self.entry_adicionar.get()

        if tarefa :
            self.caixa_de_tarefas.insert(tk.END,tarefa)

        # funçao p botao de excluir
    def excluir_tarefa(self):
        #selecionar os itens que quer excluir
        excluir = self.caixa_de_tarefas.curselection()

        if excluir:
            tarefa_escolhida = excluir[0]
            self.caixa_de_tarefas.delete(tarefa_escolhida)

    def concluir_tarefa(self):
        tarefa_selecionada = self.caixa_de_tarefas.curselection()
        

        # começa vendo as tarefas selecionadas
        if tarefa_selecionada:
            indice = tarefa_selecionada[0]

            texto_tarefa = self.caixa_de_tarefas.get(indice)

            simbolo = "✔"

        #verifica se a tarefa ja ta concluida
            if not texto_tarefa.startswith(simbolo):
                tarefa_concluida = (f"{texto_tarefa}{simbolo}")

                #atualizar a lista(deletar a antiga e recolocar)
                self.caixa_de_tarefas.delete(indice)
                #substituir a tarefa na mesma posição
                self.caixa_de_tarefas.insert(indice,tarefa_concluida)


        
           



    def run(self):
        """Iniciar a janela"""
        self.janela.mainloop()


if __name__ == "__main__":
    lista = Lista_tarefas()
    lista.run()

