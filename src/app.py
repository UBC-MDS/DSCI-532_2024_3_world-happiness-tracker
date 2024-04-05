from dash import Dash, html, dash_table, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



df_all = pd.read_csv("data/processed/app_data.csv")
factors = ["GDP per capita", "Social support", "Healthy life expectancy",
           "Freedom to make life choices", "Generosity", "Perceptions of corruption"]


# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Components
card_happiest = dbc.Card(
    color="#ececec",
    style={"border": 0, "height": 200},
    id="card-happiest"
)
card_median = dbc.Card(
    color="#ececec",
    style={"border": 0, "height": 200},
    id="card-median"
)
card_unhappiest = dbc.Card(
    color="#ececec",
    style={"border": 0, "height": 200},
    id="card-unhappiest"
)
card_range = dbc.Card(
    color="#ececec",
    style={"border": 0, "height": 200},
    id="card-range"
)
country1_dropdown = dcc.Dropdown(options=sorted(list(set(df_all["Country"]))),
                                 placeholder="Select Country 1...",
                                 id="country1-select")
country2_dropdown = dcc.Dropdown(options=sorted(list(set(df_all["Country"]))),
                                 placeholder="Select Country 2...",
                                 id="country2-select")
year_slider = dcc.Slider(min=2015, max=2019, value=2019,
                         marks={i: "{}".format(i) for i in range(2015,2020)},
                         step=1, id="year-select")
world_map = dcc.Graph(id="world-map")
table_title = html.P("Country Rankings")
rank_table = dash_table.DataTable(id="rank-table")
line_chart = dcc.Graph(id="line-chart")
factors_graph = dcc.Graph(id="factors-graph")


# Layout
app.layout = dbc.Container([
    html.Br(),
    html.H1("World Happiness Tracker"),
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
        dbc.Col(card_median),
        dbc.Col(card_unhappiest),
        dbc.Col(card_range)
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(world_map, width=8),
        dbc.Col([dbc.Row(table_title),
                 dbc.Row(rank_table)])
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(line_chart),
        dbc.Col(factors_graph)
    ]),
    html.Br(),
])


# Server side callbacks/reactivity
@callback(
    Output("card-happiest", "children"),
    Input("year-select", "value")
)
def update_card_happiest(year):
    df_card = df_all.loc[df_all["Year"] == year]
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
    df_card = df_all.loc[df_all["Year"] == year]
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
    df_card = df_all.loc[df_all["Year"] == year]
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
    df_card = df_all.loc[df_all["Year"] == year]
    max_score = df_card["Score"].max()
    min_score = df_card["Score"].min()
    score_range = round(max_score - min_score, 3)

    card_body = dbc.CardBody([
        html.P(f"Score Difference between Happiest and Unhappiest Country ({year})"),
        html.Br(),
        html.H3(f"{score_range}", style={"text-align": "center"}),
    ])

    return card_body


@callback(
    Output("world-map", "figure"),
    Input("country1-select", "value"),
    Input("year-select", "value")
)
def update_map(country1, year):
    map_df = df_all.loc[df_all["Year"] == year]
    fig = px.choropleth(map_df, locations="Country", color="Score", locationmode="country names",
                        color_continuous_scale=px.colors.sequential.Blues,
                        title="World Map of Happiness Scores")
    fig.update_layout(margin=dict(l=0, r=80, b=0, t=50))
    
    return fig


