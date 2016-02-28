import pymongo
import pandas as pd
import numpy as np

# define a specific count of observations to get back
strata_cnt = 200

# name of the file to output the sample
w_filenameSample = \
    '../../Data/Chapter02/realEstate_sample2.csv'

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
ttl_cnt = sales['beds'].count()
strata_expected_counts = sales['beds'].value_counts() / \
                         ttl_cnt * strata_cnt

# and select the sample
sample = pd.DataFrame()

for bed in beds:
    sample = sample.append(
        sales[sales.beds == bed] \
        .sample(n=np.round(strata_expected_counts[bed])),
        ignore_index=True
    )

# check if the counts selected match those expected
strata_sampled_counts = sample['beds'].value_counts()
print('Expected: ', strata_expected_counts)
print('Sampled: ', strata_sampled_counts)
print(
    'Total: expected -- {0}, sampled -- {1}' \
    .format(strata_cnt, strata_sampled_counts.sum())
)

# output to the file
with open(w_filenameSample,'w') as write_csv:
    write_csv.write(sample.to_csv(sep=',', index=False))