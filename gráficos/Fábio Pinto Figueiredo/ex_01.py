"""
1) Somando, separadamente, as notas do primeiro semestre e do segundo
semestre. Qual semestre obteve o maior somatório?
a) Para esse exercício crie um gráfico de colunas/barras para representar
os somatórios das notas de ambos os semestres.
"""
from dados import carrega_dados
import matplotlib.pyplot as plt
lista, cabecalho = carrega_dados('alunos - alunos.csv')

notas1, notas2 = 0, 0

for i in lista:
    notas1 += i['nota_semestre1']
    notas2 += i['nota_semestre2']



x = ['1º semestre', '2º semestre']
y = [notas1, notas2]


plt.bar(x,y)
plt.ylabel('soma das notas')
plt.show()
