# World Happiness Tracker App Dashboard Reflection (Milestone 4)

## Changes for Milestone 4
Since Milestone 3, we have focused on two main areas: performance improvement and enhanced user experience. In terms of the performance, the dashboard no longer reads five separate csv files and no longer performs data preprocessing. Instead, the data preprocessing component was split into a separate script, which outputs a binary parquet file which is then loaded as the input for the dashboard. In addition, we used in-memory `lru_cache` to reduce the number of unnecessary repetitive calculations.

To improve user experience, the color of the year slide was changed to white for better visibility. Toolbars from Plotly were either simplified or removed for simpler navigation. The table now has a better layout, which displays more countries and highlights selected countries. The map has a new default color for missing values to better distinguish it from countries with low happiness scores. Furthermore, the map now has markers that indicate selected countries. We also added loading spinners for charts being updated. Finally, we implemented a tab icon and tab title.

## Deviations from Initial Idea
Compared the original sketch, our dashboard mostly follows the initial concept. However, the current version has an overall color scheme, a clickable button in the navigation bar for an about section, a link to the GitHub repository and an additional key metric card.

## Advantages
The app captures the essence of being easy to use for high school students. The visuals and filters are very intuitive, and the changes are automatic. For educational purposes, this provides a tool that can be used to gain a good understanding of world happiness.

## Limitations
The user cannot filter many countries (more than two) at the moment since we do not want the plots to be overloaded with information. Also, we removed the countries that are not present in all five years, meaning that potentially useful information could be missing.

## Possible Additions
Instead of merging five datasets from different years, we could use the year filter to access these datasets individually, making the dashboard more accurate. We could implement a mult-select filter for countries that limits the maximum number of countries selected by the user. We could include an option to keep a global average in the plots, allowing for easier comparisons between countries and the global average.

## Course Reflection
We found the one-on-one discussions the professor had with our group to be particularly helpful as we received feedback specific to our project. We had some difficulties in dashboard deployment after breaking the code into separate files, and would have appreciated more resources in this area to support us.
