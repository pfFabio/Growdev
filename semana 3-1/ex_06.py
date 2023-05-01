"""
Crie um programa que leia continuamente a altura e o sexo de uma lista de
pessoas salvando todas as informações em listas, até que uma altura
negativa seja fornecida. Ao final, sabendo que a média de altura para as
mulheres brasileiras é de 1.60m e a dos homens brasileiros é de 1.73m,
escreva as seguintes informações:
a) quantas mulheres da lista estão acima da média nacional de altura
para mulheres, e quantas estão abaixo;
b) quantos homens da lista estão acima da média nacional de altura para
homens, e quantos estão abaixo.
"""


while True:
    altura, sexo, i, mulheres_altas, mulheres_baixas, homens_altos, homens_baixos = [], [], 1, 0, 0, 0, 0
    while i > 0:
        i = float(input("informe a altura da pessoa(digite um valor negativo para parar): "))
        if i < 0:
            break
        altura += [i]
        sex = input("informe o sexo da pessoa(M/F):")
        while sex != 'm' and sex != 'f':
            sex = input("não entendi\ninforme o sexo da pessoa(M/F):")
        sexo += [sex]
        if sex == 'f':
            if i > 1.6:
                mulheres_altas += 1
            elif i < 1.6:
                mulheres_baixas += 1
        if sex == 'm':
            if i > 1.73:
                homens_altos += 1
            elif i < 1.73:
                homens_baixos += 1

    print(f'detectamos {homens_altos} homens altos')
    print(f'detectamos {homens_baixos} homens baixos')
    print(f'detectamos {mulheres_altas} mulheres altas')
    print(f'detectamos {mulheres_baixas} mulheres baixas')