@callback(
    Output("rank-table", "data"),
    Output("rank-table", "style_data_conditional"),
    Input("country1-select", "value"),
    Input("country2-select", "value"),
    Input("year-select", "value")
)
def update_table(country1, country2, year):
    output_df = df_all.loc[df_all["Year"] == year]
    top_3 = output_df.head(3)['Country'].tolist()
    bottom_3 = output_df.tail(3)['Country'].tolist()
    if country1 and country2:
        countries_list = top_3 + bottom_3 + [country1, country2]
        output_df = output_df[["Overall rank", "Country", "Score"]].query("Country in @countries_list")
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(output_df["Overall rank"].min())},
                "font-weight": "bold",
            }
        ]
    elif country1:
        countries_list = top_3 + bottom_3 + [country1]
        country_rank = output_df.loc[output_df["Country"] == country1, "Overall rank"].tolist()[0]
        output_df = output_df.query("Country in @countries_list")
        output_df = output_df[["Overall rank", "Country", "Score"]]
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(country_rank)},
                "font-weight": "bold"
            }
        ]
    elif country2:
        countries_list = top_3 + bottom_3 + [country2]
        country_rank = output_df.loc[output_df["Country"] == country2, "Overall rank"].tolist()[0]
        output_df = output_df.query("Country in @countries_list")
        output_df = output_df[["Overall rank", "Country", "Score"]]
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(country_rank)},
                "font-weight": "bold"
            }
        ]
    else:
        output_df = output_df[["Overall rank", "Country", "Score"]].head(10)
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(output_df["Overall rank"].min())},
                "font-weight": "bold"
            }
        ]

    return output_df.to_dict("records"), style


@callback(
    Output("line-chart", "figure"),
    Input("country1-select", "value"),
    Input("country2-select", "value"),
    Input("year-select", "value")
)
def update_linechart(country1, country2, year):
    if country1 and country2:
        # pasting code for no countries selected for now; change code in this condition
        grouped_df = pd.DataFrame(df_all.groupby(["Year"])["Score"].mean()).reset_index()
        y_points = grouped_df.loc[grouped_df["Year"] == year, "Score"]
        fig = px.line(grouped_df, x="Year", y="Score", markers=True, title="Happiness Score over the Years")
        fig.add_trace(go.Scatter(x=[year], y=y_points, mode = "markers", name="Selected Year",
                                 marker_size = 15))
    elif country1:
        # pasting code for no countries selected for now; change code in this condition
        grouped_df = pd.DataFrame(df_all.groupby(["Year"])["Score"].mean()).reset_index()
        y_points = grouped_df.loc[grouped_df["Year"] == year, "Score"]
        fig = px.line(grouped_df, x="Year", y="Score", markers=True, title="Happiness Score over the Years")
        fig.add_trace(go.Scatter(x=[year], y=y_points, mode = "markers", name="Selected Year",
                                 marker_size = 15))
    elif country2:
        # pasting code for no countries selected for now; change code in this condition
        grouped_df = pd.DataFrame(df_all.groupby(["Year"])["Score"].mean()).reset_index()
        y_points = grouped_df.loc[grouped_df["Year"] == year, "Score"]
        fig = px.line(grouped_df, x="Year", y="Score", markers=True, title="Happiness Score over the Years")
        fig.add_trace(go.Scatter(x=[year], y=y_points, mode = "markers", name="Selected Year",
                                 marker_size = 15))
    else:
        grouped_df = pd.DataFrame(df_all.groupby(["Year"])["Score"].mean()).reset_index()
        y_points = grouped_df.loc[grouped_df["Year"] == year, "Score"]
        fig = px.line(grouped_df, x="Year", y="Score", markers=True, title="Happiness Score over the Years")
        fig.add_trace(go.Scatter(x=[year], y=y_points, mode = "markers", name="Selected Year",
                                 marker_size = 15))
    
    return fig


@callback(
    Output("factors-graph", "figure"),
    Input("country1-select", "value"),
    Input("country2-select", "value"),
    Input("year-select", "value")
)
def update_contributing_factors(country1, country2, year):
    factors_df = df_all.loc[df_all["Year"] == year]

    if country1 and country2:
        # does the same thing as if no countries are selected for now;
        #    change code in this condition
        pass
    elif country1:
        factors_df = factors_df.loc[factors_df["Country"] == country1]
    elif country2:
        # does the same thing as if no countries are selected for now;
        #    change code in this condition
        pass

    factors_df = factors_df[factors].melt(value_vars=factors, var_name="Factors", value_name="Proportion")

    fig = px.histogram(factors_df, x="Proportion", y="Factors", histfunc="avg")
    fig.update_layout(yaxis={"categoryorder": "mean ascending"},
                      xaxis_title="Proportion of Contribution", yaxis_title="Factors",
                      title="Factors Contributing to Happiness Index")

    return fig


# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=True)
