from dash import html, Input, Output, callback
import dash_bootstrap_components as dbc
from data import happiness_data


@callback(
    Output("card-happiest", "children"),
    Input("year-select", "value")
)
def update_card_happiest(year):
    df_card = happiness_data.loc[happiness_data["Year"] == year]
    max_score = df_card["Score"].max()
    happiest_country = df_card.loc[df_card["Score"] == max_score, "Country"].reset_index(drop=True)[0]

    card_body = dbc.CardBody([
        html.P(f"Happiest Country ({year})"),
        html.Br(),
        html.H3(f"{happiest_country}", style={"text-align": "center"}),
        html.H5(f"({max_score})", style={"text-align": "center", "font-style": "italic"})
    ])

    return card_body


@callback(
    Output("card-median", "children"),
    Input("year-select", "value")
)
def update_card_happiest(year):
    df_card = happiness_data.loc[happiness_data["Year"] == year]
    median_score = df_card["Score"].median()

    card_body = dbc.CardBody([
        html.P(f"Median Happiness Score ({year})"),
        html.Br(style={"line-height": "250%"}),
        html.H3(f"{median_score}", style={"text-align": "center"}),
    ])

    return card_body


@callback(
    Output("card-unhappiest", "children"),
    Input("year-select", "value")
)
def update_card_happiest(year):
    df_card = happiness_data.loc[happiness_data["Year"] == year]
    min_score = df_card["Score"].min()
    unhappiest_country = df_card.loc[df_card["Score"] == min_score, "Country"].reset_index(drop=True)[0]

    card_body = dbc.CardBody([
        html.P(f"Unhappiest Country ({year})"),
        html.Br(),
        html.H3(f"{unhappiest_country}", style={"text-align": "center"}),
        html.H5(f"({min_score})", style={"text-align": "center", "font-style": "italic"})
    ])

    return card_body


@callback(
    Output("card-range", "children"),
    Input("year-select", "value")
)
def update_card_happiest(year):
    df_card = happiness_data.loc[happiness_data["Year"] == year]
    max_score = df_card["Score"].max()
    min_score = df_card["Score"].min()
    score_range = round(max_score - min_score, 3)

    card_body = dbc.CardBody([
        html.P(f"Score Difference between Happiest and Unhappiest Country ({year})"),
        html.Br(),
        html.H3(f"{score_range}", style={"text-align": "center"}),
    ])

    return card_body
