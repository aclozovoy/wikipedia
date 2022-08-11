def api_data(subject):

    import requests
    import pandas as pd

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

    # Move data from dictionary to DataFrame
    df = pd.DataFrame(clean.items(), columns = ['Date', 'Views'])
    df = df.dropna()

    return pageid, title, df