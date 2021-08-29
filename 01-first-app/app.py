# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# For styling options visit https://codepen.io/chriddyp/pen/bWLwgP.css
app = dash.Dash(__name__, title='My Analytics Dashboard')

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Create a figure
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# .layout what the app looks like and is a hierarchical tree of components
app.layout = html.Div([
    # Header
    html.Div(
        className="app-header",
        children=[
            html.Div('My First Dash App', className="app-header--title")
        ]
    ),
    # Insert image
    html.Div([
        html.Img(src='/assets/hdm-logo.jpg', style={'height':'5%', 'width':'5%'})
    ]),
    # Subheader and simple text
    html.Div(
        children=html.Div([
            html.H5('Analytics Dashboard'),
            html.Div('''
                This is an example of a simple Dash app with
                local, customized CSS.
            ''')
        ])
    ),
    # Insert graph
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)