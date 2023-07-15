"""
2) Qual foi o percentual de alunos que utilizaram e que não utilizaram a
monitoria?
a) Crie um gráfico de pizza para representar os percentuais.
"""


from dados import carrega_dados
import matplotlib.pyplot as plt
lista, cabecalho = carrega_dados('alunos - alunos.csv')
quantidade_de_alunos = len(lista)
monitoria = 0

for i in lista:
    if i['monitoria'] == "TRUE":
        monitoria += 1


a_monitoria = 100 * monitoria/quantidade_de_alunos
a_sem_monitoria = (1 - (monitoria/quantidade_de_alunos)) * 100

x = [a_monitoria, a_sem_monitoria]
y = 'auxiliados', 'não auxiliados'

plt.pie(x,labels = y,  autopct='%1.1f%%', startangle= 90)
plt.show()

