# import numpy as np
import pandas as pd
import sqlalchemy as sa
# import sklearn.cross_validation as sk

# names of the files to output the samples
w_filenameD3js = '../../Data/Chapter2/realEstate_d3.csv'

# database credentials
usr  = 'drabast'
pswd = 'pAck7!B0ok'

# create the connection to the database
engine = sa.create_engine(
    'postgresql://{0}:{1}@localhost:5432/{0}' \
    .format(usr, pswd)
)

# read prices from the database
query = '''SELECT beds || \' beds\' AS beds, 
            sq__ft, 
            price / 1000 AS price 
        FROM real_estate 
        WHERE sq__ft > 0 
        AND beds BETWEEN 2 AND 4'''
data = pd.read_sql_query(query, engine)

# output the samples to files
with open(w_filenameD3js,'w') as write_csv:
    write_csv.write(data.to_csv(sep=',', index=False))