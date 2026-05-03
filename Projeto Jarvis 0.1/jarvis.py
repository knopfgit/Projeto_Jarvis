#Sessão responsável por importar as bibiotecas que irei utilizar no projeto
import os # responsável por ajudar o assistente a algumas funções do sistema operacional
import webbrowser # responsável por ajudar o assistente a realizar pesquisas web 

# =====================================================================================================  
# # Sessão inicial onde implementei as principais funções do nosso JARVIS
def apresentacao(): 
    print("Boas-Vindas Senhor, eu sou o JARVIS, como posso ajuda-lo?")
def ouvir():
    comando = input("Digite o seu comando:")
    return comando.lower()
def responder_comando(comando):
    if "olá jarvis" in comando:
        print("Olá senhor.")
    elif "horas" in comando:
        print("Agora são x horas, senhor.")
    elif "sair" in comando:
        print ("Desligando sistema, até breve, senhor!")
    elif "youtube" in comando:
        print("Abrindo o youtube senhor.")
        webbrowser.open("https://www.youtube.com")
    elif "google" in comando:
        print("Abrindo o google em seu navegador, senhor.")
        webbrowser.open("https://www.google.com")
    elif "pesquisar" in comando:
        termo = comando.replace("pesquisar", "").strip() # linha responsável por separar o termo que o usúario deseja pesquisar usando .strip e concatenação de "strings"
        print("Pesquisando:" + termo + " no seu navegador, senhor")
        webbrowser.open("https://www.google.com/search?q="+ termo)
    else:
        print("Desculpe, senhor, não entendi seu comando.")
def iniciar():
    apresentacao() 
    while True:
        comando = ouvir()
        responder_comando(comando)
        if comando == "sair":
            break
# ======================================================================================================          
# Bloco utilizado para chamar as fuções de apresentação, e a inicialização do JARVIS
if __name__ == "__main__":
    iniciar() # A função iniciar, já vem com a parte da apresentação, por isso removi e deixei apenas o iniciar
