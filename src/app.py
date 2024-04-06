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
world_map = dcc.Graph(id="world-map")
table_title = html.P("Country Rankings*")
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
    happiest = output_df.loc[output_df["Overall rank"] == output_df["Overall rank"].max(), "Country"].tolist()[0]
    unhappiest = output_df.loc[output_df["Overall rank"] == output_df["Overall rank"].min(), "Country"].tolist()[0]
    if country1 and country2:
        output_df = output_df[["Overall rank", "Country", "Score"]].query("Country == @country1 | Country == @country2")
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(output_df["Overall rank"].min())},
                "font-weight": "bold",
            }
        ]
    elif country1:
        country_rank = output_df.loc[output_df["Country"] == country1, "Overall rank"].tolist()[0]
        output_df = output_df.query("Country in [@happiest, @country1, @unhappiest]")
        output_df = output_df[["Overall rank", "Country", "Score"]]
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(country_rank)},
                "font-weight": "bold"
            }
        ]
    elif country2:
        country_rank = output_df.loc[output_df["Country"] == country2, "Overall rank"].tolist()[0]
        output_df = output_df.query("Country in [@happiest, @country2, @unhappiest]")
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
    fig = go.Figure()

    
    if country1:
        df_country1 = df_all[df_all["Country"] == country1]
        fig.add_trace(go.Scatter(x=df_country1["Year"], y=df_country1["Score"], mode='lines+markers', name=country1))
        if year in df_country1["Year"].values:  # Check if the selected year is within the data
            y_point_country1 = df_country1.loc[df_country1["Year"] == year, "Score"].values[0]
            fig.add_trace(go.Scatter(x=[year], y=[y_point_country1], mode='markers', name=f"{country1} {year}",
                                     marker=dict(color='red', size=15), showlegend=False))
    
    
    if country2:
        df_country2 = df_all[df_all["Country"] == country2]
        fig.add_trace(go.Scatter(x=df_country2["Year"], y=df_country2["Score"], mode='lines+markers', name=country2))
        if year in df_country2["Year"].values:  # Check if the selected year is within the data
            y_point_country2 = df_country2.loc[df_country2["Year"] == year, "Score"].values[0]
            fig.add_trace(go.Scatter(x=[year], y=[y_point_country2], mode='markers', name=f"{country2} {year}",
                                     marker=dict(color='red', size=15), showlegend=False))

    
    if not country1 and not country2:
        grouped_df = df_all.groupby("Year")["Score"].mean().reset_index()
        # Change mode to 'lines+markers' to see points for all years
        fig.add_trace(go.Scatter(x=grouped_df["Year"], y=grouped_df["Score"], mode='lines+markers', name='Global Average'))
        if year in grouped_df["Year"].values:  # Check if the selected year is within the data
            global_y_point = grouped_df.loc[grouped_df["Year"] == year, "Score"].values[0]
            fig.add_trace(go.Scatter(x=[year], y=[global_y_point], mode='markers', name=f"Global {year}",
                                     marker=dict(color='red', size=15), showlegend=False))

    
    last_year = df_all["Year"].max()
    fig.update_xaxes(range=[df_all["Year"].min() - 0.5, last_year + 0.5])  

    
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))

  
    fig.update_layout(
        margin=dict(l=20, r=20, t=60, b=20),
        title="Happiness Score Over the Years",
        xaxis_title="Year",
        yaxis_title="Happiness Score",
        legend_title="Country",
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
            factors_df = factors_df.loc[(factors_df["Country"] == country1) | (factors_df["Country"] == country2)]
        elif country1:
            factors_df = factors_df.loc[factors_df["Country"] == country1]
        elif country2:
            factors_df = factors_df.loc[factors_df["Country"] == country2]
        
        factors_df = factors_df.melt(id_vars = ["Country"], value_vars=factors, var_name="Factors", value_name="Proportion")
        fig = px.histogram(factors_df, x="Proportion", y="Factors", color = 'Country', histfunc="avg", barmode="group")
    

    else:
        factors_df = factors_df[factors].melt(value_vars=factors, var_name="Factors", value_name="Proportion")
        fig = px.histogram(factors_df, x="Proportion", y="Factors", histfunc="avg")

    fig.update_layout(yaxis={"categoryorder": "mean ascending"},
                      xaxis_title="Proportion of Contribution", 
                      yaxis_title="Factors",
                      title="Factors Contributing to Happiness Index")

    return fig


# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=False)
