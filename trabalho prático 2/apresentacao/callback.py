from dash import  Output, Input
import pandas as pd
import plotly.express as px
import sqlalchemy

#função que cria conexão com o SQL e baixa o dataframe para trabalhar
def SQL_pandas(tabela):
    conn = None
    try:
        conn = sqlalchemy.create_engine(
            'mysql+mysqlconnector://root:@localhost:3306/stream?', 
            pool_recycle=3600)
        
        query = f'SELECT * FROM {tabela}'
        
        return pd.read_sql_query(query, conn)
    finally:
        if conn is not None:
            conn.dispose()


def registra_callback(app):
    @app.callback(
        Output('grafico_1', 'figure'),
        Output('grafico_2', 'figure'),
        Input('lista_games', 'value'),
        Input('ano', 'value'),
        Input('mes', 'value'),
        Input('ano2', 'value'),
        Input('coluna', 'value'),
        Input('jogo', 'value')
    )
    def render(lista_games, ano, mes, ano2, coluna,jogo):

        #carregamento das databases
        games = SQL_pandas('games')
        global_ = SQL_pandas('global')

        #criação da coluna usada pra determinar o tamanho dos itens no gráfico
        games['tamanho'] = games['Hours_watched'] / global_['Hours_watched'] * 100

        #limpeza da nova coluna pra evitar bugs
        games['tamanho'] = games['tamanho'].fillna(0.0000001)
        

        #filtragem por mes e ano
        games_ano = games[(games['Year'] == ano) & (games['Month'] == mes[0])]

        #filtragem por nome dos jogos e ordenando para que as cores não se modifiquem
        games_filtrados = games_ano[games_ano['Game'].isin(lista_games)].sort_values('Game')
        

        #montagem do gráfico
        fig = px.scatter(games_filtrados,
                        x='Streamers',
                        y='Hours_watched',
                        color='Game',
                        size='tamanho',
                        labels={
                            'Hours_watched': 'Horas assistidas'
                        },
                        hover_name= "Game"
        )

        #deixando o gráfico na palheta de cor
        fig.update_layout( paper_bgcolor = '#e7ae78', plot_bgcolor = '#87b2e8')

        #configurando os items do hover
        fig.update_traces(
            hovertemplate="Game: %{hovertext}<br>Horas assistidas: %{y:.2f} <br>Streamers: %{x:.2f}"
        )

        #para impedir que o nome do hover saia da posição desejada
        fig.update_traces(
            hoverlabel=dict(
                namelength=0
            )
        )

        fig.update_yaxes(range=[0, 350000000])    



        game_filtrado = games[(games['Year'] == ano2)& (games['Game'] == jogo)]
        print(game_filtrado)

        if coluna == None :
            fig2 = fig
        else:
            fig2 = px.bar(game_filtrado, x='Month', y=coluna)



        return fig,fig2

