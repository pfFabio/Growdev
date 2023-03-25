'''
Escreva um programa que receba dois números, exiba as opções: a) 1 - adição
b) 2 - subtração
Então peça ao usuário para escolher uma das opções. Caso escolha a opção 1 o programa deve
realizar a soma dos dois números lidos e exibir. Caso escolha a opção 2 o programa deve
realizar a subtração dos dois números lidos e exibir.
'''

def soma(x, y):
    return x+y

def subtracao(x, y):
    return x-y

while True:
    primeiro = float(input("digite o 1º numero"))
    segundo = float(input("digite o 2º numero"))
    escolha = int(input("digite 1 para fazer a soma\ndigite 2 para fazer a subtração"))

    match escolha:
        case 1:
            print("o resultado da soma é", soma(primeiro, segundo))

        case 2:
            print("o resultado da subtração é ", subtracao(primeiro, segundo))

        case _:
            print("não entendi, por favor repita!")
