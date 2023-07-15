#os dados vem em formato string do arquivo, essa função converte para formatos mais faceis de trabalhar
def converte_dado(dado,tipo):
    if tipo == int:
        return int(dado)
    elif tipo == float:
        return float(dado)
    elif tipo == bool:
        if dado == "True":
            return True
        else:
            return False
    return dado




#essa função le o arquivo e retorna uma lista de dicionários com cabeçalho
#note o uso da função converte_dado
def carrega_dados(nome_arquivo, separador, tipos):
    lista = []
    arquivo = open(nome_arquivo, 'r')
    conteudo =  arquivo.readlines()
    cabecalho = conteudo[0].replace('\n', '').split(separador)
    conteudo.remove(conteudo[0])

    for i in range(len(conteudo)):
        formatado = conteudo[i].replace('\n', '').split(separador)
        aluno = {}

        for index, tipo in enumerate(tipos):
            campo = cabecalho[index]
            aluno[campo] = converte_dado(formatado[index], tipo)

        lista += [aluno]

    return lista, cabecalho
