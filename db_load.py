def load(df, title, taglist, cursor):

    import pymysql
    import pandas as pd


    # INSERT INTO PAGEVIEWS TABLE
    for index, row in df.iterrows():

        curdate = str(row[0])
        curdate = curdate[0:4] + '-' + curdate[4:6] + '-' + curdate[6:8]

        views = str(int(row[1]))
        sql = '''
        INSERT INTO pageviews(page_name, viewdate, views)
        SELECT * FROM (SELECT '{}' AS page_name, '{}' AS viewdate, {} AS views) AS temp
        WHERE NOT EXISTS (SELECT page_name, viewdate FROM pageviews WHERE page_name = '{}' AND viewdate = '{}') LIMIT 1;
        '''.format(title,curdate,views,title,curdate)
        cursor.execute(sql)
        cursor.fetchall()
    
    # INSERT INTO TAGS TABLE
    for tag in taglist:
        sql = '''
        INSERT INTO tags(tag, page_name)
        SELECT * FROM (SELECT '{}' AS tag, '{}' AS page_name) AS temp
        WHERE NOT EXISTS (SELECT tag, page_name FROM tags WHERE tag = '{}' AND page_name = '{}') LIMIT 1;
        '''.format(tag,title,tag,title)
        cursor.execute(sql)
        cursor.fetchall()

    # COMMIT CHANGES
    cursor.connection.commit()
    cursor.fetchall()