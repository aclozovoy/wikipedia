def db_view(subject, cursor):

    # FIND MOST RECENT DATE FOR CURRENT SUBJECT
    sql = '''
    SELECT DATE_FORMAT(viewdate, '%Y%m%d') FROM pageviews
    WHERE page_name = '{}'
    ORDER BY viewdate DESC
    LIMIT 1;
    '''.format(subject)

    cursor.execute(sql)
    result = cursor.fetchall()

    if result == ():
        latest = '11111111'
    else:
        latest = result[0][0]

    return latest