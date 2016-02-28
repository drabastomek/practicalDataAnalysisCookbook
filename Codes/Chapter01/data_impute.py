import pandas as pd 

# name of the file to read from
r_filenameCSV = '../../Data/Chapter01/' + \
    'realEstate_trans_less_dirty.csv'

# name of the output file
w_filenameCSV = '../../Data/Chapter01/' + \
    'realEstate_trans_price_imputed.csv'

# read the data
csv_read = pd.read_csv(r_filenameCSV)

# impute mean in place of NaNs
csv_read['price_mean'] = csv_read['price'] \
    .fillna(
        csv_read.groupby('zip')['price'].transform('mean')
    )

# impute median in place of NaNs
csv_read['price_median'] = csv_read['price'] \
    .fillna(
        csv_read.groupby('zip')['price'].transform('median')
    )

# and write to a file
with open(w_filenameCSV, 'w') as write_csv:
	write_csv.write(csv_read.to_csv(sep=',', index=False))