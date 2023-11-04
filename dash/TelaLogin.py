from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd

TelaLogin = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

TelaLogin.layout = html.Div([
    html.Link(rel='stylesheet', href='/assets/estilo.css'),
    html.H1("Dashboard de Controle de Estoque"),
    html.P("Bem-vindo ao nosso aplicativo de controle de estoque."),
    dcc.Graph(id='grafico-estoque'),
])

@TelaLogin.callback(
    Output('grafico-estoque', 'figure'),
    Input('seletor-data', 'value')
)
if __name__ == '__main__':
    app.run_server(debug=True)