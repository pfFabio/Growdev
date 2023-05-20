from dados import carrega_dados
import matplotlib.pyplot as plt
dados, cabecalho = carrega_dados('alunos - alunos.csv')


faltas_escola = {}
alunos_escola = {}

for aluno in dados:
    escola = aluno['escola']
    if faltas_escola.get(escola) is not None:
        faltas_escola[escola] += aluno['faltas']
        alunos_escola[escola] += 1
    else:
        faltas_escola[escola] = aluno['faltas']
        alunos_escola[escola] = 1

nomes_escolas = faltas_escola.keys()

print(faltas_escola)

print(alunos_escola)