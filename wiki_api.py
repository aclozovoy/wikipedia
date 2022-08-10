import requests
import json
import pandas as pd

 
subject = 'Python (programming language)'
url = 'https://en.wikipedia.org/w/api.php'
params = {
        'action': 'query',
        'format': 'json',
        'titles': subject,
        'prop': 'pageviews',
        'pvipdays': 60,
    }
 
r = requests.get(url, params=params)
data = r.json()

# Page id
temp = data['query']['pages']
pageid = list(temp.keys())[0]

# Title
title = data['query']['pages'][str(pageid)]['title']

# Viewcount data
clean = data['query']['pages'][str(pageid)]['pageviews']
print(clean)

# Move data from dictionary to DataFrame
df = pd.DataFrame(clean.items(), columns = ['Date', 'Views'])
print(df)






# url = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Albert_Einstein/daily/2013100100/2015103100'
# df2 = pd.read_json(url)
# print(df2)

