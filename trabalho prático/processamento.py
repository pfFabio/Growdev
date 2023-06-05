
#retorna os valores de uma linha especifica
def localiza(lista, linha):
    if linha < len(lista):
        print(lista[linha])
        return lista[linha]
    else:
        print("erro")
        return None


#retorna uma lista que contem todas as linhas(dicionários) correspondentes a  um filtro
def filtrar(lista,coluna, operacao, valor):
    dados_filtrados = []
    if operacao == '==':
        for linha in lista:
            if linha[coluna] == valor:
                dados_filtrados += [linha]
    elif operacao == '>=':
        for linha in lista:
            if linha[coluna] >= valor:
                dados_filtrados += [linha]
    elif operacao == '<=':
        for linha in lista:
            if linha[coluna] <= valor:
                dados_filtrados += [linha]
    elif operacao == '>':
        for linha in lista:
            if linha[coluna] > valor:
                dados_filtrados += [linha]
    elif operacao == '<':
        for linha in lista:
            if linha[coluna] < valor:
                dados_filtrados += [linha]
    elif operacao == '!=':
        for linha in lista:
            if linha[coluna] != valor:
                dados_filtrados += [linha]
    return dados_filtrados

#retorna uma lista com as colunas requisitadas
def projetar(lista, coluna):
    projecao = []
    for linha in lista:
        linha_projetada = {}
        for campo, valor in linha.items():
            if campo in coluna:
                linha_projetada[campo] = valor
        projecao += [linha_projetada]
    return projecao

#atualiza os dados de acordo com a operação e o valor passados
def atualizacao(lista, coluna, operacao, valor, novo):
    if operacao == '==':
        for linha in lista:
            if linha[coluna] == valor:
                linha[coluna] = novo
    elif operacao == '>=':
        for linha in lista:
            if linha[coluna] >= valor:
                linha[coluna] = novo
    elif operacao == '<=':
        for linha in lista:
            if linha[coluna] <= valor:
                linha[coluna] = novo
    elif operacao == '>':
        for linha in lista:
            if linha[coluna] > valor:
                linha[coluna] = novo
    elif operacao == '<':
        for linha in lista:
            if linha[coluna] < valor:
                linha[coluna] = novo
    elif operacao == '!=':
        for linha in lista:
            if linha[coluna] != valor:
                linha[coluna] = novo


#filtra com a operação de "==" para economizar processamento
def filtro(lista, coluna, checa):
    grupo = []
    for linha in lista:
        if linha[coluna] == checa:
            grupo += [linha]
    return grupo

#analisa uma coluna e junta as linhas que nessa coluna tenham valores iguais
def prof_agrupar(dados,coluna):

    dados_agrupados = {}

    for linha in dados:
        valor_celula = linha[coluna]
        if dados_agrupados.get(valor_celula) == None:
            dados_agrupados[valor_celula] = []
        dados_agrupados[valor_celula].append(linha)

    return dados_agrupados

#cria ou atualiza um arquivo a partir da lista,cabeçalho e separador passados
def salvar_arquivo(nome_arquivo, separador, lista, cabecalho=None):
    arquivo = open(nome_arquivo, 'w')
    cabecalho_str = ''
    linha_str = ''
    for coluna in cabecalho:
        cabecalho_str += coluna
        if coluna != cabecalho[-1]:
            cabecalho_str += separador
    cabecalho_str += '\n'

    for linha in lista:
        for coluna, dado in linha.items():
            linha_str += str(dado)
            if coluna != cabecalho[-1]:
                linha_str += separador
        linha_str += '\n'
        arquivo.write(linha_str)

    arquivo.write(cabecalho_str)
    arquivo.close()

