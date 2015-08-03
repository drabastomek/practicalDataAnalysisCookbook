import pandas as pd 

# name of the JSON file to read from
r_filenameJSON = '../../Data/Chapter1/realEstate_trans.json'

# read the data
json_read = pd.read_json(r_filenameJSON)

# print the first 10 records
print(json_read.head(10))
