"""
5) De todos os alunos que obtiveram média final maior ou igual a sete, quantos
ultrapassaram 15 faltas?
a) Crie um gráfico de pizza que representa o total de alunos, a
quantidade desses alunos com média final maior ou igual a 7 e desses
quantos ultrapassaram as 15 faltas. Ex. 100 alunos, 80 deles ficaram
com nota igual ou superior a 7 e 25 desses ficaram com mais de 15
faltas. O gráfico deverá ser então conforme o gráfico a seguir.
"""
import matplotlib.pyplot as plt
from dados import carrega_dados

#le o arquivo e faz 2 listas, uma contendo o cabeçalho e outra os dicionarios
lista, cabecalho = carrega_dados('alunos - alunos.csv')
faltosos, aprovados = 0, 0


for i in lista:
    #passando pela lista de dicionarios verifico a média
    media = (i['nota_semestre1'] + i['nota_semestre2']) / 2
    if media >= 7:
        if i['faltas'] <= 15:
            aprovados += 1
        else:
            faltosos += 1

#trocando os valores absolutos pelas porcentagens
aprovados = aprovados/len(lista)
faltosos = faltosos/len(lista)
resto = 1 - (aprovados + faltosos)

#fazendo as labels pro gráfico
titulos = ['Media suficiente', 'Mais 15 faltas', 'Reprovados']

cores = ['#3246a8', '#c46a10', '#376ca6']

plt.pie([aprovados, faltosos, resto], colors = cores, labels = titulos, autopct='%1.1f%%', pctdistance = 1)
kw = dict(arrowprops=dict(arrowstyle="->"), va="center")
plt.show()
