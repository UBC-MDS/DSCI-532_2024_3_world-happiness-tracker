from dash import callback, Input, Output
import plotly.express as px
import plotly.graph_objects as go
from data import happiness_data
from utils import FACTORS, COLORS
import functools

@callback(
    Output("world-map", "figure"),
    Input("country1-select", "value"),
    Input("country2-select", "value"),
    Input("year-select", "value")
)
@functools.lru_cache()
def update_map(country1, country2, year):
    map_df = happiness_data.loc[happiness_data["Year"] == year]
    fig = px.choropleth(map_df, locations="Country", color="Score", locationmode="country names",
                        color_continuous_scale= px.colors.sequential.Blues
                        )
    fig.update_traces(hovertemplate='%{location} (%{z:.2f})')
    fig.update_layout(margin=dict(l=0, r=80, b=0, t=0), 
                      modebar_remove=['pan', 'toImage', 'select2d', 'lasso2d'],
                      geo=dict(landcolor = '#f9f4ec')
                      )
    
    highlights = px.scatter_geo(map_df.loc[map_df['Country'].isin([country1, country2])],
                         locations="Country", 
                         color_discrete_sequence=[COLORS[1], COLORS[1]], 
                         locationmode="country names")
    
    highlights.update_traces(
        marker=dict(size=12, symbol="x", line=dict(width=1)),
        selector=dict(mode="markers"),
        hovertemplate=None,
        hoverinfo= 'skip'
        )

    highlight_dict = highlights.data[0]
    highlight_dict['showlegend'] = False

    fig.add_trace(highlight_dict)
    return fig


@callback(
    Output("rank-table", "data"),
    Output("rank-table", "style_data_conditional"),
    Input("country1-select", "value"),
    Input("country2-select", "value"),
    Input("year-select", "value")
)
@functools.lru_cache()
def update_table(country1, country2, year):
    output_df = happiness_data.loc[happiness_data["Year"] == year]
    top_3 = output_df.head(3)['Country'].tolist()
    bottom_3 = output_df.tail(3)['Country'].tolist()
    highlight_color = COLORS[1]
    maximum_num_rows = 13
    
    if country1 and country2:
        countries_list = top_3 + bottom_3 + [country1, country2]
        placeholders_num = maximum_num_rows - len(set(countries_list))

        full_countries = output_df['Country'].to_list()
        filtered = [item for item in full_countries if item not in countries_list]

        if placeholders_num % 2:
            add_top = filtered[:placeholders_num//2+1]
            add_bottom = filtered[-placeholders_num//2:]
        else:
            add_top = filtered[:placeholders_num//2]
            add_bottom = filtered[-placeholders_num//2:]
        
        countries_list = countries_list + add_top + add_bottom
        
        output_df = output_df[["Overall rank", "Country", "Score"]].query("Country in @countries_list")
        rank_country_1 = output_df.loc[output_df["Country"] == country1, "Overall rank"].tolist()[0]
        rank_country_2 = output_df.loc[output_df["Country"] == country2, "Overall rank"].tolist()[0]
        style = [
            {
                "if": {"filter_query": f"{{Overall rank}} = {rank_country_1} || {{Overall rank}} = {rank_country_2}"},
                'backgroundColor': highlight_color,
                'color': 'white'
            }
        ]
    elif country1:
        countries_list = top_3 + bottom_3 + [country1]

        placeholders_num = maximum_num_rows - len(set(countries_list))

        full_countries = output_df['Country'].to_list()
        filtered = [item for item in full_countries if item not in countries_list]

        if placeholders_num % 2:
            add_top = filtered[:placeholders_num//2+1]
            add_bottom = filtered[-placeholders_num//2:]
        else:
            add_top = filtered[:placeholders_num//2]
            add_bottom = filtered[-placeholders_num//2:]
        
        countries_list = countries_list + add_top + add_bottom
        
        country_rank = output_df.loc[output_df["Country"] == country1, "Overall rank"].tolist()[0]
        output_df = output_df.query("Country in @countries_list")
        output_df = output_df[["Overall rank", "Country", "Score"]]
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(country_rank)},
                'backgroundColor': highlight_color,
                'color': 'white'
            }
        ]
    elif country2:
        countries_list = top_3 + bottom_3 + [country2]

        placeholders_num = maximum_num_rows - len(set(countries_list))

        full_countries = output_df['Country'].to_list()
        filtered = [item for item in full_countries if item not in countries_list]

        if placeholders_num % 2:
            add_top = filtered[:placeholders_num//2+1]
            add_bottom = filtered[-placeholders_num//2:]
        else:
            add_top = filtered[:placeholders_num//2]
            add_bottom = filtered[-placeholders_num//2:]
        
        countries_list = countries_list + add_top + add_bottom
        
        country_rank = output_df.loc[output_df["Country"] == country2, "Overall rank"].tolist()[0]
        output_df = output_df.query("Country in @countries_list")
        output_df = output_df[["Overall rank", "Country", "Score"]]
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(country_rank)},
                'backgroundColor': highlight_color,
                'color': 'white'
            }
        ]
    else:
        output_df = output_df[["Overall rank", "Country", "Score"]].head(maximum_num_rows)
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(output_df["Overall rank"].min())},
                'backgroundColor': highlight_color,
                'color': 'white'
            }
        ]

    return output_df.to_dict("records"), style


@callback(
    Output("line-chart", "figure"),
    Input("country1-select", "value"),
    Input("country2-select", "value"),
    Input("year-select", "value")
)
@functools.lru_cache()
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
        fig.update_traces(showlegend=True)
        fig.data[0]['name'] = 'Global average'

    
    last_year = happiness_data["Year"].max()
    fig.update_xaxes(range=[happiness_data["Year"].min() - 0.5, last_year + 0.5])  

    for trace in fig.data:
        trace.hovertemplate = '%{data.name}: %{y:.2f}<extra></extra>'

    
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))

  
    fig.update_layout(
        margin=dict(l=20, r=20, t=60, b=20),
        xaxis_title="Year",
        yaxis_title="Happiness Score",
        legend_title="",
        showlegend=True,
        hovermode="closest"
    )

    return fig


@callback(
    Output("factors-graph", "figure"),
    Input("country1-select", "value"),
    Input("country2-select", "value"),
    Input("year-select", "value")
)
@functools.lru_cache()
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
        fig.update_traces(showlegend=True)
        fig.data[0]['name'] = 'Global average'

    fig.update_traces(hovertemplate='%{x:.2f}')

    fig.update_layout(yaxis={"categoryorder": "mean ascending"},
                      xaxis_title="Proportion of Contribution", 
                      yaxis_title="",
                      legend_title="",
                      showlegend=True)

    return fig
