"""
Construa uma função que desenhe um retângulo usando os caracteres ‘+’ ,
‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo
que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se
valores fora da faixa forem informados, eles devem ser modificados para
valores dentro da faixa.
"""


minimo = 1
maximo = 20
desenha = ''

while True:
    linhas = int(input("qual a largura do retangulo?"))
    colunas = int(input("qual a altura do retangulo?"))
#garante o tamanho máximo do retangulo
    if linhas < minimo:
        linhas = minimo
    elif linhas > maximo:
        linhas = maximo
    if colunas < minimo:
        colunas = minimo
    elif colunas > maximo:
        colunas = maximo

#desenha linha superior
    desenha = '+'
    for i in range(linhas):
        desenha += '-'
    desenha += '+'
    print(desenha)

    #desenha linhas intermediarias
    for i in range(colunas - 2):
        desenha = '|'
        for i in range(linhas):
            desenha += ' '
        desenha += '|'
        print(desenha)

    #desenha linha inferior
    desenha = '+'
    for i in range(linhas):
        desenha += '-'
    desenha += '+'
    print(desenha)
