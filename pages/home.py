import dash
from dash import html
from components.navbar import Navbar

dash.register_page(__name__, path="/")

layout = html.Div([
    Navbar(),
    
    # Introdução
    html.Div([
        html.H4("Bem-vindo ao assistente financeiro", style={"textAlign": "center", "marginTop": "20px"}),
        html.P(
            "Nosso objetivo é ajudar você na escolha dos melhores ativos para compor sua carteira. "
            "Com base no seu interesse fazemos uma análise inicial que é de grande valor para o processo de tomada de decisão.",
            style={"textAlign": "center", "maxWidth": "80%", "margin": "0 auto"}
        ),
    ], style={"marginBottom": "40px"}),
    
    # Conteúdo em blocos 2x2
    html.Div(
        style={
            "display": "grid",
            "gridTemplateColumns": "50% 50%",
            "gridTemplateRows": "auto auto",
            "gap": "20px",
            "padding": "0 5%",
            "backgroundColor": "#eee",
            "paddingBottom": "90px"
        },
        children=[
            # Imagem Média Móvel
            html.Div([
                html.Img(
                src="/assets/media_movel_precos.png",  # Certifique-se de que a imagem está mesmo em /assets/
                style={"width": "100%", "maxWidth": "500px", "margin": "0 auto", "display": "block"}
            )
            ], style={"display": "flex", "alignItems": "center", "justifyContent": "center"}),

            # Explicação Média Móvel
            html.Div([
                html.P(
                    "📈 **Média móvel**: servem de suporte ao processo de tomada de decisão de compra e venda de ativos. "
                    "Elas são calculadas por meio da média dos preços de fechamento dos ativos em um determinado período.",
                    style={"fontSize": "16px"}
                )
            ], style={"padding": "20px", "display": "flex", "alignItems": "center"}),

            # Explicação Bandas de Bollinger
            html.Div([
                html.P(
                    "📊 **Bandas de Bollinger**: servem de suporte ao processo de tomada de decisão de compra e venda de ativos. "
                    "Elas são calculadas com base em uma média móvel e um desvio padrão, permitindo observar quando o ativo "
                    "está sobrecomprado ou sobrevendido.",
                    style={"fontSize": "16px"}
                )
            ], style={"padding": "20px", "display": "flex", "alignItems": "center"}),

            # Imagem Bandas de Bollinger
            html.Div([
                html.Img(
                src="/assets/bandas_bollinger.png",  # Certifique-se de que a imagem está mesmo em /assets/
                style={"width": "100%", "maxWidth": "500px", "margin": "0 auto", "display": "block"}
            )
            ], style={"display": "flex", "alignItems": "center", "justifyContent": "center"}),
        ]
    )
])
