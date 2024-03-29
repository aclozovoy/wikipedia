def conn():

    import pymysql

    host = 'acl-database.cl7ay4156fuf.us-west-2.rds.amazonaws.com'
    user = 'admin'

    try:
        with open('localpass.txt') as f:
            password = f.readline().strip('\n')

    connection = pymysql.connect(
                    host = host,
                    user = user,
                    password = password)

    cursor = connection.cursor()


    # USE DATABASE
    sql = '''USE wikidata'''
    cursor.execute(sql)
    cursor.fetchall()


    # DROP TABLE
    # sql = "DROP TABLE IF EXISTS pageviews"
    # cursor.execute(sql)
    # cursor.fetchall()

    # sql = "DROP TABLE IF EXISTS tags"
    # cursor.execute(sql)
    # cursor.fetchall()

    # cursor.connection.commit()
    # cursor.fetchall()

 
    # CREATE PAGEVIEWS TABLE
    sql = '''
    CREATE TABLE IF NOT EXISTS pageviews (
    pageviews_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    page_name VARCHAR(250) NOT NULL,
    viewdate DATE NOT NULL,
    views INT NOT NULL,
    entered_at TIMESTAMP DEFAULT NOW()
    )
    '''
    cursor.execute(sql)
    cursor.fetchall()

    # CREATE TAGS TABLE
    sql = '''
    CREATE TABLE IF NOT EXISTS tags (
    tags_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tag VARCHAR(100) NOT NULL,
    page_name VARCHAR(250) NOT NULL,
    entered_at TIMESTAMP DEFAULT NOW()
    )
    '''
    cursor.execute(sql)
    cursor.fetchall()



    # COMMIT CHANGES
    cursor.connection.commit()
    cursor.fetchall()

    return cursor