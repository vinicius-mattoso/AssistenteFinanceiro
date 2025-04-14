import dash
from dash import html, dcc, callback, Output, Input, State
from components.navbar import Navbar
from utils.openai_interface import consultar_chatgpt
import base64
import os

dash.register_page(__name__, path="/assistente")

layout = html.Div([
    Navbar(),

    html.Div([
        html.Div([
            html.H3("No que posso lhe ajudar hoje?", style={"textAlign": "center"}),

            dcc.Input(
                id="pergunta-input",
                type="text",
                placeholder="Ex: Como está as ações do Banco do Brasil no últimos 12 meses?",
                style={
                    "width": "100%",
                    "padding": "10px",
                    "border": "1px solid #ccc",
                    "borderRadius": "5px",
                    "marginTop": "10px"
                }
            ),

            # Botão centralizado
            html.Div([
                html.Button("Consultar", id="consultar-btn", n_clicks=0,
                            style={
                                "padding": "10px 20px",
                                "backgroundColor": "#2d5fa7",
                                "color": "white",
                                "border": "none",
                                "borderRadius": "5px",
                                "cursor": "pointer"
                            }),
            ], style={"display": "flex", "justifyContent": "center", "marginTop": "20px"}),

            html.Div(id="resposta-output", style={
                "marginTop": "30px",
                "fontSize": "18px",
                "textAlign": "justify",
                "maxWidth": "700px"
            }),

            html.Div(id="grafico-output", style={"marginTop": "30px"})
        ], style={
            "maxWidth": "800px",
            "margin": "0 auto",
            "padding": "40px",
            "border": "1px solid #ccc",
            "borderRadius": "10px",
            "boxShadow": "0px 0px 10px rgba(0,0,0,0.1)",
            "backgroundColor": "#f9f9f9"
        }),
    ], style={"padding": "40px"})
])


@callback(
    Output("resposta-output", "children"),
    Output("grafico-output", "children"),
    Input("consultar-btn", "n_clicks"),
    State("pergunta-input", "value"),
    prevent_initial_call=True
)
def responder_pergunta(n_clicks, pergunta):
    if not pergunta:
        return "Por favor, digite uma pergunta antes de consultar.", None

    resultado = consultar_chatgpt(pergunta)
    resposta_texto = resultado.get("resposta")
    caminho_grafico = resultado.get("grafico_salvo_em")

    grafico_html = None
    if caminho_grafico and os.path.exists(caminho_grafico):
        with open(caminho_grafico, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            grafico_html = html.Img(
                src=f"data:image/svg+xml;base64,{encoded}",
                style={"width": "100%", "maxWidth": "700px", "marginTop": "20px"}
            )

    return resposta_texto, grafico_html