from dash import Dash, html
import dash_bootstrap_components as dbc
from components.navbar import navbar, about_text
from components.filters import country1_dropdown, country2_dropdown, year_slider
from components.cards import card_happiest, card_median, card_range, card_unhappiest
from components.charts import world_map, rank_table, line_chart, factors_graph
import callbacks


# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server


# Layout
app.layout = dbc.Container([
    navbar,
    about_text,
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
    html.P("*This dashboard only includes the countries that appear in the dataset of all 5 years. The remaining countries were then re-ranked.",
           style={"font-size": "12px"}),
    html.P("This app illustrates an overview of happiness in countries around the world across 5 years.",
           style={"font-size": "12px"}),
    html.P("Authors: Hongyang Zhang, Jerry Yu, Michelle Hunn, Paolo De Lagrave-Codina",
           style={"font-size": "12px"}),
    html.A("Link to GitHub Repository", href="https://github.com/UBC-MDS/DSCI-532_2024_3_world-happiness-tracker",
           target="_blank", style={"font-size": "12px"}),
    html.P("Last deployed on April 5, 2023",
           style={"font-size": "12px"})
])


# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=True)
