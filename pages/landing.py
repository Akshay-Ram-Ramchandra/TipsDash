import dash
from dash import Dash, html, dcc, callback, Output, Input


# server = Flask(__name__)
# app = dash.Dash(name=__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app.title = "CSCI453ML"

dash.register_page(__name__, path='/')

layout = html.Div(
    [
        html.Div(
            [
                html.H1("Welcome to Akshay's Page", className="display-4"),
                html.P(
                    "This is a landing page for Akshay's personal page. "
                    "Feel free to explore the content and navigate to different sections.",
                    className="lead",
                ),
            ],
            className="container mt-5 pt-5 text-center",
        )
    ]
)