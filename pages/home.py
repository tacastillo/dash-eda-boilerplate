import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from app import app

content = """
# Exploratory Data Analysis Boilerplate
## Introduction
This is some simple boilerplate code to perform exploratory data analysis on any data set using Plotly Dash.
"""

layout = dbc.Container([
    dbc.Row(
        [
            dcc.Markdown(content)
        ]
    ),
], fluid=True)