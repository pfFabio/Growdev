"""
Escreva um programa que leia um valor inicial A e uma razão R e imprima
uma sequência em P.G. contendo 10 valores.
"""

while True:
    A = float(input("me de o valor inicial da PG"))
    R = float(input("me de a razão da PG"))
    for i in range(10):
        print(A)
        A *= R