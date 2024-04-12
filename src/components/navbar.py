from dash import html
import dash_bootstrap_components as dbc
from utils import COLORS


about_text_style = {'display': 'none', 'backgroundColor': '#006AA7', 'color': 'white',
                    'padding-left': '50px', 'padding-top': '10px', 'padding-bottom': '10px'}

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("GitHub", href="https://github.com/UBC-MDS/DSCI-532_2024_3_world-happiness-tracker", target="_blank")),
        dbc.Button("About", id="open-about", color="secondary", className="ml-2", style={'border': '0px'}),
       
    ],
    brand="World Happiness Tracker",
    brand_href="#",
    brand_style={'font-size' : '40px',
                 'margin-left': 50},
    id='custom-navbar', 
    color="primary",  
    dark=True, 
    style={'border-radius': 5, 
           'padding-right': 50},
    fluid=True
)
about_text = html.Div(
    [
        html.P(
            [
                "This app illustrates an overview of happiness in countries around the world across 5 years.",
                html.Br(),
                "The dashboard only includes the countries that appear in the dataset of all 5 years. The remaining countries were then re-ranked.",
            ],
            id='about-text',
            style=about_text_style  
        )
    ],
    className='rounded-bottom'  
)
