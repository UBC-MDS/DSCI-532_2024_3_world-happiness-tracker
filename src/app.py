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
    [dbc.CardBody([
        html.P("Happiest Country"),
        html.Br(),
        html.H4("[  country_name (score)  ]")
    ])],
    color="#ececec",
    style={"border": 0, "height": 200}
)
card_median = dbc.Card([dbc.CardBody([
        html.P("Median Happiness Score"),
        html.Br(),
        html.H4("[  score  ]")
    ])],
    color="#ececec",
    style={"border": 0, "height": 200}
)
card_unhappiest = dbc.Card([dbc.CardBody([
        html.P("Unhappiest Country"),
        html.Br(),
        html.H4("[  country_name (score)  ]")
    ])],
    color="#ececec",
    style={"border": 0, "height": 200}
)
card_range = dbc.Card([dbc.CardBody([
        html.P("Score Difference between Happiest and Unhappiest Country"),
        html.H4("[  range  ]")
    ])],
    color="#ececec",
    style={"border": 0, "height": 200}
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
    Output("world-map", "figure"),
    Input("country1-select", "value"),
    Input("year-select", "value")
)
def update_map(country1, year):
    map_df = df_all.loc[df_all["Year"] == year]
    # map_df["show"] = "No"
    fig = px.choropleth(map_df, locations="Country", color="Score", locationmode="country names",
                        title="World Map of Happiness Scores")
    fig.update_layout(margin=dict(l=0, r=80, b=0, t=50))
    # if country1:
    #     map_df.loc[map_df["Country"] == country1, "show"] = "Yes"
    #     fig.add_trace(px.choropleth(map_df,locations="Country", color="show",locationmode="country names",# showlegend = False,
    #                                 color_discrete_sequence=["rgba(255,255,255,0.75)", "rgba(255,255,255,0)"]).data[0],
    #                                 showlegend=False)
    
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
    if country1 and country2:
        # pasting code for no countries selected for now; change code in this condition
        output_df = output_df[["Overall rank", "Country", "Score"]].head(10)
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(output_df["Overall rank"].min())},
                "backgroundColor": "lime",
            }
        ]
    elif country1:
        # pasting code for no countries selected for now; change code in this condition
        country_rank = output_df.loc[output_df["Country"] == country1, "Overall rank"].tolist()[0]
        output_df = output_df.loc[output_df["Overall rank"] >= country_rank - 2]
        output_df = output_df.loc[output_df["Overall rank"] <= country_rank + 2]
        output_df = output_df[["Overall rank", "Country", "Score"]]
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(country_rank)},
                "backgroundColor": "orange",
                "color": "white"
            }
        ]
    elif country2:
        # pasting code for no countries selected for now; change code in this condition
        output_df = output_df[["Overall rank", "Country", "Score"]].head(10)
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(output_df["Overall rank"].min())},
                "backgroundColor": "lime",
            }
        ]
    else:
        output_df = output_df[["Overall rank", "Country", "Score"]].head(10)
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(output_df["Overall rank"].min())},
                "backgroundColor": "lime",
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
