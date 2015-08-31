import numpy as np
import pandas as pd
import sqlalchemy as sa

# specify what proportion of data to hold out for testing
test_size = 0.33

# names of the files to output the samples
w_filenameTrain = '../../Data/Chapter2/realEstate_train.csv'
w_filenameTest  = '../../Data/Chapter2/realEstate_test.csv'

# database credentials
usr  = 'drabast'
pswd = 'pAck7!B0ok'

# create the connection to the database
engine = sa.create_engine(
    'postgresql://{0}:{1}@localhost:5432/{0}' \
    .format(usr, pswd)
)

# read prices from the database
query = 'SELECT * FROM real_estate'
data = pd.read_sql_query(query, engine)

# create a variable to flag the training sample
data['train']  = np.random.rand(len(data)) < (1 - test_size) 

# split the data into training and testing
train = data[data.train]
test  = data[~data.train]

# output the samples to files
with open(w_filenameTrain,'w') as write_csv:
    write_csv.write(train.to_csv(sep=',', index=False))

with open(w_filenameTest,'w') as write_csv:
    write_csv.write(test.to_csv(sep=',', index=False))