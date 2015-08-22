import pandas as pd

def normalize(col):
    '''
        Normalize column
    '''
    return (col - col.min()) / (col.max() - col.min())

def standardize(col):
    '''
        Standardize column
    '''
    return (col - col.mean()) / col.std()

# name of the file to read from
r_filenameCSV = '../../Data/Chapter1/' + \
    'realEstate_trans_price_imputed.csv'

# name of the output file
w_filenameCSV = '../../Data/Chapter1/' + \
    'realEstate_trans_standardized.csv'

# list of columns to normalize and standardize
cols = ['price_mean','sq__ft']

# read the data
csv_read = pd.read_csv(r_filenameCSV)

# impute mean in place of NaNs
for col in cols:
    csv_read['n_' + col] = normalize(csv_read[col])
    csv_read['s_' + col] = standardize(csv_read[col])

# check if all is well now
for col in cols:
    print('{0}_n: min -- {1:.2f}, max -- {2:.2f}\n' \
        .format(
            col,
            csv_read['n_' + col].min(),
            csv_read['n_' + col].max()
        )
    )

    print('{0}_s: mean -- {1:.2f}, std dev -- {2:.2f}' \
        .format(
            col, 
            csv_read['s_' + col].mean(),
            csv_read['s_' + col].std()
        )
    )

# and write to a file
with open(w_filenameCSV, 'w') as write_csv:
	write_csv.write(csv_read.to_csv(sep=',', index=False))