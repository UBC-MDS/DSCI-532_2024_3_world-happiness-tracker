# World Happiness Tracker App Dashboard Reflection (Milestone 3)

During the second milestone, our team managed to implement all of the proposed features with some changes (documented in `m2-reflection.md`). So, this week, we focused more on refinements. Some of the specific changes are:

- A new font.
- The overall color scheme is now blue and yellow. This applies to the plots and the header. The key numbers have also been changed to blue. There is also now a new grey background color.
- The key numbers have been rearranged into the order of: happiest, unhappiest, difference of maximum and minimum happiness score, and the median happiness score.
- The year selection widget now no longer has the line up to the selected year, which previously made it look like a range instead of a single value.
- Charts are now placed inside cards for better visuals.
- We have also taken inspiration from group 18's Vancouver Airbnb Listings and added a navigation bar for our header. This bar includes an collapsible "About" section for more information about the application, and a clickable Github link to our repository.
- There is now a new footer, with the author names and the last deployed date repositioned.
- We have turned off debug mode.
- Page margin is adjusted for better visual.

The repository is now restructured as well. Previously all the source code resided in the single `app.py` file. Now they have been broken down into several components:

- `assets`: file for including custom CSS styling
- `callbacks`: callback functions
- `components`: the main components in the dashboard (cards, charts, filter, and navbar)
- `data`: data preprocessing functions
- `utils`: global variables to be accessed by multiple functions

Compared to last week, our dashboard now bears a much more appealing aesthetics, and it meets our expectations functionality-wise. However, there is still plenty of room for improvements. The country selector is not very flexible, as it only allows two countries to be selected at once, and there is a drop-down menu for each one of the countries. We can definitely improve it to make it much more flexible, whether it is to be able to select more than 2 countries, or to at least make it a single menu so that the user can select multiple countries by checking multiple boxes, which is a much more intuitive way. We are also looking to make the map more interactive. The map is the biggest part of the dashboard and therefore should bear more functionalities than just displaying the happiness score by countries.