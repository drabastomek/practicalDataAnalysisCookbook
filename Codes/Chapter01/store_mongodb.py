import pandas as pd
import pymongo

# name of the CSV file to read from and SQLite database
r_filenameCSV = '../../Data/Chapter01/realEstate_trans.csv'

# read the data
csv_read = pd.read_csv(r_filenameCSV)

# transform sale_date to a datetime object
csv_read['sale_date'] = pd.to_datetime(csv_read['sale_date'])

# connect to the MongoDB database
client = pymongo.MongoClient()

# and select packt database
db = client['packt']

# then connect to real_estate collection
real_estate = db['real_estate']

# if there are any documents stored already -- remove them
if real_estate.count() > 0:
    real_estate.remove()

# and then insert the data
real_estate.insert(csv_read.to_dict(orient='records'))

# print out the top 10 documents 
# sold in ZIP codes 95841 and 95842
sales = real_estate.find({'zip': {'$in': [95841, 95842]}})
for sale in sales.sort('_id').limit(10):
    print(sale)