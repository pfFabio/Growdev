"""
Após construir o programa anterior, crie mais duas versões dele para prever as seguintessituações:
a) Um aluno pode ficar em recuperação se possuir frequência suficiente (superior a 75%) e média superior a 5 mas
 inferior a 7;
b) Caso um aluno reprove por média e faltas, sua situação deve ser “Reprovado por Média e Faltas” (ao invés de
 simplesmente “Reprovado por Faltas” como antes).
"""


def media(a, b, c, d):
    nota = (a+b+c+d)/4
    if nota >= 7:
        return 1
    elif nota >= 5:
        return 0.5
    else:
        return 0


def presenca(total, faltas):
    aulas = 1 - faltas/total

    if aulas > 0.75:
        return 1
    else:
        return 0


def situacao(aprovacaom, aprovacaop):
    if aprovacaom <= 0.5 and aprovacaop == 0:
        print("reprovado por falta e media")
    elif aprovacaom == 0.5 and aprovacaop == 1:
        print("está em recuperação")
    elif aprovacaom == 1 and aprovacaop == 1:
        print("aprovado")
    elif aprovacaom == 0:
        print("reprovado por nota")
    else:
        print("reprovado por faltas")


lista = []
while True:
    for i in range(4):
        lista += [float(input(f"qual foi a {i + 1}ª nota?\n"))]

    calendario = int(input("quantos dias de aula houveram nesse ano?\n"))
    falta = int(input("quantas faltas o aluno teve?"))

    Aprovacaom = media(lista[0], lista[1], lista[2], lista[3])
    Aprovacaop = presenca(calendario, falta)

    situacao(Aprovacaom, Aprovacaop)



