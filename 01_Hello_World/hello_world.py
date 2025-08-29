import tkinter as tk


janela = tk.Tk()
janela.title("Janela da Lolo")

# configurando a janela
#Mudando o tamanho da tela
janela.geometry("800x400+200+300")
#Permitindo a mudança da janela
janela.resizable(True,True)
#Mudando a cor da janela
janela.configure(bg="#810C0C")
#Mudar o icone da janela
janela.iconbitmap("01_Hello_World/fox.ico")

# criando os widgets (os componentes)
# criando o titulo e formatando
def mostrar():
    """ESta função coleta o noem colocado na caixa de texto e deseja um bom dia."""
    n = c_n.get()
    res.configure(text=f"Bom dia {n}!!!")
#Adicionando texto e modificando
tet = tk.Label(janela, 
               text="Hello World", 
               background="#ae1a1a", 
               foreground="#FFFFFF",
               font="Times-New-Roman")
tet.pack(pady=30)

#Vai indicar o que o usuario deve fazer
l_nome = tk.Label(janela,
                text="Digite o seu nome:",
                background="#BC1717", 
                foreground="#FFFFFF",
                font="Times-New-Roman",)
l_nome.pack(pady=2)

#Criar uma caixa de texto
c_n = tk.Entry(janela)
c_n.pack()

#
b_bd = tk.Button(janela,
                 text="Desejar bom dia!!!",
                 height=2,
                 command= mostrar)
b_bd.pack(pady=20)

#label que vai aparecer o bom dia
res = tk.Label(janela,
               text="",
               background="#1b22a7",
               foreground="#FFFFFF")
res.pack()

#Loop para manter a janela aberta
janela.mainloop()

