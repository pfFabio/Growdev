"""
Modifique o programa anterior para que utilize apenas uma lista e em cada
posição da lista armazene um dicionário com o nome e a média.
"""


while True:
    nome, aprovados = {}, []
    for i in range(3):
        #fazer index separado pra não atrapalhar ordem dos prints
        index = input(f"diga o nome do {i+1}º aluno: ")
        #associando as médias das notas aos nomes
        nome[index] = (float(input(f"diga a 1ª nota do aluno: ")) + float(input(f"diga a 2ª nota do aluno: "))) /2
    print(nome)
    for i in nome:
        if nome[i] >= 7:
            aprovados += i

    print(f"tivemos {len(aprovados)} aprovados:\n{aprovados}")