"""
Crie um programa para que retorne o somatório de todos os números entre 1
e um valor fornecido pelo usuário. Por exemplo, se o usuário fornecer o
número 4, o computador deverá calcular o somatório 1+ 2 + 3 + 4 = 10.
"""

while True:
    num = int(input("me de um numero para somar todos os antecessores: "))
    resultado = 0
    for i in range(num):
        resultado += i
    print(f"a soma é igual a {resultado}")

