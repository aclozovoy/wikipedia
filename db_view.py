def db_view(subject, cursor):

    # FIND MOST RECENT DATE FOR CURRENT SUBJECT 
    sql1 = '''
    SELECT DATE_FORMAT(viewdate, '%Y%m%d') FROM pageviews
    JOIN pages
        ON pageviews.wiki_id = pages.wiki_id
    WHERE page_name =
    '''
    sql2 = " '" + subject + "' "
    sql3 = '''
    ORDER BY viewdate
    LIMIT 1;
    '''
    sql = sql1  + sql2 + sql3

    cursor.execute(sql)
    result = cursor.fetchall()

    latest = result[0][0]

    return latest