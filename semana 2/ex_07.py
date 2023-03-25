'''
Faça um programa para ler a temperatura atual e conforme leitura, imprima o resultado de
acordo com a tabela abaixo.
'''

def clima(x):
    if x <= 15:
        return "Muito frio"
    elif x <= 22:
        return "Frio"
    elif x <= 26:
        return "Agradavel"
    elif x <= 30:
        return "Quente"
    elif x >= 31:
        return "Muito quente"


while True:
    temperatura = int(input("digite a temperatura(somente numeros)"))
    print(clima(temperatura))
