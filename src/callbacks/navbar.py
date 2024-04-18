from dash import Input, Output, State, callback
import functools


@callback(
    Output("about-text", "style"),
    Input("open-about", "n_clicks"),
    State("about-text", "style"),
)
@functools.lru_cache()
def toggle_about(n, about_style):
    if n:
        if about_style and about_style.get('display') == 'none':
            about_style['display'] = 'block'  
        else:
            about_style['display'] = 'none'
    return about_style
