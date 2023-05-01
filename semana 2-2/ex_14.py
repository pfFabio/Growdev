"""
Desenvolver um programa que efetue a soma de todos os números ímpares
que se encontram no conjunto dos números de 1 até 500.
"""

resultado = 0
for i in range(1,500):
    if i % 2 == 1:
        resultado += i

print(f"a soma dos numeros impares de 1 a 500 é igual a {resultado}")