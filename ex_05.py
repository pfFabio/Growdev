"""
Escreva um programa para solicitar ao usuário o raio r de uma esfera, e
calcular o volume V da esfera usando uma função, e exibir o resultado. Utilize
a seguinte fórmula para determinar o volume:
v = (4.0 / 3.0) * ℼ * r³
"""
from math import pi

while True:
    raio = float(input("qual o raio da esfera? "))
    volume = (4/3) * pi * raio
    print(f"o volume da esfera é {volume}")

