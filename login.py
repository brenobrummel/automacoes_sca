from selenium.webdriver import Firefox
import pyautogui as pt
import time

pt.PAUSE = 0.4

navegador = Firefox()
url = 'http://localhost:5173/'

def esperar(tempo):
    time.sleep(tempo)

def entrar_e_logar():
    navegador.get(url)

    usuario = navegador.find_element('xpath', '//*[@id="root"]/div/div[2]/div[2]/input')
    senha = navegador.find_element('xpath', '//*[@id="root"]/div/div[2]/div[3]/div/input')
    botao_entrar = navegador.find_element('xpath', '//*[@id="root"]/div/div[2]/button')

    esperar(5)
    pt.hotkey('ctrl', '-')
    pt.hotkey('ctrl', '-')
    pt.hotkey('ctrl', '-')
    usuario.send_keys('7470428')
    senha.send_keys('senha123')
    botao_entrar.click()

entrar_e_logar()

esperar(1)

pt.click(x=35, y=741)