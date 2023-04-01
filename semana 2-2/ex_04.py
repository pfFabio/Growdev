"""
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
coletando dados sobre o salário e número de filhos. A prefeitura deseja
saber:
a) média do salário da população;
b) média do número de filhos;
c) maior salário;
d) percentual de pessoas com salário até R$2000,00.
Escreva um programa que receba as informações necessárias de 5 pessoas
conforme a descrição e responda às questões a, b, c e d anteriores.
"""


while True:
    familias = []
    renda, pobres, ricasso, filhos = 0, 0, 0, 0
    for i in range(5):
        familias += [[float(input("informe a renda familiar: "))]]
        familias[i] += [int(input("informe o numero de filhos na familia: "))]

    for i in range(len(familias)):
        if familias[i][0] < 2000:
            pobres += 1
        if familias[i][0] > ricasso:
            ricasso = familias[i][0]
        renda += familias[i][0]
        filhos += familias[i][1]


    print(f"\n\na média dos salários é R${renda / len(familias):.2f}")
    print(f"a média dos filhos é {filhos / len(familias):.1f}")
    print(f"o maior salário informado foi de {ricasso}")
    print(f"{pobres * 100 / len(familias)}% das familias recebem menos de R$2000,00\n\n")
