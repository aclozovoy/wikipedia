def api_data(subject,start_date,end_date):

    import pandas as pd

    # WRITE URL STRING FOR API CALL
    base = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/'
    subject = subject.replace(" ", "_")
    interval = '/daily/'
    start_date = start_date + '/'
    end_date = end_date
    url = base + subject + interval + start_date + end_date
    

    df_json = pd.read_json(url)
  
    # Create empty dataframe
    df = pd.DataFrame(columns = ['Date', 'Views'])

    for index, row in df_json.iterrows():
        df.at[index,'Date'] = row.loc['items']['timestamp']
        df.at[index,'Views'] = row.loc['items']['views']

    df = df.dropna()

    return df