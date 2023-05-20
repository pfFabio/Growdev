"""
3) Qual foi a média de faltas dos alunos do colégio Pedro II?
"""


from dados import carrega_dados
lista, cabecalho = carrega_dados('alunos - alunos.csv')
faltas, contador = 0, 0
for i in lista:
    if i['escola'] == 'Pedro II':
        faltas += i['faltas']
        contador += 1

print(f"a média de faltas dos alunos do pedro segundo é {faltas/contador:.0f}")
