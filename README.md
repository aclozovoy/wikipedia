# wikipedia
Track and visualize wikipedia page views over time

wiki_api.py is the main file which runs functions organized in api_data.py, db_conn.py, db_load.py, and db_view.py.


db_conn.py extablishes a connection with the MySQL Amazon RDS Server.

wiki_page_list.txt is a list of all of the Wikipedia pages we are interested in and their respective categories.

db_view.py looks at the current database values and determines which dates need data from the Wikipedia API.

api_data.py makes an API request for the applicable dates and stores the data in a Pandas DataFrame.

db_load.py loads the data from the API request into the MySQL database.

Tableau loads data from the MySQL database: https://public.tableau.com/app/profile/andrew.lozovoy/viz/WikipediaPageViews_16612873165990/InfoPage