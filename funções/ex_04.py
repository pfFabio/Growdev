"""
4) Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e
colunas, com um número em cada posição e no qual a soma das linhas,
colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de
lado 3, com números de 1 a 9:
8 3 4
1 5 9
6 7 2
Elabore uma função que receba uma estrutura de 3x3 formada por listas, e
diga se é um quadrado mágico ou não.
"""

def quadrado_magico(quadrado):
    somas = []
    for i in range(3):
        somas += [sum(quadrado[i])]
        somas += [quadrado[0][i] + quadrado[1][i] + quadrado[2][i]]
    somas += [quadrado[0][0] + quadrado[1][1] + quadrado[2][2]]
    somas += [quadrado[0][2] + quadrado[1][1] + quadrado[2][0]]
    teste = somas[0]
    print(quadrado)
    for i in somas:
        if i != teste:
            return False
    return True




while True:
    matriz = [[], [], []]

    for i in range(3):
        matriz[0] += [int(input(f"digite o {i+1}º valor da 1ª linha: "))]

    for i in range(3):
        matriz[1] += [int(input(f"digite o {i+1}º valor da 2ª linha: "))]

    for i in range(3):
        matriz[2] += [int(input(f"digite o {i+1}º valor da 3ª linha: "))]

    if quadrado_magico(matriz):
        print("é um quadrado mágico")
    else:
        print("não é um quadrado mágico")
