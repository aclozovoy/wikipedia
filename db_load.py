def load(df, pageid, title, tag, cursor):

    import pymysql
    import pandas as pd

    # INSERT INTO PAGES
    sql1 = "INSERT INTO pages (wiki_id,page_name,category) "
    sql2 = "SELECT * FROM (SELECT " + pageid + " AS wiki_id, '" + title + "' AS page_name, '" + tag + "' AS category) AS temp "
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