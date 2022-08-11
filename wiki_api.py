import requests
import pandas as pd
import pymysql
 

subject = 'Colorado'
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


connection = pymysql.connect(
                host = 'database-1.cl7ay4156fuf.us-west-2.rds.amazonaws.com',
                user = 'admin',
                password = '_7t6TKH!oJHQEHQ')

cursor = connection.cursor()


# USE DATABASE
sql = '''USE wikidata'''
cursor.execute(sql)
cursor.fetchall()

# DROP TABLE
# sql = "DROP TABLE IF EXISTS pages"
# cursor.execute(sql)
# cursor.fetchall()

# sql = "DROP TABLE IF EXISTS pageviews"
# cursor.execute(sql)
# cursor.fetchall()


# CREATE TABLE
sql = '''
CREATE TABLE IF NOT EXISTS pages (
pages_id INT NOT NULL AUTO_INCREMENT,
wiki_id INT NOT NULL,
page_name VARCHAR(250) NOT NULL,
entered_at TIMESTAMP DEFAULT NOW(),
PRIMARY KEY (pages_id)
)
'''
cursor.execute(sql)
cursor.fetchall()


# CREATE TABLE
sql = '''
CREATE TABLE IF NOT EXISTS pageviews (
pageviews_id INT NOT NULL AUTO_INCREMENT,
wiki_id INT NOT NULL,
viewdate DATE NOT NULL,
views INT NOT NULL,
entered_at TIMESTAMP DEFAULT NOW(),
PRIMARY KEY (pageviews_id)
)
'''
cursor.execute(sql)
cursor.fetchall()


# INSERT INTO PAGES
sql1 = "INSERT INTO pages (wiki_id,page_name) "
sql2 = "SELECT * FROM (SELECT " + pageid + " AS wiki_id, '" + title + "' AS page_name) AS temp "
sql3 = "WHERE NOT EXISTS (SELECT wiki_id FROM pages WHERE wiki_id = " + pageid + ") LIMIT 1;"
sql = sql1 + sql2 + sql3
cursor.execute(sql)
cursor.fetchall()


# INSERT INTO PAGEVIEWS
for index, row in df.iterrows():
    curdate = str(row[0])
    views = str(int(row[1]))
    sql1 = "INSERT INTO pageviews(wiki_id, viewdate, views) "
    sql2 = "SELECT * FROM (SELECT " + pageid + " AS wiki_id, '" + curdate + "' AS viewdate, " + views + " AS views) AS temp "
    sql3 = "WHERE NOT EXISTS (SELECT wiki_id, viewdate FROM pageviews WHERE wiki_id = " + pageid + " AND viewdate = '" + curdate + "') LIMIT 1;"
    sql = sql1 + sql2 + sql3
    cursor.execute(sql)
    cursor.fetchall()


# COMMIT CHANGES
cursor.connection.commit()
cursor.fetchall()