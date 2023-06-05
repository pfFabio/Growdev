#retorna a soma de todos os dados de uma coluna
def somatorio(dados, coluna):
    soma = 0
    for registro in dados:
        soma += registro[coluna]
    return soma



#usa a função somatório em conjunto com o "len" para retornar a média da coluna
def media(dados, coluna):
    return somatorio(dados, coluna)/len(dados)