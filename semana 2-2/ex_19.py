"""
Escreva um programa que leia um valor inicial A e uma razão R e imprima
uma sequência em P.A. contendo 10 valores.
"""

while True:
    A = float(input("me de o valor inicial da PA"))
    R = float(input("me de a razão da PA"))
    for i in range(10):
        print(A)
        A += R
