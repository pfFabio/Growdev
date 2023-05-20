"""
5) De todos os alunos que obtiveram média final maior ou igual a sete, quantos
ultrapassaram 15 faltas?
"""

from dados import carrega_dados
lista, cabecalho = carrega_dados('alunos - alunos.csv')

faltosos = 0

for i in lista:
    media = (i['nota_semestre1'] + i['nota_semestre2']) / 2
    if media >= 7 and i['faltas'] > 15:
            faltosos += 1

faltosos = faltosos/len(lista)
print(f'5) {faltosos} alunos tiveram média maior ou igual a 7 e faltas maiores que 15')
