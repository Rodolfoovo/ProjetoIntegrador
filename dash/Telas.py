from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
    
app = Dash(__name__, external_stylesheets=external_stylesheets),

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='DashBoard', value='tab-1'),
        dcc.Tab(label='Relatorio', value='tab-2'),
        dcc.Tab(label='Rank Produtos', value='tab-3'),
        dcc.Tab(label='Entrada e Saida de estoque', value='tab-4'),
        dcc.Tab(label='Produtos', value='tab-5'),
        dcc.Tab(label='Gerenciar Usuarios', value='tab-6'),
    ]),
    html.Div(id='tabs-content'),
    html.Div([
        generate_table(df),
    ])
])

@callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('DashBoard'),
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Relatorios'),
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Relatorios'),
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3('Relatorios'),
        ])
    elif tab == 'tab-5':
        return html.Div([
            html.H3('Relatorios'),
        ])
    elif tab == 'tab-6':
        return html.Div([
            html.H3('Relatorios'),
        ])
    elif tab == 'tab-7':
        return html.Div([
        ])



if __name__ == '__main__':
    app.run(debug=True)