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

def desenha_linha(linhas,char_central, char_lateral):
    desenha = char_lateral
    for i in range(linhas):
        desenha += char_central
    desenha += char_lateral
    print(desenha)


def retangulo(linhas = 1, colunas = 1):
    desenha_linha(linhas, '-', '+')
    for i in range(colunas):
        desenha_linha(linhas, ' ', '|')
    desenha_linha(linhas, '-', '+')

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

    retangulo(linhas, colunas)

