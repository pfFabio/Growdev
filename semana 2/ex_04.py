'''
 Ler um número inteiro (assuma até três dígitos) e imprimir a saída da seguinte forma:
CENTENA = x
DEZENA = x
UNIDADE = x
Exemplo: 357 tem 3 centenas, 5 dezenas e 7 unidades.
'''


def desmembra(a):
    a = str(a)
    print(f"CENTENA = {a[:-2]}")
    print(f"DEZENA = {a[-2:-1]}")
    print(f"UNIDADE = {a[-1:]}")

while True:
    desmembra(input("me de um numero de 3 dígitos:\n"))
