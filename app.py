import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Inicialização da aplicação com suporte a multipages
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # Para deploy

app.layout = html.Div([
    dcc.Location(id="url"),
    html.Div([
        dash.page_container
    ])
])

if __name__ == "__main__":
    app.run(debug=True, port=8050)
