"""
Escrever um programa que lê um valor N inteiro e positivo e que calcula e
escreve o valor de E.
E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + ... + 1 / N!
"""

while True:
    E = 0
    num = int(input("me de o valor para calcular o E:"))
    for fatorial in range(num + 1):
        resultado = 1
        while fatorial > 0:
            resultado *= fatorial
            fatorial -= 1
        E += 1/resultado
        print(f"1 / {resultado} = {1/ resultado:.4f}")
    print(f"E é igual a {E:.4f}")