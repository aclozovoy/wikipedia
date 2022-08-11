
 
subject = 'Arizona'
tag = 'state'

from api_data import *
pageid, title, df = api_data(subject)

from db_conn import *
cursor = conn()

from db_load import *
load(df, pageid, title, tag, cursor)
