import pymongo
import pandas as pd
import numpy as np

# define fraction of the data to sample
strata_frac = 0.2

# name of the file to output the sample
w_filenameSample = '../../Data/Chapter2/realEstate_sample.csv'

# limiting sales transactions to those of 2, 3, and 4 bedroom
# properties
beds = [2,3,4]

# connect to the MongoDB database
client = pymongo.MongoClient()
db = client['packt']
real_estate = db['real_estate']

# get all the documents, limit to specific fields
# and the number of beds
sales = pd.DataFrame.from_dict(
    list(
        real_estate.find(
            {
                'beds': {'$in': beds}
            }, {
                '_id': 0,
                'zip': 1, 
                'city': 1, 
                'price': 1,
                'beds': 1,
                'sq__ft': 1
            }
        )
    )
)

# calculate the expected counts
strata_expected_counts = sales['beds'].value_counts() * \
                         strata_frac

# and select the sample
sample = pd.DataFrame()

for bed in beds:
    sample = sample.append(
        sales[sales.beds == bed].sample(frac=strata_frac),
        ignore_index=True
    )

# check if the counts selected match those expected
print(strata_expected_counts)
print(sample['beds'].value_counts())

# output to the file
with open(w_filenameSample,'w') as write_csv:
    write_csv.write(sample.to_csv(sep=',', index=False))