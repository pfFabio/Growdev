"""
Faça um programa que peça o nome e as duas notas de 5 alunos, calcule a
média das notas e armazene nome e média cada uma em uma lista, ao final
imprima o nome e o número de alunos com média maior ou igual a 7.0.
"""

while True:
    nome, media, aprovados = [], [], []
    for i in range(5):
        nome += [input(f"diga o nome do {i+1}º aluno: ")]
        media += [(float(input(f"diga a nota do 1º aluno: ")) + float(input(f"diga a nota do 2º aluno: "))) /2]
    print(nome, media)

    for i in range(len(media)):
        if media[i] >= 7:
            aprovados += nome[i]

    print(f"tivemos {len(aprovados)} aprovados:\n{aprovados}")