from dash import Dash, html, dash_table, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

df_2019 = pd.read_csv("data/raw/2019.csv")

factors = ["GDP per capita", "Social support", "Healthy life expectancy",
           "Freedom to make life choices", "Generosity", "Perceptions of corruption"]
df_2019["sum"] = df_2019[factors].sum(axis=1)
df_2019[factors] = df_2019[factors].div(df_2019["sum"], axis=0)
df_2019.drop(columns=["sum"], inplace=True)


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.Br(),
    html.H1("World Happiness Tracker"),
    html.Br(),
    html.Label(["Country:"]),
    dcc.Dropdown(options=sorted(list(df_2019["Country or region"])), placeholder="Select a country...",
                 id="country-select"),
    html.Br(),
    dash_table.DataTable(id="rank-table"),
    html.Br(),
    dcc.Graph(id="factors-graph")
])

@callback(
    Output("rank-table", "data"),
    Output("rank-table", "style_data_conditional"),
    Input("country-select", "value")
)
def update_table(country):
    if country:
        country_rank = df_2019.loc[df_2019["Country or region"] == country, "Overall rank"].tolist()[0]
        output_df = df_2019.loc[df_2019["Overall rank"] >= country_rank - 2]
        output_df = output_df.loc[output_df["Overall rank"] <= country_rank + 2]
        output_df = output_df[["Overall rank", "Country or region", "Score"]]
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(country_rank)},
                "backgroundColor": "orange",
                "color": "white"
            }
        ]
    else:
        output_df = df_2019[["Overall rank", "Country or region", "Score"]].head(10)
        style = [
            {
                "if": {"filter_query": "{{Overall rank}} = {}".format(output_df["Overall rank"].min())},
                "backgroundColor": "lime",
            }
        ]

    return output_df.to_dict("records"), style


@callback(
    Output("factors-graph", "figure"),
    Input("country-select", "value")
)
def update_contributing_factors(country):
    if country:
        factors_df = df_2019.loc[df_2019["Country or region"] == country]        
    else:
        factors_df = df_2019.copy()
    factors_df = factors_df[factors].melt(value_vars=factors, var_name="Factors", value_name="Proportion")

    fig = px.histogram(factors_df, x="Proportion", y="Factors", histfunc="avg")
    fig.update_layout(yaxis={"categoryorder": "mean ascending"},
                      xaxis_title="Proportion of Contribution", yaxis_title="Factors",
                      title="Factors Contributing to Happiness Index")

    return fig


if __name__ == "__main__":
    app.run(debug=True)