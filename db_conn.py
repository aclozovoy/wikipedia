def conn():

    import pymysql

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
    category VARCHAR(250),
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

    # COMMIT CHANGES
    cursor.connection.commit()
    cursor.fetchall()

    return cursor