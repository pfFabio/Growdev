"""
Faça um programa, com uma função que necessite de três argumentos, e
que forneça a soma desses três argumentos.
"""


def soma_tres(x, y, z):
    return x + y + z


while True:
    primeiro_numero = float(input("me de o primeiro numero :"))
    segundo_numero = float(input("me de o segundo numero : "))
    terceiro_numero = float(input("me de o terceiro numero :"))
    print(soma_tres(primeiro_numero, segundo_numero, terceiro_numero))
