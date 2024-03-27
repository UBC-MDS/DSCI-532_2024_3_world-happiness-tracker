from dash import Dash, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

df_2019 = pd.read_csv("data/raw/2019.csv")


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1(children="World Happiness Tracker"),
    dash_table.DataTable(data=df_2019[["Overall rank", "Country or region", "Score"]].head(10).to_dict("records"))
])

if __name__ == "__main__":
    app.run(debug=True)