from dash import Input, Output, callback
import plotly.express as px
import plotly.graph_objects as go
from data import happiness_data
from utils import FACTORS, COLORS


@callback(
    Output("world-map", "figure"),
    Input("country1-select", "value"),
    Input("year-select", "value")
)
def update_map(country1, year):
    map_df = happiness_data.loc[happiness_data["Year"] == year]
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
    output_df = happiness_data.loc[happiness_data["Year"] == year]
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
       grouped_df = happiness_data[happiness_data["Country"].isin([country1, country2])]
       y_point_1 = grouped_df.loc[(grouped_df["Year"] == year) & (grouped_df["Country"] == country1), "Score"]
       y_point_2 = grouped_df.loc[(grouped_df["Year"] == year) & (grouped_df["Country"] == country2), "Score"]
       fig = px.line(grouped_df, x="Year", y="Score", color = 'Country', color_discrete_sequence=COLORS, markers=True)
       fig.add_trace(go.Scatter(x=[year], y=y_point_1, mode = "markers", name="Selected Year",
                                 marker=dict(color='red', size=15)))
       fig.add_trace(go.Scatter(x=[year], y=y_point_2,  mode = "markers", showlegend=False,
                                 marker=dict(color='red', size=15)))
    
    elif country1:
        grouped_df = happiness_data.loc[happiness_data["Country"] == country1]
        y_points = grouped_df.loc[grouped_df["Year"] == year, "Score"]
        fig = px.line(grouped_df, x="Year", y="Score", color = 'Country', color_discrete_sequence=COLORS, markers=True)
        fig.add_trace(go.Scatter(x=[year], y=y_points, mode = "markers", name="Selected Year",
                                    marker=dict(color='red', size=15)))
        
        
    elif country2:
        grouped_df = happiness_data.loc[happiness_data["Country"] == country2]
        y_points = grouped_df.loc[grouped_df["Year"] == year, "Score"]
        fig = px.line(grouped_df, x="Year", y="Score", color = 'Country', color_discrete_sequence=COLORS, markers=True)
        fig.add_trace(go.Scatter(x=[year], y=y_points, mode = "markers", name="Selected Year",
                                    marker=dict(color='red', size=15)))
        
        
    else:
        grouped_df = happiness_data[['Score', 'Year']].groupby(['Year']).mean().reset_index()
        fig = px.line(grouped_df, x="Year", y="Score", color_discrete_sequence=COLORS, markers=True)
        y_points = grouped_df.loc[grouped_df["Year"] == year, "Score"]
        fig.add_trace(go.Scatter(x=[year], y=y_points, mode = "markers", name="Selected Year",
                                    marker=dict(color='red', size=15)))
        fig.update_traces(showlegend=False)
        fig.data[0]['name'] = 'Global average'

    
    last_year = happiness_data["Year"].max()
    fig.update_xaxes(range=[happiness_data["Year"].min() - 0.5, last_year + 0.5])  

    
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))

  
    fig.update_layout(
        margin=dict(l=20, r=20, t=60, b=20),
        xaxis_title="Year",
        yaxis_title="Happiness Score",
        showlegend=False,
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
    factors_df = happiness_data.loc[happiness_data["Year"] == year]
    
    if (country1 and country2) or (country1) or (country2):

        if country1 and country2:
            factors_df = factors_df[factors_df["Country"].isin([country1, country2])]
        elif country1:
            factors_df = factors_df.loc[factors_df["Country"] == country1]
        elif country2:
            factors_df = factors_df.loc[factors_df["Country"] == country2]
 
        factors_df = factors_df.melt(id_vars = ["Country"], value_vars=FACTORS, var_name="Factors", value_name="Proportion")
        fig = px.histogram(factors_df, x="Proportion", y="Factors", color = 'Country', histfunc="avg", barmode="group",
                           color_discrete_sequence=COLORS)
    
    else:
        factors_df = factors_df[FACTORS].melt(value_vars=FACTORS, var_name="Factors", value_name="Proportion")
        fig = px.histogram(factors_df, x="Proportion", y="Factors", histfunc="avg", color_discrete_sequence=COLORS)
        fig.update_traces(showlegend=False)
        fig.data[0]['name'] = 'Global average'

    fig.update_layout(yaxis={"categoryorder": "mean ascending"},
                      xaxis_title="Proportion of Contribution", 
                      yaxis_title="",
                      showlegend=False)
                      #legend_title="Legend")

    return fig
