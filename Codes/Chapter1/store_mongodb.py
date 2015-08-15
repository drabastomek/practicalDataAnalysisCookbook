import pandas as pd
import pymongo as pm

# name of the CSV file to read from and SQLite database
r_filenameCSV = '../../Data/Chapter1/realEstate_trans.csv'
rw_filenameSQLite = '../../Data/Chapter1/realEstate_trans.db'

# read the data
csv_read = pd.read_csv(r_filenameCSV)

# transform sale_date to a datetime object
csv_read['sale_date'] = pd.to_datetime(csv_read['sale_date'])

# connect to the MongoDB database
client = pm.MongoClient()

# and select packt database
db = client['packt']

# then connect to real_estate collection
collection = db['real_estate']

# if there are any documents stored already -- remove them
if collection.find().count() > 0:
    collection.remove()

# and then insert the newly read data
collection.insert(csv_read.to_dict(orient='records'))

# print out the top 10 documents
cursor = collection.find()
for record in cursor.sort('_id').limit(10):
    print(record)