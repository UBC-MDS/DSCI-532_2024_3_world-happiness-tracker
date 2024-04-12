import pandas as pd

df_2019 = pd.read_csv("data/raw/2019.csv").assign(Year=2019)
df_2018 = pd.read_csv("data/raw/2018.csv").assign(Year=2018)
df_2017 = pd.read_csv("data/raw/2017.csv").assign(Year=2017)
df_2016 = pd.read_csv("data/raw/2016.csv").assign(Year=2016)
df_2015 = pd.read_csv("data/raw/2015.csv").assign(Year=2015)

df_2019.rename(columns={"Country or region": "Country"}, inplace=True)
df_2018.rename(columns={"Country or region": "Country"}, inplace=True)
df_2017.rename(columns={"Happiness.Rank": "Overall rank", "Happiness.Score": "Score",
                        "Economy..GDP.per.Capita.": "GDP per capita", "Family": "Social support",
                        "Health..Life.Expectancy.": "Healthy life expectancy", "Freedom": "Freedom to make life choices",
                        "Trust..Government.Corruption.": "Perceptions of corruption"},
                        inplace=True)
df_2016.rename(columns={"Happiness Rank": "Overall rank", "Happiness Score": "Score", "Economy (GDP per Capita)": "GDP per capita",
                        "Family": "Social support", "Health (Life Expectancy)": "Healthy life expectancy",
                        "Freedom": "Freedom to make life choices", "Trust (Government Corruption)": "Perceptions of corruption"},
                        inplace=True)
df_2015.rename(columns={"Happiness Rank": "Overall rank", "Happiness Score": "Score", "Economy (GDP per Capita)": "GDP per capita",
                        "Family": "Social support", "Health (Life Expectancy)": "Healthy life expectancy",
                        "Freedom": "Freedom to make life choices", "Trust (Government Corruption)": "Perceptions of corruption"},
                        inplace=True)

df_2019 = df_2019[["Overall rank", "Country", "Score", "GDP per capita", "Social support", "Healthy life expectancy",
                    "Freedom to make life choices", "Generosity", "Perceptions of corruption", "Year"]]
df_2018 = df_2018[["Overall rank", "Country", "Score", "GDP per capita", "Social support", "Healthy life expectancy",
                    "Freedom to make life choices", "Generosity", "Perceptions of corruption", "Year"]]
df_2017 = df_2017[["Overall rank", "Country", "Score", "GDP per capita", "Social support", "Healthy life expectancy",
                    "Freedom to make life choices", "Generosity", "Perceptions of corruption", "Year"]]
df_2016 = df_2016[["Overall rank", "Country", "Score", "GDP per capita", "Social support", "Healthy life expectancy",
                    "Freedom to make life choices", "Generosity", "Perceptions of corruption", "Year"]]
df_2015 = df_2015[["Overall rank", "Country", "Score", "GDP per capita", "Social support", "Healthy life expectancy",
                    "Freedom to make life choices", "Generosity", "Perceptions of corruption", "Year"]]

countries_2019 = set(df_2019["Country"].tolist())
countries_2018 = set(df_2018["Country"].tolist())
countries_2017 = set(df_2017["Country"].tolist())
countries_2016 = set(df_2016["Country"].tolist())
countries_2015 = set(df_2015["Country"].tolist())
select_countries = countries_2019.intersection(countries_2018).intersection(countries_2017)\
    .intersection(countries_2016).intersection(countries_2015)\

df_2019 = df_2019.loc[df_2019["Country"].isin(select_countries)]
df_2018 = df_2018.loc[df_2018["Country"].isin(select_countries)]
df_2017 = df_2017.loc[df_2017["Country"].isin(select_countries)]
df_2016 = df_2016.loc[df_2016["Country"].isin(select_countries)]
df_2015 = df_2015.loc[df_2015["Country"].isin(select_countries)]

df_2019["Overall rank"] = list(range(1, len(df_2019)+1))
df_2018["Overall rank"] = list(range(1, len(df_2018)+1))
df_2017["Overall rank"] = list(range(1, len(df_2017)+1))
df_2016["Overall rank"] = list(range(1, len(df_2016)+1))
df_2015["Overall rank"] = list(range(1, len(df_2015)+1))

df_all = pd.concat([df_2019, df_2018, df_2017, df_2016, df_2015])
df_all["Score"] = df_all["Score"].round(3)

factors = ["GDP per capita", "Social support", "Healthy life expectancy",
           "Freedom to make life choices", "Generosity", "Perceptions of corruption"]
df_2019["sum"] = df_2019[factors].sum(axis=1)
df_2019[factors] = df_2019[factors].div(df_2019["sum"], axis=0)
df_2019.drop(columns=["sum"], inplace=True)

df_all["sum"] = df_all[factors].sum(axis=1)
df_all[factors] = df_all[factors].div(df_all["sum"], axis=0)
df_all.drop(columns=["sum"], inplace=True)


happiness_data = df_all
