"""
2) Qual foi o percentual de alunos que utilizaram e que não utilizaram a
monitoria?
"""


from dados import carrega_dados
lista, cabecalho = carrega_dados('alunos - alunos.csv')
quantidade_de_alunos = len(lista)
monitoria = 0

for i in lista:
    if i['monitoria'] == "TRUE":
        monitoria += 1


print(f'notamos que {(100 * monitoria)/quantidade_de_alunos:.2f}% dos alunos fez monitoria')
print(f'e {(1 - (monitoria/quantidade_de_alunos)) * 100:.2f}% dos não fez monitoria')
