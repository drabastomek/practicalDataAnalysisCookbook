import pandas as pd
import sqlalchemy as sa

# name of the CSV file to read from
r_filenameCSV = '../../Data/Chapter1/realEstate_trans.csv'

# database credentials
usr  = 'drabast'
pswd = 'pAck7!B0ok'

# create the connection to the database
engine = sa.create_engine(
    'postgresql://{0}:{1}@localhost:5432/{0}' \
    .format(usr, pswd)
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