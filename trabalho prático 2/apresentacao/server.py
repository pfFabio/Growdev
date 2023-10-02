
from dash import Dash
from dash.html import Div
from header import header
from body import body
from callback import registra_callback

app = Dash(__name__)
    

registra_callback(app)

app.layout = Div(
    style={'backgroundColor': '#e7ae78'},
    children= [
        header,
        body
    ]
)


app.run_server(debug=True, port=8080)

