import ttkbootstrap as tk
import tkinter as tki
from tkinter import messagebox
from tkinter import Listbox
from tkinter import END
import sqlite3

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
#-------------------------------------------------------------------------------------------

        #conectando ao banco de dados
        #dar nome pro banco de dados
        #colocar o nome da pasta onde eu quero guardar o banco de dados
        conexao = sqlite3.connect("04_lista_tarefas/bd_lista_tarefa.sqlite")

        #cursor é responsável por comandar o banco de dados
        cursor = conexao.cursor()

        # criar as tabelas
        cursor.execute(""" 
                            CREATE TABLE IF NOT EXISTS tarefa(
                            codigo integer primary key autoincrement, 
                            descricao_tarefa varchar(200)
                            );
                         """)
        
        #comitei as alterações
        conexao.commit()

        #fechei a conexão (posso usar so a conexao.close q ja fecha o cursor)
        cursor.close()
        conexao.close()

        self.atualizar_lista()
#------------------------------------------------------------------------------------------

    def atualizar_lista(self):
        #atualizar a lista
        conexao = sqlite3.connect("04_lista_tarefas/bd_lista_tarefa.sqlite")

        cursor = conexao.cursor()
        cursor.execute("""
                        SELECT codigo, descricao_tarefa FROM tarefa;
                       """)
        
        lista_de_tarefas = cursor.fetchall()


        cursor.close()
        conexao.close()

        #inserindo os itens na listbox
        for linha in lista_de_tarefas:
            self.caixa_de_tarefas.insert("end", linha[1])



        # funçao p botao de adicionar
    def adicionar_tarefa(self):
        tarefa = self.entry_adicionar.get()

        #criando a tabela pra conseguir inserir os dados
        conexao = sqlite3.connect("04_lista_tarefas/bd_lista_tarefa.sqlite")
        cursor = conexao.cursor()

        cursor.execute("""
                        INSERT INTO tarefa(descricao_tarefa)
                        VALUES(?)
                       """, [tarefa])

        conexao.commit()
        cursor.close()
        conexao.close()

        if tarefa :
            self.caixa_de_tarefas.insert(tk.END,tarefa)

        # funçao p botao de excluir
    def excluir_tarefa(self):
        #selecionar os itens que quer excluir
        excluir = self.caixa_de_tarefas.curselection() #retorna o indice selecionado

        if excluir:
            tarefa_escolhida = excluir[0]
            self.caixa_de_tarefas.delete(tarefa_escolhida)
        else:
            messagebox.showerror(message="Selecione um item antes de excluir")

        conexao = sqlite3.connect("04_lista_tarefas/bd_lista_tarefa.sqlite")
        cursor = conexao.cursor()

        cursor.execute("""
                        DELETE FROM tarefa WHERE id = 
                       """)
        conexao.commit()
        cursor.close()
        conexao.close()

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

