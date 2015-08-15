import pandas as pd
import sqlalchemy as sa

# name of the CSV file to read from and SQLite database
r_filenameCSV = '../../Data/Chapter1/realEstate_trans.csv'
rw_filenameSQLite = '../../Data/Chapter1/realEstate_trans.db'

# create the connection to the database
engine = sa.create_engine(
    'sqlite:///{0}'.format(rw_filenameSQLite)
)

# read the data
csv_read = pd.read_csv(r_filenameCSV)

# transform sale_date to a datetime object
csv_read['sale_date'] = pd.to_datetime(csv_read['sale_date'])

# store the data in the database
csv_read.to_sql('real_estate', engine, if_exists='replace')

# print the top 10 rows from the database
query = 'SELECT * FROM real_estate LIMIT 10'
top10 = pd.read_sql_query(query, engine)
print(top10)