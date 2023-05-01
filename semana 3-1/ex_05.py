"""
Construa um programa que permita a um usuário informar uma série de
números, até que um número negativo seja fornecido. Ao final, imprima o
somatório desses números, a média, o valor máximo e o mínimo.
Desconsidere o último número (negativo) informado pelo usuário.
"""

while True:
    soma, maior, cont = 0, 0, 0
    i = float(input("digite um numero positivo para começar: "))
    menor = i
    while i>0:
        soma += i
        if i > maior:
            maior = i
        if i < menor:
            menor = i
        cont += 1
        i = float(input("digite o próximo numero positivo para continuar ou digite um numero negativo para parar"))
    print(f'o maior valor digitado foi: {maior}')
    print(f'o menor valor digitado foi: {menor}')
    print(f'a média dos valores digitados foi {soma / cont}')
