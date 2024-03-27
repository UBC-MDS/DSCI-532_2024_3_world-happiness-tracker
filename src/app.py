from dash import Dash, html, dash_table
import pandas as pd

df_2019 = pd.read_csv("data/raw/2019.csv")


app = Dash(__name__)

app.layout = html.Div([
    html.Div(children="World Happiness Tracker"),
    dash_table.DataTable(data=df_2019[["Overall rank", "Country or region", "Score"]].to_dict("records"))
])

if __name__ == "__main__":
    app.run(debug=True)