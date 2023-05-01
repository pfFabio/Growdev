"""
Desenvolver um programa que leia um número não determinado de valores
e calcule e escreva a média aritmética dos valores lidos, a quantidade de
valores positivos, a quantidade de valores negativos e o percentual de
valores negativos e positivos.
"""

while True:
    numeros = []
    num = ''
    resultado, negativos, positivos = 0, 0, 0
    while num != "pare":
        num = input("me de um numero ou digite 'pare'")
        if num != "pare":
            numeros += [int(num)]
            resultado += int(num)
    for i in numeros:
        if i < 0:
            negativos += 1
        else:
            positivos += 1

    quantidade = len(numeros)

    print(f"a média dos valores entregues é igual a {resultado/quantidade}")
    print(f"foram digitados {positivos} numeros positivos que equivale a {positivos * 100 / quantidade:.2f}% do total")
    print(f"foram digitados {negativos} numeros negativos que equivale a {negativos * 100 / quantidade:.2f}% do total")

