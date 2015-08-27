import pandas as pd 

# name of the file to read from
r_filenameCSV = '../../Data/Chapter2/' + \
    'realEstate_trans_full.csv'

# name of the output file
w_filenameCSV = '../../Data/Chapter2/' + \
    'realEstate_descriptives.csv'

# read the data
csv_read = pd.read_csv(r_filenameCSV)

# calculate the descriptives: count, mean, std,
# min, 25%, 50%, 75%, max
# for a subset of columns
csv_desc = csv_read[
    [   
        'beds','baths','sq__ft','price','s_price',
        'n_price','s_sq__ft','n_sq__ft','b_price',
        'p_price','d_Condo','d_Multi-Family',
        'd_Residential','d_Unkown'
    ]
].describe().transpose()

# and add skewness, mode and kurtosis
csv_desc['skew'] = csv_read.skew(numeric_only=True)
csv_desc['mode'] = \
    csv_read.mode(numeric_only=True).transpose()
csv_desc['kurtosis'] = csv_read.kurt(numeric_only=True)

# output the descriptives to a file
with open(w_filenameCSV,'w') as write_csv:
    write_csv.write(csv_desc.to_csv(sep=','))