import tkinter as tk

def mostrar_nome():
    escrever_nome = colocar_nome.get()
    label_resultado.config(text = f"Bom dia, {escrever_nome}!")

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
                        foreground="#fefeff",
                        )
#pedir pra inserir o label na janela
label_titulo.pack()

label_nome = tk.Label(janela,
                      text = "Digite seu nome: ",
                      bg= "#66091b",
                      font="Arial",
                      foreground= "#fbfbfb",
                      height= 1)
label_nome.pack()

# caixa de texto para a pessoa digitar seu nome
colocar_nome = tk.Entry(janela)
colocar_nome.pack()

# botão para o programa desejar bom dia
botao_nome = tk.Button(janela,
                       text = "Desejar Bom dia",
                       command = mostrar_nome,
                       bg= "#b31e3b",
                       font="Arial",
                       foreground= "#000000")

botao_nome.pack(pady=5)

label_resultado = tk.Label(janela,
                           text= "")
label_resultado.pack()


# permitir que a entrada e captura de texto



# loop pra manter a janela aberta
janela.mainloop()

