import ttkbootstrap as tk
import tkinter as tki
from tkinter import messagebox
from tkinter import Listbox
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

#---------------------------------------------------------------------------------------------------

        
    