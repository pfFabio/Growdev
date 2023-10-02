from dash.html import Div
from dash.dcc import Graph, Dropdown, RangeSlider, Checklist
from callback import SQL_pandas

lista_games = SQL_pandas('games')
lista_de_games = lista_games['Game'].drop_duplicates().to_list()
colunas_df = lista_games.columns.to_list()
colunas_df.remove('Year')
colunas_df.remove('Month')

nova_lista = [{'label': jogo, 'value': jogo} for jogo in lista_de_games]

body = Div(
    id= 'body',
    children = [
        Div(
            className='texto',
            children=[
                'Escolha os jogos, um ano e um mês para formar o gráfico'
            ]
        ),
        Div(
            id = 'filtros',
            children = [
                Div(
                    className= 'filtro ',
                    children = [
                        Dropdown(
                            id = 'lista_games',
                            options= lista_de_games ,
                            value=['League of Legends', 'Dota 2'],
                            multi=True,                    
                        ),
                    ]
                ),
                Div(
                    className= 'filtro',
                    children = [
                        Dropdown(
                            id = 'ano',
                            options= [2016,2017,2018,2019,2020,2021,2022],
                            value= 2016
                        ),
                    ]
                )
            ]
        ),
        RangeSlider(
            id = 'mes',
            min = 1,
            max = 12,
            step = 1,
            value= [1]
        ),
        Graph(
            id = 'grafico_1'
        ),

        Div(
            className= 'texto',
            children=[
                'A seguir escolha um jogo, uma informação e um ano para formar o gráfico'
            ]

        ),
        Div(
            className= 'filtro ',
            children = [
                Dropdown(
                    id = 'jogo',
                    options= lista_de_games ,
                    value='League of Legends',                 
                ),
            ]
        ),

        Div(
            className= 'filtro',
            children = [
                Dropdown(
                    id = 'coluna',
                    options= colunas_df,
                    value= 'Hours_streamed',
                    placeholder='Escolha 1 informação para ser o eixo do gráfico'
                )
            ]
        ),
        Div(
            className= 'filtro',
            children = [
                Dropdown(
                    id = 'ano2',
                    options= [2016,2017,2018,2019,2020,2021,2022],
                    value= 2016
                )
            ]
        ),
        Graph(
            id = 'grafico_2'
        ),                
    ]
)