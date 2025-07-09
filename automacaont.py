import pyautogui
import time
import pandas as pd




# Passo 1: Entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# PAsso 2: Fazer login (email,senha e click enter.)
# Passo 3: Importar a base de dados
# Passo 4: cADASTRAR  PRODUTO
    # codigo,marca,tipo,categoria,preco_unitario,custo,obs
        # Passo 4.1: Repetir para todos os produtos:

#-------------PAUSA PARA EXECUÇÕES----------#

pyautogui.PAUSE = 0.3

#-----------------DEFINIÇÃO DE FUNÇÕES-------------#

def abrir_navegador(url):
    pyautogui.PAUSE = 1
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.write(url)
    pyautogui.press("enter")
    time.sleep(3)

def fazer_login(email,senha):
    pyautogui.press("tab")
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)

def cadastrar_produtos(tabela):

    for linha in tabela.idex:
        pyautogui.click(x=758, y=255)
        pyautogui.write(str(tabela.loc[linha, "codigo"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "marca"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "tipo"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "categoria"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "preco_unitario"""]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "custo"]))
        pyautogui.press("tab")

        obs = tabela.loc[linha, "obs"]
        if not pd.isna(obs):
            pyautogui.write(str(tabela.loc[linha, "obs"]))

        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(5000)


#----------------EXECUÇÃO DO SCRIPT---------------#

#Etapa 1: Abertura do navegador:

abrir_navegador("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

#Etapa 2: Fazer login:

fazer_login("devnatanael.natan@gmail.com", "dev#2469")

#Etapa 3: Carregar base de dados:
tabela = pd.read_csv("produtos.csv")
print(tabela)

#Etapa 4: Cadastrar produos:

cadastrar_produtos(tabela)