import dash
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.io as pio
from flask import Flask
import pandas as pd
import os
import configparser

# server = Flask(__name__)
# app = dash.Dash(name=__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app.title = "CSCI453ML"

dash.register_page(__name__, path='/')
config = configparser.ConfigParser()
config.read('config.ini')
base_path = config['PATHS']['base']
print(base_path)

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