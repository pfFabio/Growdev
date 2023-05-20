"""
 Faça um programa, com uma função que necessite de um argumento. A
função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’,
se seu argumento for zero ou negativo
"""

def positivo_negativo(A):
    if A > 0:
        return 'P'
    return 'N'

retorno = positivo_negativo(1)
print(retorno)
