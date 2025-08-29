import ttkbootstrap as tk

class Janela_principal:
    """Classe para a criação da janela principal"""

    def __init__(self):

        # criando uma janela
        # Tk (com a primeira maiuscula) é uma classe
        self.janela = tk.Window(themename= "vapor")
        self.janela.title("Janela Da Lolo")
        # pra colocar título na janela

        # configurando a janela

        self.janela.iconbitmap("01_Hello_World/fox.ico") # caminho de um ícone
        self.janela.geometry("800x400+200+300") # arrumar o tamanho da tela
        self.janela.resizable(True, True) # pro usuário não editar o tamanho da janela



        # criando os widgets (os componentes)
        # criando o titulo e formatando
        self.label_titulo = tk.Label(self.janela,
                                text="Hello World!",
                                font="Arial"
                                )
        #pedir pra inserir o label na janela
        self.label_titulo.pack(pady=5)#pady é a distancia que fica entre o botão e o texto

        self.label_nome = tk.Label(self.janela,
                            text = "Digite seu nome: ",
                            font="Arial",
                      )
        self.label_nome.pack(pady=2)

        # caixa de texto para a pessoa digitar seu nome
        self.colocar_nome = tk.Entry(self.janela)
        self.colocar_nome.pack(pady=2)

        # botão para o programa desejar bom dia
        self.botao_nome = tk.Button(self.janela,
                            text = "Desejar Bom dia",
                            command = self.mostrar_nome, #aqui que eu chamo a função
                            )

        self.botao_nome.pack(pady=5)

        self.label_resultado = tk.Label(self.janela,
                                text= "")
        self.label_resultado.pack()


        # permitir que a entrada e captura de texto

    def run(self):
        """Inicie a janela"""
        # loop pra manter a janela aberta
        self.janela.mainloop()


        #função para o botão funcionar
    def mostrar_nome(self):
        #3 aspas pra documentar os códigos e facilitar
        """Esta função pega o nome digitado na caixa de texto e deseja um bom dia"""
        escrever_nome = self.colocar_nome.get() #get é pra pegar o texto digitado na caixa 
        self.label_resultado.configure(text = f"Bom dia, {escrever_nome}!")