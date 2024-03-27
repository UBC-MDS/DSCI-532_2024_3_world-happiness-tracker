from dash import Dash, html, dash_table, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd

df_2019 = pd.read_csv("data/raw/2019.csv")


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.Br(),
    html.H1("World Happiness Tracker"),
    html.Label(["Country:"]),
    dcc.Dropdown(options=sorted(list(df_2019["Country or region"])), placeholder="Select a country...",
                 id="country-select"),
    dash_table.DataTable(
                         id="rank-table")
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
                "if": {"filter_query": "{{Country or region}} = {}".format(country)},
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

if __name__ == "__main__":
    app.run(debug=True)