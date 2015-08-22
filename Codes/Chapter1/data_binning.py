import numpy as np
import pandas as pd

# name of the file to read from
r_filenameCSV = '../../Data/Chapter1/' + \
    'realEstate_trans_standardized.csv'

# name of the output file
w_filenameCSV = '../../Data/Chapter1/' + \
    'realEstate_trans_binned.csv'

# read the data
csv_read = pd.read_csv(r_filenameCSV)

# create bins for the price that are based on the 
# linearly spaced range of the price values
bins = np.linspace(
    csv_read['price_mean'].min(), 
    csv_read['price_mean'].max(), 
    6
)

# and apply the bins to the data
csv_read['b_price'] = np.digitize(
    csv_read['price_mean'], 
    bins
)

# print out the counts for the bins
counts_b = csv_read['b_price'].value_counts()
print(counts_b.sort_index())

# create bins based on deciles
decile = csv_read['price_mean'].quantile(np.linspace(0,1,11))

# and apply the decile bins to the data
csv_read['p_price'] = np.digitize(
    csv_read['price_mean'], 
    decile
)

# print out the counts for the percentile bins
counts_p = csv_read['p_price'].value_counts()
print(counts_p.sort_index())

# and write to a file
with open(w_filenameCSV, 'w') as write_csv:
	write_csv.write(csv_read.to_csv(sep=',', index=False))