'''
Escreva um programa que receba a idade do usuário e exiba a mensagem “Maior de idade”
caso a idade seja maior ou igual de 18 anos e a mensagem “Menor de idade” caso a idade
seja menor de 18 anos.
'''


def maior_de_idade(idade):
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")


while True:
    idade = int(input("qual a sua idade?\n"))
    maior_de_idade(idade)

