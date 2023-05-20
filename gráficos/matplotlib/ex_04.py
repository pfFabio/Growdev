"""
4) A média de notas do primeiro semestre foi maior entre alunos do 1 ano ou 3
ano?
a) Exiba as médias dos alunos como um gráfico de barras/colunas.
"""
import matplotlib.pyplot as plt

from dados import carrega_dados
lista, cabecalho = carrega_dados('alunos - alunos.csv')

notas_primeiro_1, notas_primeiro_3 = 0, 0
contador1, contador2 =0, 0

for i in lista:
    if i['ano'] == 1:
        notas_primeiro_1 += i['nota_semestre1']
        contador1 += 1
    elif i['ano'] == 3:
        notas_primeiro_3 += i['nota_semestre1']
        contador2 += 1

media1 = notas_primeiro_1/contador1
media2 = notas_primeiro_3/contador2

plt.bar(['1º ano', '3º ano'], [media1, media2])
plt.show()
