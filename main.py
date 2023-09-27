import dash
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
from flask import Flask
import pandas as pd

df = pd.read_csv('tips.csv')
server = Flask(__name__)
app = dash.Dash(name = __name__, server = server)
app.layout = dbc.Container([
    html.H1(children='Tips Dataset', style={'textAlign':'center'}),
    html.H3(children=str([i for i in df.columns ]), style={'textAlign':'center'}),
    # dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    # dff = df[df.country==value]
    return px.line(x=[1,2,3], y=[4,5,6])

if __name__ == '__main__':
    app.run(debug=True)
