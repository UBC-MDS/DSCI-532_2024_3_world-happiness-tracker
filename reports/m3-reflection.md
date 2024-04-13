# World Happiness Tracker App Dashboard Reflection (Milestone 3)

During the second milestone, our team managed to implement all of the proposed features with some changes (documented in `m2-reflection.md`). Hence, this week, we focused more on refinements, which involve deviations from the original proposal. These changes include the following:

- The theme was changed from `dbc.themes.BOOTSTRAP` to `dbc.themes.MINTY` for better font.
- The overall color scheme is now blue and yellow . This applies to the plots and the header. The key numbers have also been changed to blue. Having a consistent color theme makes the dashboard more professional.
- The background color was set to light gray.
- Charts are now placed inside cards. All cards now are white in color, which contrasts well with the light gray background and makes the dashboard look clean, neat and easy on the eye.
- The key numbers have been rearranged into the order of: happiest, unhappiest, difference of maximum and minimum happiness score, and the median happiness score.
- The year selection widget now no longer has the blue line on the slider up to the selected year, which previously made it look like a range instead of a single value.
- We have taken inspiration from Group 18's Vancouver Airbnb Listings dashboard and added a navigation bar for our header. This bar includes an collapsible "About" section for description about the application, and a clickable GitHub link to our repository.
- There is now a new footer, with the author names and the last deployed date repositioned.
- Page margin is adjusted for better visual.

As described above, most of the changes made this week make the app more neat and easier to read, making it a more effective tool in conveying information to the target audience. The dashboard also looks more professional, and hence also more trustworthy, which is important for the purpose of education which was described in the original proposal.

The repository was restructured as well. Previously all the source code resided in the single `app.py` file. Now they have been divided into several parts:

- `assets/custom.css`: file for including custom CSS styling
- `callbacks/`: callback functions, which are further divided into three files based on similar functionality
- `components/`: dashboard components, organized into four files (`cards.py`, `charts.py`, `filter.py`, and `navbar.py`)
- `data/`: script which preprocesses raw data into proper format to be used in the dashboard, stored in `data.py`
- `utils/`: global variables to be accessed by multiple functions, stored in `global_variables.py`

Compared to last week, our dashboard now bears a much more appealing and professional appearance, and it meets our expectations functionality-wise. Still, there are areas that could be improved. First, the two dropdown filters currently only allow two countries to be selected at once. We switch to a single filter that allows the selection of multiple countries. The filter should also allow a limit to be set on the maximum number of countries selected. Another possible improvement is to allow the map to be clicked on to select countries.
