"""
Escrever um programa que lê 5 valores para a, um de cada vez, e conta
quantos destes valores são negativos, escrevendo esta informação.
"""

while True:
    numeros = []
    contador = 0
    for i in range(5):
         numeros += [int(input(f"\nme de o {i+1}º numero: "))]
         if numeros[i] < 0:
             print(f"{numeros[i]} é negativo")
             contador += 1
    print(f"você digitou {contador} numeros negativos")