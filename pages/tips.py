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

dash.register_page(__name__, path='/tips')
config = configparser.ConfigParser()
config.read('config.ini')
base_path = config['PATHS']['base']


df = pd.read_csv(os.path.join(base_path, 'pages/tips.csv'))

df['bill_percent'] = (df['tip'] / df['total_bill']) * 100
pio.templates.default = 'plotly_white'
dconfig = {'displayModeBar': False}

layout = dbc.Container([
    dbc.Row([
        dbc.Col([html.H1(children='Tips Dataset', style={'textAlign': 'center'})])]),

    dbc.Row([html.H3(children="Availablecolumns:" + str([i for i in df.columns]), style={'textAlign': 'center'})]),

    dbc.Row([
        dbc.Col([html.H3("Plots", style={'textAlign': 'left'})])
    ]),
    dbc.Row([
        dbc.Col([html.H3("Question 7: Plot a histogram of the total_bill amounts. Label your axes appropriately.",
                         style={'textAlign': 'left'})])
    ]),

    dbc.Row([
        dbc.Col([dcc.Graph(id='q7',
                           figure=px.histogram(df,
                                               'total_bill',
                                               title="Distribution of total bill amount").update_xaxes(
                               title_text="Total Bill ($)").
                           update_yaxes(title_text="Count"),
                           config=dconfig,
                           style={'height': '90vh'})],
                )]),
    dbc.Row([
        dbc.Col(
            [html.H4("The distribution of tips is right skewed. Tips between 16-18 are the most common tip amounts.",
                     style={'textAlign': 'left'})])
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col([html.H3(
            "Create a scatter plot to visualize the relationship between the total_bill and tip. Label your axes and "
            "give your plot a title.",
            style={'textAlign': 'left'})])
    ]),

    dbc.Row([
        dbc.Col([dcc.Graph(id='q8',
                           figure=px.scatter(df,
                                             'total_bill',
                                             'tip',
                                             title="Total Bill by Tip").update_xaxes(title_text="Total Bill ($)").
                           update_yaxes(title_text="Tip ($)"),
                           config=dconfig,
                           style={'height': '90vh'})],
                )]),

    dbc.Row([
        dbc.Col([html.H4(
            "There is moderate correlation between the tip amount and the bill amount. It indicates that higher"
            "the bill amount, higher is the tips.",
            style={'textAlign': 'left'})])
    ]),

    html.Hr(),
    dbc.Row([
        dbc.Col([html.H3(
            "Question 9: Using a bar plot, visualize the average tip amount for each day of the week.",
            style={'textAlign': 'left'})])
    ]),

    dbc.Row([
        dbc.Col([dcc.Graph(id='q9',
                           figure=px.bar(df.groupby(['day'])['tip'].mean().reindex(['Thur', 'Fri', 'Sat', 'Sun']),
                                         title="Distribution of average tips,by day"
                                         ).update_xaxes(title_text="Day of the week").
                           update_yaxes(title_text="Average Tip ($)"),
                           config=dconfig,
                           style={'height': '90vh'})],
                )]),

    html.Hr(),

    dbc.Row([
        dbc.Col([html.H3(
            "Question 9: Using a bar plot, visualize the average tip amount for each day of the week.",
            style={'textAlign': 'left'})])
    ]),

    dbc.Row([
        dbc.Col([dcc.Graph(
            figure=px.box(df,
                          x='day',
                          y='tip',
                          title="Tips by day of the week",
                          color='day',
                          category_orders={'day': ['Thur', 'Fri', 'Sat', 'Sun']}
                          ).update_xaxes(title_text="Day of the week").
            update_yaxes(title_text="Tip ($)"),
            config=dconfig,
            style={'height': '90vh'})],
        )]),

    dbc.Row([
        dbc.Col([dcc.Graph(
            figure=px.box(df,
                          x='day',
                          y='bill_percent',
                          title="Percentage of tip by day of the week",
                          color='day',
                          category_orders={'day': ['Thur', 'Fri', 'Sat', 'Sun']}
                          ).update_xaxes(title_text="Day of the week").
            update_yaxes(title_text="Tip ($)"),
            config=dconfig,
            style={'height': '90vh'})],
        )]),

    dbc.Row([
        dbc.Col([dcc.Graph(
            figure=px.scatter(df,
                              x='total_bill',
                              y='tip',
                              title="Bill amount by tip; Colored by percentage",
                              color='bill_percent',
                              ).update_xaxes(title_text="Bill amount ($)").
            update_yaxes(title_text="Tip ($)"),
            config=dconfig,
            style={'height': '90vh'})],
        )]),

    dbc.Row([
        dbc.Col([dcc.Graph(
            figure=px.scatter(df,
                              x='tip',
                              y='bill_percent',
                              color='smoker',
                              title="Tip by Bill percentage; Colored by smoker",
                              ).update_xaxes(title_text="Tip ($)").
            update_yaxes(title_text="Percentage of bill"),
            config=dconfig,
            style={'height': '90vh'})],
        )]),

    dbc.Row([
        dbc.Col([dcc.Graph(
            figure=px.box(df,
                          x='time',
                          y='bill_percent',
                          color='time',
                          title="Tip by Bill percentage; Colored by time",
                          ).update_xaxes(title_text="Tip ($)").
            update_yaxes(title_text="Percentage of bill"),
            config=dconfig,
            style={'height': '90vh'})],
        )]),

    dbc.Row([
        dbc.Col([dcc.Graph(
            figure=px.histogram(df,
                                x='bill_percent',
                                title="Count of tip percentage",
                                marginal='box',
                                ).update_xaxes(title_text="Tip percentage").
            update_yaxes(title_text="Frequency"),
            config=dconfig,
            style={'height': '90vh'})],
        )]),

],
    fluid=False)

