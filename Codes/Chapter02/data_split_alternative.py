import numpy as np
import pandas as pd
import sqlalchemy as sa
import sklearn.cross_validation as sk

# names of the files to output the samples
w_filenameTrain = '../../Data/Chapter02/realEstate_train2.csv'
w_filenameTest  = '../../Data/Chapter02/realEstate_test2.csv'

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

# select the independent and dependent variables
x = data[['zip', 'beds', 'sq__ft']]
y = data['price']

# and perform the split
x_train, x_test, y_train, y_test = sk.train_test_split(
    x, y, test_size=0.33, random_state=42)

# then form DataFrames for ease of manipulating
train = pd.DataFrame(
    np.append(
        x_train, \
        y_train.reshape((x_train.shape[0], 1)), \
        1), 
    columns=['zip', 'beds', 'sq__ft', 'price']
)

test = pd.DataFrame(
    np.append(
        x_test, 
        y_test.reshape((x_test.shape[0], 1)), \
        1), 
    columns=['zip', 'beds', 'sq__ft', 'price']
)

# output the samples to files
with open(w_filenameTrain,'w') as write_csv:
    write_csv.write(train.to_csv(sep=',', index=False))

with open(w_filenameTest,'w') as write_csv:
    write_csv.write(test.to_csv(sep=',', index=False))