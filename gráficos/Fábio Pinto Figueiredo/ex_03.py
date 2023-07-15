"""
3) Qual foi a média de faltas dos alunos do colégio Pedro II?
a) Modifique esse exercício para calcular a média de alunos de cada
colégio, e exiba os resultados como um gráfico de linha.
"""


from dados import carrega_dados
import matplotlib.pyplot as plt
lista, cabecalho = carrega_dados('alunos - alunos.csv')
faltas= 0
escolas = []
medias = []
contador = []
for i in lista:
    controle = 0
    for j in range(len(escolas)): #passa pelo vetor escola procurando se a escola ja esta listada
        if i['escola']  == escolas[j] and controle == 0:
            medias[j] += i['faltas']
            contador[j] += 1
            controle = 1
    if controle == 0: #se não encontrar a escola adiciona nos vetores
        escolas += [i['escola']]
        medias += [i['faltas']]
        contador += [0]

for i in range(len(medias)): #substitui os somadores pelas médias
    medias[i] = medias[i] / contador[i]

plt.plot(escolas,medias)
plt.xticks(rotation=12)
plt.ylabel('média das faltas')
plt.show()





