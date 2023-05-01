'''
Numa determinada escola, os critérios de aprovação são os seguintes:
a) O aluno deve ter, no máximo, 25% de faltas;
b) A nota final deve ser igual ou superior a 7,00.
Construa um programa para ler as notas que um aluno tirou nos 4 bimestres,
o número total de aulas e o número de faltas, mostrando ao final a situação do aluno como sendo “Aprovado”,
“Reprovado por Faltas” e “Reprovado por média”,
considerando que a reprovação por faltas se sobrepõe a reprovação por nota.
'''


def media(a, b, c, d):
    return ((a+b+c+d)/4) >= 7


def presenca(total, faltas):
    return (faltas/total) < 0.25

list = []
while True:
    for i in range(4):
        list += [float(input(f"qual foi a {i+1}ª nota?\n"))]

    calendario = int(input("quantos dias de aula houveram nesse ano?\n"))
    falta = int(input("quantas faltas o aluno teve?"))

    if not presenca(calendario, falta):
        print("Reprovado por Faltas")
    elif not media(list[0], list[1], list[2], list[3]):
        print("Reprovado por média")
    else:
        print("Aprovado")

