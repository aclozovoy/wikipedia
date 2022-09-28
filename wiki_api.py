

import datetime
cur_date = datetime.datetime.now().strftime('%Y%m%d')
begin_date = '20220101'

file = 'wiki_page_list.txt'

# Make text file into a list
my_file = open(file, "r")
data = my_file.read()
my_file.close()
subjectlist = data.split("\n")

# CONNECT TO DATABASE
from db_conn import conn
cursor = conn()


for row in subjectlist:
    subject = row.split('|')[0]
    taglist = row.split('|')[1:]
    print(subject)

    # CHECK DATA ALREADY IN DATABASE
    from db_view import db_view
    latest = db_view(subject, cursor)

    if latest == '11111111':
        start_date = begin_date
    else:
        start_date = latest

    # GET DATA FROM WIKIPEDIA API
    from api_data import api_data
    df = api_data(subject,start_date,cur_date)

    # LOAD DATA INTO DATABASE
    from db_load import load
    load(df, subject, taglist, cursor)
