import google.generativeai as genai


class Gemini_Bot:
    #Cria um robo especialista em atrasos
    """Classe responsável por gerenciar o modelo do Gemini"""

    #função pra colocar o codigo do gemini api
    def __init__(self):
        genai.configure(api_key="AIzaSyDh57VQ1HK1fhFg8MS0jP8sGYyxX2DNyIM")
        
        introducao_sistema = """
                Você é especialista em atrasos
                """
        
        self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=introducao_sistema
        )




        self.chat = self.model.start_chat()

    #função pra ele guardar a resposta e imprimir 
    #self é sempre o primeiro atributo
    def enviar_mensagem(self,pergunta:str) -> str:
        """Envia mensagem para o modelo e retorna a resposta."""

        response = self.chat.send_message(pergunta)
        return response.text
    
# o if só será executado se eu rodar o arquivo diretamente
# caso eu importe, essa parte não será executada
# pode ser utilizada para testes
if __name__ == "__main__":
    robo = Gemini_Bot()
    resposta = robo.enviar_mensagem("Qual é o animal mais lindo do mundo?")
    print(resposta)