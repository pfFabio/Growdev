"""
Escreva um programa que imprima na tela para escrever a tabuada de um
número fornecido pelo usuário, de 1 a 10.
"""


while True:
    base = int(input("me de um numero de 1 a 10"))

    print(f"a tabuada de {base} é:")
    for i in range(10):
        print(f"{base} * {i} = {i * base}")
