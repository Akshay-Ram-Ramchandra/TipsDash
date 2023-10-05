import dash

from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px

dash.register_page(__name__, path='/LinearRegression')

layout = dbc.Container([
    dbc.Row([
        dbc.Col([html.H1(children='Linear Regression', style={'textAlign': 'center'})])]),

    dbc.Row([
        dbc.Col([html.H3(
            [
                "Linear Regression is a very simple Machine Learning (ML) Model that attempts to learn a "
                "function "
                "that is a Linear combination of the input features."]
        )])

    ]),

    dbc.Row([
        dcc.Markdown([
            """$f_{w, b}(x) = wx + b$ (1) represents a model where: $w$ is a D-dimensional vector of parameters. $b$ is a real number. Here, the notation $ f_{w, b} $ signifies that the model $ f $ is parametrized by two values: $w$ and $b$."""
        ], mathjax=True)

    ]),
    dbc.Row([
        dbc.Col([
            "Below is a demonstration of the effect of changing the parameters w and b on a regression line."
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label("Select w Value"),
            dcc.Slider(
                id='w-slider',
                min=-20,
                max=20,
                step=0.1,
                value=0,
                marks={i: str(i) for i in range(-20, 20)},
                tooltip={'placement': 'top'}
            ),
            dbc.Label("Select b Value"),
            dcc.Slider(
                id='b-slider',
                min=-20,
                max=20,
                step=0.1,
                value=1,
                marks={i: str(i) for i in range(-20, 20)},
                tooltip={'placement': 'top'}
            )
        ])
    ]),

    dbc.Row([
        dcc.Graph(id="Demo", style={'height': '80vh', 'width': '100%'})
    ])
],

    style={'marginTop': '5%'},
    fluid=False

)


@callback(
    Output("Demo", "figure"),
    Input("w-slider", "value"),
    Input("b-slider", "value")
)
def update_graph(w, b):
    x = [i for i in range(-100, 100)]
    y = [((w * i) + b) for i in x]
    fig = px.line(x=x, y=y, labels={'x': 'X', 'y': 'Y'})

    # Set the x and y axis ranges explicitly
    fig.update_xaxes(range=[-50, 50])
    fig.update_yaxes(range=[-50, 50])  # Adjust the range as needed

    fig.add_shape(
        type="line",
        x0=-50,
        x1=50,
        y0=0,
        y1=0,
        line=dict(color="black", width=2)
    )
    fig.add_shape(
        type="line",
        x0=0,
        x1=0,
        y0=-50,
        y1=50,
        line=dict(color="black", width=2)
    )

    # Customize the appearance of the graph
    fig.update_traces(line=dict(color="blue", width=2))
    fig.update_layout(
        title=f"Equation: y = {w} * x + {b}",
        xaxis=dict(title="X", showgrid=False, ticks="inside", tickvals=[0], ticktext=[0]),


        yaxis=dict(title="Y", showgrid=False),
        plot_bgcolor="white",
        paper_bgcolor="white",
        hovermode="x unified",
    )

    return fig
