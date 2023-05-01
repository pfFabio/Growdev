import random


def loteria():
    lista = []
    for i in range(3):
        lista += [random.randint(0, 9)]

    return lista


def comparacao(x, aposta):
    contador = 0
    if x == aposta:
        return 10
    for i in x:
        for j in aposta:
            if i == j:
                contador += 1
    return contador


def resultado(x):
    if x == 0:
        print("você não fez pontos")
    elif x == 1:
        print("você fez 10 pontos")
    elif x == 2:
        print("você fez 100 pontos")
    elif x == 3:
        print("você fez 1000 pontos")
    elif x == 10:
        print("você fez 1.000.000 de pontos")


while True:
    aposta = []
    for i in range(3):
        aposta += [int(input(f"faça sua {i+1}ª aposta: "))]
    loteria1 = loteria()
    sorte = comparacao(loteria1, aposta)
    print(f"suas apostas foram: {aposta}\na loteria sorteou: {loteria1}")
    resultado(sorte)
    print("\n\n\n")


