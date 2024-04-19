from dash import dcc
import dash_bootstrap_components as dbc
from data import happiness_data


country1_dropdown = dcc.Dropdown(options=sorted(list(set(happiness_data["Country"]))),
                                 placeholder="Select Country 1...",
                                 id="country1-select")
country2_dropdown = dcc.Dropdown(options=sorted(list(set(happiness_data["Country"]))),
                                 placeholder="Select Country 2...",
                                 id="country2-select")
year_slider = dcc.Slider(min=2015, max=2019, value=2019,
                         marks={i: "{}".format(i) for i in range(2015,2020)},
                         step=1, included=False, id="year-select",
                         className='slider-class')
