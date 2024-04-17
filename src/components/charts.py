from dash import dash_table, html, dcc
import dash_bootstrap_components as dbc


world_map = dbc.Card(children=[html.H5("World Map of Happiness Scores"),
                               dcc.Graph(id="world-map")],
                     body=True)
rank_table = dbc.Card(children=[html.H5("Country Rankings"),
                                html.Br(),
                                dash_table.DataTable(id="rank-table")],
                      body=True,
                      style={"height":"100%"})
line_chart = dbc.Card(children=[html.H5("World Map of Happiness Scores"),
                                dcc.Graph(id="line-chart", config={'displayModeBar': False})],
                      body=True)
factors_graph = dbc.Card(children=[html.H5("Factors Contributing to Happiness Index"),
                                   dcc.Graph(id="factors-graph")],
                         body=True)
