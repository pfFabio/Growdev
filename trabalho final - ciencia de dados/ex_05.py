
jovens, adultos, idosos = 0, 0, 0
jovens_gastos, adultos_gastos, idosos_gastos = 0, 0, 0
lista = []
nome_do_arquivo = 'compras - compras.csv'

arquivo = open(nome_do_arquivo, 'r')

conteudo = arquivo.readlines()
conteudo.remove(conteudo[0]) #removendo cabeçalho

for i in range(len(conteudo)):
    conteudo[i] = conteudo[i].replace('\n', '')
    formatado = [conteudo[i].split(',')]
    lista.append({  'nome':formatado[0][0],
                    'sobrenome':formatado[0][1],
                    'idade': int(formatado[0][2]),
                    'sexo': formatado[0][3],
                    'compra': float(formatado[0][4]),
                    'ano': int(formatado[0][5]),
                    'pagamento': formatado[0][6] })

for i in lista:
    if 18 <= i['idade'] <= 25:
        jovens += 1
        jovens_gastos += i['compra']
    elif 25 < i['idade'] <= 59:
        adultos += 1
        adultos_gastos += i['compra']
    elif 59 < i['idade']:
        idosos += 1
        idosos_gastos += i['compra']


if jovens_gastos <= idosos_gastos and adultos_gastos <= idosos_gastos:
    print('5) os idosos gastaram mais')
elif adultos_gastos <= jovens_gastos and idosos_gastos <= jovens_gastos:
    print('5) os jovens gastaram mais')
elif idosos_gastos <= adultos_gastos and jovens_gastos <= adultos_gastos:
    print('5) os adultos gastaram mais, isso pode estar relacionado a quantidade maior de membros nesse grupo')

print(f'podemos verificar que a proporção de pessoas pra gastos é mantida, aproximadamente, a mesma por exemplo:\n'
      f'a proporção de adultos para jovens é {adultos/jovens} e a de gastos é {adultos_gastos/jovens_gastos}\n'
      f'a proporção de adultos para jovens é {adultos/idosos} e a de gastos é {adultos_gastos/idosos_gastos}')
