from dash import html, dcc
import dash_bootstrap_components as dbc

def Navbar():
    return dbc.Navbar(
        dbc.Container([
            dbc.NavbarBrand("Assistente Financeiro", className="ms-2 text-white"),
            dbc.Nav([
                dbc.Button("Home", href="/", color="primary", className="me-2"),
                dbc.Button("Assistente", href="/assistente", color="primary", className="me-2"),
                html.A(html.Img(src="https://cdn-icons-png.flaticon.com/512/25/25231.png", height="30px"),
                       href="https://github.com", target="_blank", className="me-2"),
                html.A(html.Img(src="https://cdn-icons-png.flaticon.com/512/174/174857.png", height="30px"),
                       href="https://linkedin.com", target="_blank"),
            ], className="ms-auto", navbar=True)
        ]),
        color="primary",
        dark=True,
        className="mb-4"
    )
