"""
Escrever um programa que lê um valor N inteiro e positivo e que calcula seu
valor fatorial. Ex: 5! = 5 * 4 * 3 * 2 * 1
"""


while True:
    num = int(input("me de o valor para calcular o fatorial:"))
    resultado = 1
    while num > 0:
        resultado *= num
        num -= 1
    print(f"o fatorial é {resultado}")