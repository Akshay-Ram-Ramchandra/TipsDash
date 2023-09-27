import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
from flask import Flask

import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
server = Flask(__name__)
app = dash.Dash(name = __name__, server = server)
app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
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
