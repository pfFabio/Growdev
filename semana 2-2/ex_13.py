"""
13)Faça um programa que leia um valor N e mostre os N termos da Série a
seguir:
a) S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m
"""

while True:
    resultado = 0
    N = int(input("me de o valor de N")) + 1
    for i in range(1, N):
        M = int(i * 2) - 1
        print(f"{i}/{M}")
        resultado += i/M

    print(f"a soma dos valores é igual a {resultado}")
