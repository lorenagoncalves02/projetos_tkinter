import tkinter as tk

# criando uma janela
# Tk (com a primeira maiuscula) é uma classe
janela = tk.Tk()
janela.title("Janela Da Lolo")
# pra colocar título na janela

# configurando a janela
janela.configure(bg="#66091b") # colocar uma cor na janela
janela.iconbitmap("01_Hello_World/fox.ico") # caminho de um ícone
janela.geometry("800x400+200+300") # arrumar o tamanho da tela
janela.resizable(True, True) # pro usuário não editar o tamanho da janela

# criando os widgets (os componentes)
# criando o titulo e formatando
label_titulo = tk.Label(janela,
                        text="Hello World!",
                        bg="#66091b",
                        font="Arial",
                        foreground="#fefeff")
#pedir pra inserir o label na janela
label_titulo.pack()

# permitir que a entrada e captura de texto
label_nome = tk.Label(janela,
                      text = "Digite seu nome: ")

# loop pra manter a janela aberta
janela.mainloop()

