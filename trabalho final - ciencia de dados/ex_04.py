lista, mulheres, compras_mulheres_2014 = [], 0, 0
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
    if i['sexo'] == 'F' and  i['ano'] == 2014:
            compras_mulheres_2014 += i['compra']


print(f'4) as mulheres gastaram um total R${compras_mulheres_2014:.2f}')