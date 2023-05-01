"""
Escreva um programa que leia 10 valores e encontre o maior e o menor
deles. Mostre o resultado.
"""
while True:
    lista = []
    for i in range(10):
        lista += [int(input(f"me de o {i + 1}º numero"))]
    print("o maior valor recebido é " + str(max(lista)))
    print("o menor valor recebido é " + str(min(lista)))