# World Happiness Tracker App Dashboard Reflection

All of our purposed features have been implemented, with some of them being slightly different than our initial designs. We initially proposed 3 key metrics at the top that are invariable regardless of which year is selected, but we believe that as user applies changes to any of the gadgets, they would expect most of if not all of the sections of the dashboard to undergo some changes as well, which is why we have now made the key metrics dynamic to the year selected. Additionally, we believe it is also an interesting statistic showing the gap between the highest and the lowest countries in terms of the happiness score, which we have added as another key metric on top of the proposed 3. Compared to the initial design, the filters now appear on top of these key metrics because we think this visualization is better.

The map remains the same as our initial design, that shows the happiness score for each country/region, and is also subject to the change of years. Another big change we made compared to the proposal of the ranking table. The table initially was going to be below the map and along with two other charts, however, due to its size and for the sake of readability, we have moved it to the right. This table, depends on the user selection with the two countries drop-down tabs, displays different things:

- When both of them are selected, the table shows only these two countries and their ranking.
- When one of the countries is selected (either country 1 or country 2), that country, along with the happiest and the unhappiest countries, are displayed, so that the user may be able to see where this country stands compared to the maximum and minimum. Only two countries are displayed if either the happiest or the unhappiest country is selected.

This table changes contents depending on the year selected.

Finally, the two summary charts remain roughly the same. As in our proposal:

- The line plot shows the happiness over time for 1 (if only one country is selected) or 2 (if both countries are selected) countries, with the happiness score of the selected year highlighted. If no country is selected, the line displays the global average over time instead.

- The bar chart shows how each component contributes to the happiness score. It is subject to the year change, and also behaves similarly with respect to the countries selected to the line plot.

So far, all features behave the exact way we expect them too. The current dashboard, while meets our demands in the proposal, is aesthetically unpleasing. Given that our goal is to create good visualizations, we will likely need to enhance the visual details to make it more appealing.