import dash
from dash import Dash, html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container

from flask import Flask
import os

server = Flask(__name__)
app = Dash(__name__, use_pages=True,
           server=server,
           pages_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pages'),
           external_stylesheets=[dbc.themes.BOOTSTRAP])
navbar = dbc.Navbar(
    [
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.DropdownMenu(
                        children=[dbc.DropdownMenuItem('Home', href='/')] +
                        [
                                     dbc.DropdownMenuItem(page['name'], href=page['path'])
                                     for page in dash.page_registry.values() if page['name'] != 'Landing'
                                 ],
                        nav=True,
                        in_navbar=True,
                        label="Other Pages",
                        right=False,  # Move the dropdown to the right
                        direction="down"
                    ),
                ],
                className="ml-auto",  # Align menu to the right
                navbar=True,
            ),
            id="navbar-collapse",
            navbar=True,
        ),
        dbc.NavbarBrand("Machine Learning Fall 2023", href="#"),
    ],
    color="dark",
    dark=True,
    expand="lg",  # Expand to full width for the hamburger menu
    fixed="top",  # Fixed position at the top
)

app.layout = html.Div([
    navbar,
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)
