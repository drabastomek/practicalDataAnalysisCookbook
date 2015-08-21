import pandas as pd

# name of the file to read from
r_filenameCSV = '../../Data/Chapter1/' + \
    'realEstate_trans_binned.csv'

# name of the output file
w_filenameCSV = '../../Data/Chapter1/' + \
    'realEstate_trans_full.csv'

# read the data
csv_read = pd.read_csv(r_filenameCSV)

# dummy code the column with the type of the property
csv_read = pd.get_dummies(
    csv_read, 
    prefix='d', 
    columns=['type']
)

# and write to a file
with open(w_filenameCSV, 'w') as write_csv:
	write_csv.write(csv_read.to_csv(sep=',', index=False))