"""
Escreva um programa que leia a idade e salário de 10 pessoas. Informe em
seguida:
a) Qual é a média de idade entre as pessoas?
b) Quantas pessoas há por faixa etária, considerando:
i) jovens < 18
ii) 18 <= adultos < 60
iii) idosos >= 60
c) Em seguida, mostre qual é a faixa etária que acumula o maior salário.
"""


while True:
    pessoas = []
    jovens, adultos, idosos, somai, salarioj, salarioa, salarioi= 0, 0, 0, 0, 0, 0, 0
    rico = ["",0]
    for i in range(3):
        pessoas += [[int(input(f"me de a idade: "))]]
        pessoas[i] += [float(input(f"me de o salário: "))]

    for i in range(len(pessoas)):

        if pessoas[i][0] < 18: #separando por faixa etaria e somando os salários para comparar depois
            jovens += 1
            salarioj += pessoas[i][1]
        elif pessoas[i][0] < 60:
            adultos += 1
            salarioa += pessoas[i][1]
        else:
            idosos += 1
            salarioi += pessoas[i][1]

        somai += i #somando as idade pra achar a média depois

    if salarioj >= salarioa and salarioj >= salarioi:
        rico = "jovens"
    if salarioa >= salarioi and salarioa >= salarioj:
        rico = "adultos"
    if salarioi >= salarioj and salarioi >= salarioa:
        rico = "idosos"

    print(f"\na média de idades é {somai/len(pessoas)}")
    print(f"temos: \n{jovens} jovens\n{adultos} adultos\n{idosos} idosos")
    print(f"a faixa etária que acumula o maior valor salarial são os {rico}\n\n")




