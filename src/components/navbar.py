from dash import html
import dash_bootstrap_components as dbc


about_text_style = {'display': 'none', 'backgroundColor': '#006AA7', 'color': 'white', 'padding': '10px'}

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("GitHub", href="https://github.com/UBC-MDS/DSCI-532_2024_3_world-happiness-tracker", target="_blank")),
        dbc.Button("About", id="open-about", color="secondary", className="ml-2"),
       
    ],
    brand="World Happiness Tracker",
    brand_href="#",
    id='custom-navbar', 
    color="primary",  
    dark=True,  
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
