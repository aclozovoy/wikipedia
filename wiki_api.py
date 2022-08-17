
file = 'test.txt'
tag = 'tester'

# Make text file into a list
my_file = open(file, "r")
data = my_file.read()
my_file.close()
subjectlist = data.split("\n")

# CONNECT TO DATABASE
from db_conn import *
cursor = conn()


for subject in subjectlist:
    print(subject)
    tag = tag

    # CHECK DATA ALREADY IN DATABASE
    from db_view import *
    latest = db_view(subject, cursor)

    # GET DATA FROM WIKIPEDIA API
    from api_data import *
    pageid, title, df = api_data(subject)#,start_date,end_date)

    # LOAD DATA INTO DATABASE
    from db_load import *
    load(df, pageid, title, tag, cursor)
