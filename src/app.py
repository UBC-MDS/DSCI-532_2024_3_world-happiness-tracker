from dash import Dash, html
import dash_bootstrap_components as dbc
from components.navbar import navbar, about_text
from components.filters import country1_dropdown, country2_dropdown, year_slider
from components.cards import card_happiest, card_median, card_range, card_unhappiest
from components.charts import world_map, rank_table, line_chart, factors_graph
import callbacks


# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])

server = app.server


# Layout
app.layout = dbc.Container([
    dbc.Row([
        navbar,
        about_text,
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            dbc.Row([
                dbc.Col(html.Label(["Country 1"])),
                dbc.Col(html.Label(["Country 2"])),
                dbc.Col(html.Label(["Year"]))
            ]),
            dbc.Row([
                dbc.Col(country1_dropdown),
                dbc.Col(country2_dropdown),
                dbc.Col(year_slider)
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(card_happiest),
                dbc.Col(card_unhappiest),
                dbc.Col(card_range),
                dbc.Col(card_median)
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(world_map, width=8),
                dbc.Col(rank_table),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(line_chart),
                dbc.Col(factors_graph)
            ]),
            html.Br(),
            html.Hr(),
            dbc.Row([
                dbc.Col([
                    html.P("Authors: Hongyang Zhang, Jerry Yu, Michelle Hunn, Paolo De Lagrave-Codina",
                        style={"font-size": "12px"})
                ]),
                dbc.Col([
                    html.P("Last deployed on April 12, 2024",
                        style={"font-size": "12px", "text-align": "right"})
                ])
            ])   
        ])
    ], style={'padding-left': 50,
              'padding-right': 50,
              'background-color': '#ececec'})
], style={'padding':0}, fluid=True)


# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=False)
