from dash import Dash, html, dash_table, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



df_all = pd.read_csv("data/processed/app_data.csv")
factors = ["GDP per capita", "Social support", "Healthy life expectancy",
           "Freedom to make life choices", "Generosity", "Perceptions of corruption"]
colors = ['#636EFA', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']


# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server


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
world_map = dbc.Card(children=[html.H5("World Map of Happiness Scores"),
                               dcc.Graph(id="world-map")],
                     body=True)
rank_table = dbc.Card(children=[html.H5("Country Rankings*"),
                                html.Br(),
                                dash_table.DataTable(id="rank-table")],
                      body=True,
                      style={"height":"100%"})
line_chart = dbc.Card(children=[html.H5("World Map of Happiness Scores"),
                                dcc.Graph(id="line-chart")],
                      body=True)
factors_graph = dbc.Card(children=[html.H5("Factors Contributing to Happiness Index"),
                                   dcc.Graph(id="factors-graph")],
                         body=True)


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
                        color_continuous_scale=px.colors.sequential.Blues)
    fig.update_layout(margin=dict(l=0, r=80, b=0, t=0))
    
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
    if (country1 and country2):
       grouped_df = df_all[df_all["Country"].isin([country1, country2])]
       y_point_1 = grouped_df.loc[(grouped_df["Year"] == year) & (grouped_df["Country"] == country1), "Score"]
       y_point_2 = grouped_df.loc[(grouped_df["Year"] == year) & (grouped_df["Country"] == country2), "Score"]
       fig = px.line(grouped_df, x="Year", y="Score", color = 'Country', color_discrete_sequence=colors, markers=True)
       fig.add_trace(go.Scatter(x=[year], y=y_point_1, mode = "markers", name="Selected Year",
                                 marker=dict(color='red', size=15)))
       fig.add_trace(go.Scatter(x=[year], y=y_point_2,  mode = "markers", showlegend=False,
                                 marker=dict(color='red', size=15)))
    
    elif country1:
        grouped_df = df_all.loc[df_all["Country"] == country1]
        y_points = grouped_df.loc[grouped_df["Year"] == year, "Score"]
        fig = px.line(grouped_df, x="Year", y="Score", color = 'Country', color_discrete_sequence=colors, markers=True)
        fig.add_trace(go.Scatter(x=[year], y=y_points, mode = "markers", name="Selected Year",
                                    marker=dict(color='red', size=15)))
        
        
    elif country2:
        grouped_df = df_all.loc[df_all["Country"] == country2]
        y_points = grouped_df.loc[grouped_df["Year"] == year, "Score"]
        fig = px.line(grouped_df, x="Year", y="Score", color = 'Country', color_discrete_sequence=colors, markers=True)
        fig.add_trace(go.Scatter(x=[year], y=y_points, mode = "markers", name="Selected Year",
                                    marker=dict(color='red', size=15)))
        
        
    else:
        grouped_df = df_all[['Score', 'Year']].groupby(['Year']).mean().reset_index()
        fig = px.line(grouped_df, x="Year", y="Score", color_discrete_sequence=colors, markers=True)
        y_points = grouped_df.loc[grouped_df["Year"] == year, "Score"]
        fig.add_trace(go.Scatter(x=[year], y=y_points, mode = "markers", name="Selected Year",
                                    marker=dict(color='red', size=15)))
        fig.update_traces(showlegend=True)
        fig.data[0]['name'] = 'Global average'

    
    last_year = df_all["Year"].max()
    fig.update_xaxes(range=[df_all["Year"].min() - 0.5, last_year + 0.5])  

    
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))

  
    fig.update_layout(
        margin=dict(l=20, r=20, t=60, b=20),
        xaxis_title="Year",
        yaxis_title="Happiness Score",
        legend_title="Legend",
        hovermode="closest"
    )

    return fig


@callback(
    Output("factors-graph", "figure"),
    Input("country1-select", "value"),
    Input("country2-select", "value"),
    Input("year-select", "value")
)
def update_contributing_factors(country1, country2, year):
    factors_df = df_all.loc[df_all["Year"] == year]
    
    if (country1 and country2) or (country1) or (country2):

        if country1 and country2:
            factors_df = df_all[df_all["Country"].isin([country1, country2])]
        elif country1:
            factors_df = factors_df.loc[factors_df["Country"] == country1]
        elif country2:
            factors_df = factors_df.loc[factors_df["Country"] == country2]
 
        factors_df = factors_df.melt(id_vars = ["Country"], value_vars=factors, var_name="Factors", value_name="Proportion")
        fig = px.histogram(factors_df, x="Proportion", y="Factors", color = 'Country', histfunc="avg", barmode="group", color_discrete_sequence=colors)
    
    else:
        factors_df = factors_df[factors].melt(value_vars=factors, var_name="Factors", value_name="Proportion")
        fig = px.histogram(factors_df, x="Proportion", y="Factors", histfunc="avg", color_discrete_sequence=colors)
        fig.update_traces(showlegend=True)
        fig.data[0]['name'] = 'Global average'

    fig.update_layout(yaxis={"categoryorder": "mean ascending"},
                      xaxis_title="Proportion of Contribution", 
                      yaxis_title="Factors",
                      legend_title="Legend")

    return fig


# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=True)
