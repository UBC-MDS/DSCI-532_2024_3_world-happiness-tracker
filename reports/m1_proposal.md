## Motivation and Purpose
Our Role: Creation of Teaching Tools   

Target Audience: Educational Dashboard for Students  

Exploring various methods to learn about happiness in the world is commonplace within educational contexts, encompassing fields such as psychology, sociology, and economics. We inhabit a world where comprehending and comparing global happiness is increasingly significant. With the expanding divide between technology and conventional education, this dashboard seeks to bridge that gap by integrating technological tools into educational settings, thereby enhancing students understanding of happiness around the globe.  

The ability to visually interact with this dashboard enables students to see different regions and countries happiness scores, as well as the factors contributing to these specific scores, through a variety of filters. Students will also gain an understanding of how a country or region's happiness scores compare to global averages and how these scores have evolved over recent years  

## Description of Data  
For our visualization, we will use data spanning from 2015 to 2019, comprising approximately 156 rows (countries) for each year. This brings the total to 782 rows. The dataset includes various columns that indicate a country's happiness ranking and score, as well as the factors contributing to this score. The included columns are:

1. Country: String values that will appear five times, once for each year. 

3. Happiness Ranking: Integer values ranging from 1 to 156, representing the country’s happiness ranking globally. Each ranking will appear five times, as the same ranking can be assigned to different years.  

4. Happiness Score: Continuous values that typically range between 7.8 and 2.8, with higher scores indicating greater happiness according to the data.  

5. The following columns: GDP per capita, Family, Life Expectancy, Freedom, Generosity, and Trust (Government Corruption), are continuous variables. They detail the extent to which these factors contribute to a country's happiness score. These variables can be interpreted as coefficients and will range between 0 and 2.  
  
Utilizing this data, we will create certain columns such as a year column and a reverse-engineered version of the following variables: GDP per capita, Family, Life Expectancy, Freedom, Generosity, and Trust (Government Corruption), to provide additional, more interpretable data points. This will aid in better understanding the impact of various factors on a country's Happiness Score.
