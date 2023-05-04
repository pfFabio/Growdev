"""
Utilize as seguintes faixas etárias nos exercícios em que for necessário.
● Jovens, 18 a 25 anos
● Adultos, 26 a 59 anos
● Idosos, igual ou maior que 60 anos
Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
exercícios.
1) Qual a porcentagem de homens e mulheres na base de dados?
2) Qual foi o gasto por ano?
3) Qual foi o ano com maior gasto?
4) Qual foi o ano em que os homens mais usaram o crédito?
5) Procure quem foi a pessoa que mais gastou?
"""

def retorna_ano(e):
    return e['ano']

pessoas = {
    'nome': '',
    'gastos': 0
}

cadastro = {
    'nome': '',
    'sobrenome': '',
    'idade': 0,
    'sexo': '',
    'compra': 0,
    'ano': 0,
    'pagamento': ''
}

ano = {
    'ano': 0,
    'custo': 0,
    'credito homens': 0
}

homens, mulheres, lista, anos, baleias = 0, 0, [], [], []
baleia, baleia_carteira, ano_caro, caro, homens_caros, ano_homem = '', 0, 0, 0, 0, 0


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
#passando pela lista atras da resposta do exercicio
for i in lista:
#contando homens e mulheres
    if i['sexo'] == 'M':
        homens += 1
    elif i['sexo'] == 'F':
        mulheres += 1
#separando custos anuais
    controle = 0
    for j in anos:
        if j['ano'] == i['ano']:
            j['custo'] += i['compra']
            controle = 1
    if controle == 0:
        anos.append({'ano': i['ano'], 'custo': i['compra'], 'credito homens': 0})
#separando custo por pessoa
    controle = 0
    for k in baleias:
        if k['nome'] == i['nome']:
            k['gastos'] += i['compra']
            controle = 1
    if controle == 0:
        baleias.append({'nome': i['nome'], 'gastos': i['compra']})

#contando uso de crédito por homens
    if i['sexo'] == "M" and i['pagamento'] == 'credito':
        for j in anos:
            if j['ano'] == i['ano']:
                j['credito homens'] += 1
#procurando a baleia
    for i in baleias:
        if baleia_carteira < i['gastos']:
            baleia = i['nome']
            baleia_carteira = i['gastos']

anos.sort(key= retorna_ano)


print(f'1) temos uma proporção de: {(homens/(mulheres+homens)) * 100}% de homens e {(mulheres/(homens+mulheres) * 100)}% de mulheres')
print(f'2) segue a lista de anos e os respectivos custos')
for i in anos:
    print(f"      no ano {i['ano']} foi gasto R${i['custo']:.2f}")
    if caro < i['custo']:
        caro = i['custo']
        ano_caro = i['ano']
    if i['credito homens'] > homens_caros:
        ano_homem = i['ano']
        homens_caros = i['credito homens']

print(f'3) o ano com maior gasto foi {ano_caro} com custo de R${caro:.2f}')

print(f'4) o ano {ano_homem} foi aquele no qual os homens usaram credito mais vezes')

print(f'5) {baleia} foi a pessoa que mais gastou')
