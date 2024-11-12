import random
import string
placas = []
def gerar_tres_letras(tamanho=3):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(tamanho))
def gerar_uma_letra(tamanho=1):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(tamanho))

for _ in range(199):
    placa = f'{gerar_tres_letras()}{random.randint(0, 9)}{gerar_uma_letra()}{random.randint(10, 99)}'
    placas.append(placa)

print(placas)