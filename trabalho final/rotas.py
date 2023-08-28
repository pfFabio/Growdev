from flask import render_template, request
import pandas as pd

arquivo = pd.read_csv("tabela-fipe-historico-precos.csv")
arquivo = arquivo.dropna()
arquivo['anoModelo'] = arquivo['anoModelo'].astype('Int16')
arquivo['anoReferencia'] = arquivo['anoReferencia'].astype('Int16')
arquivo['mesReferencia'] = arquivo['mesReferencia'].astype('Int8')

registros_por_pagina = 10
serie = None

def formata(palavra):
    match palavra:
        case 'codigoFipe': return 'Código FIPE'
        case 'marca': return "Marca"
        case 'modelo': return 'Modelo'
        case 'mesReferencia': return "Mês de Referencia"
        case 'anoReferencia': return "Ano de Referencia"
        case "anoModelo": return "Ano do Modelo"
        case "valor": return "Valor"

def index():
    return render_template('index.html')

def filtro():

    query = ""

    fipe_check = request.form.get('fipe_check')
    marca_check = request.form.get('marca_check')
    modelo_check = request.form.get('modelo_check')
    ano_modelo_check = request.form.get('ano_modelo_check')
    mes_referencia_check = request.form.get('mes_referencia_check')
    ano_referencia_check = request.form.get('ano_referencia_check')
    valor_check = request.form.get('valor_check')


    if fipe_check:
        query += ' and ' if query != '' else ''
        fipe_valor = str(request.form.get('fipe_valor'))
        query += f'codigoFipe == "{fipe_valor}"'

    if marca_check:
        query += ' and ' if query != '' else ''
        marca_valor = request.form.get('marca_valor')
        query += f'marca == "{marca_valor}"'
    
    if modelo_check:
        query += ' and ' if query != '' else ''
        modelo_valor = request.form.get('modelo_valor')
        query += f'modelo == "{modelo_valor}"'
    
    if ano_modelo_check:
        query += ' and ' if query != '' else ''
        ano_modelo_comparador = request.form.get('ano_modelo_comparador')
        ano_modelo_valor = request.form.get('ano_modelo_valor')
        query += f'anoModelo {ano_modelo_comparador} {ano_modelo_valor}'
    
    if mes_referencia_check:
        query += ' and ' if query != '' else ''
        mes_referencia_comparador = request.form.get('mes_referencia_comparador')
        mes_referencia_valor = request.form.get('mes_referencia_valor')
        query += f'mesReferencia {mes_referencia_comparador} {mes_referencia_valor}'
    
    if ano_referencia_check:
        query += ' and ' if query != '' else ''
        ano_referencia_comparador = request.form.get('ano_referencia_comparador')
        ano_referencia_valor = request.form.get('ano_referencia_valor')
        query += f'anoReferencia {ano_referencia_comparador} {ano_referencia_valor}'
    
    if valor_check:
        query += ' and ' if query != '' else ''
        valor_comparador = request.form.get('valor_comparador')
        valor_valor = request.form.get('valor_valor')
        query += f'valor {valor_comparador} {valor_valor}'



    if len(query) > 0:
        arquivo_filtrado = arquivo.query(query)
    else:
        arquivo_filtrado = arquivo.head()


    return render_template('filtro.html', arquivo = arquivo_filtrado)


def agrupamento():
    coluna = ''
    coluna = request.form.get('coluna')
    equacao = request.form.get('equacao')
    
    if coluna != None and coluna != '':
        arquivo_agrupado = arquivo.filter(items = [coluna, 'valor'])
        if equacao == 'max':
            arquivo_agrupado = arquivo_agrupado.groupby([coluna], as_index=False)['valor'].max()
        elif equacao == "min":
            arquivo_agrupado = arquivo_agrupado.groupby([coluna], as_index=False)['valor'].min()
        elif equacao == "media":
            arquivo_agrupado = arquivo_agrupado.groupby([coluna], as_index=False)['valor'].mean()
        elif equacao == "desvio_padrao":
            arquivo_agrupado = arquivo_agrupado.groupby([coluna], as_index=False)['valor'].std()
    else:
        coluna = "codigoFipe"
        arquivo_agrupado = arquivo.filter(items = [coluna, 'valor'])
        arquivo_agrupado = arquivo_agrupado.groupby(coluna, as_index=False)['valor'].max()
    

    coluna = formata(coluna)
    return render_template('grouping.html', arquivo = arquivo_agrupado, variavel = coluna, desvio = False)

def info():
    informacao = request.form.get('informacao')
    formula = request.form.get('formula')
    serie = arquivo
    tamanho_arquivo = len(arquivo)
    if formula == 'max':
        serie = arquivo.sort_values(informacao, ascending=False)  
    elif formula == "min":
        serie = arquivo.sort_values(informacao)  
    elif formula == "media":
        objetivo = arquivo[informacao].mean()
        informacao_att = formata(informacao)
        return render_template('info_media', objetivo = objetivo, informacao_att = informacao_att)

    page = int(request.args.get('page', 1))  # Página atual (padrão: 1)
    start = (page - 1) * registros_por_pagina
    end = start + registros_por_pagina

    serie = serie[start:end]
    total_paginas = len(serie) // registros_por_pagina + 1

    
    return render_template('infos.html', serie = serie, page=page, total_paginas=total_paginas, tamanho_arquivo = tamanho_arquivo)

