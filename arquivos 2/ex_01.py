"""
1) Somando, separadamente, as notas do primeiro semestre e do segundo
semestre. Qual semestre obteve o maior somatório?
"""
from dados import carrega_dados
lista, cabecalho = carrega_dados('alunos - alunos.csv')

notas1, notas2 = 0, 0

for i in lista:
    notas1 += i['nota_semestre1']
    notas2 += i['nota_semestre2']


if notas1 > notas2:
    print('quando somadas, as notas do primeiro semestre superam as do segundo')
if notas2 > notas1:
    print('quando somadas, as notas do segundo semestre superam as do primeiro')
else:
    print('ao somar as notas dos semestres notamos que o resultado é igual')
