


def carrega_dados(nome_arquivo):
    lista = []
    arquivo = open(nome_arquivo, 'r')
    conteudo =  arquivo.readlines()
    cabecalho = conteudo[0].split(',')
    conteudo.remove(conteudo[0])
    for i in range(len(conteudo)):
        conteudo[i] = conteudo[i].replace('\n', '')
        formatado = conteudo[i].split(',')
        lista += [{
            'nome': formatado[0],
            'ano': int(formatado[1]),
            'escola': formatado[2],
            'nota_semestre1': float(formatado[3]),
            'nota_semestre2': float(formatado[4]),
            'faltas': int(formatado[5]),
            'nota_exame': float(formatado[6]),
            'monitoria': formatado[7]
        }]

    return lista, cabecalho