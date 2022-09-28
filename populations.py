import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents

# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
statestable=soup.find('table',{'class':"wikitable"})

df=pd.read_html(str(statestable))
# convert list to dataframe
df=pd.DataFrame(df[0])
print(df.head())


# drop the unwanted columns
# df = df.drop(["Rank", "Population(2001)"], axis=1)
df.columns = df.columns.map('_'.join)
for col in df.columns:
    print(type(col))
    print(col)

# print(df['State or Territory'])
df_states = pd.DataFrame(columns=['Territory', 'Population'])
df_states['Territory'] = df["State or territory_State or territory"]
df_states['Population'] = df["Census population[8][a]_July 1, 2021 (est.)"]

print(df_states)
df_states.to_csv('state_populations.csv','|')


#### COUNTRIES ###

# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
countriestable=soup.find('table',{'class':"wikitable"})

df=pd.read_html(str(countriestable))
# convert list to dataframe
df=pd.DataFrame(df[0])
print(df.head())


# drop the unwanted columns
# df = df.drop(["Rank", "Population(2001)"], axis=1)
# df.columns = df.columns.map('_'.join)
for col in df.columns:
    print(type(col))
    print(col)

# print(df['State or Territory'])
df_countries = pd.DataFrame(columns=['Territory', 'Population'])
df_countries['Territory'] = df['Country / Dependency']
df_countries['Population'] = df['Population']


print(df_countries)
df_countries.to_csv('country_populations.csv','|')