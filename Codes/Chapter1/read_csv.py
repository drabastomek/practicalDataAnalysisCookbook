import pandas as pd 

# names of files to read from
r_filenameCSV = '../../Data/Chapter1/realEstate_trans.csv'
r_filenameTSV = '../../Data/Chapter1/realEstate_trans.tsv'

# names of files to write to
w_filenameCSV = '../../Data/Chapter1/realEstate_trans.csv'
w_filenameTSV = '../../Data/Chapter1/realEstate_trans.tsv'

# read the data
csv_read = pd.read_csv(r_filenameCSV)
tsv_read = pd.read_csv(r_filenameTSV, sep='\t')

# print the first 10 records
print(csv_read.head(10))
print(tsv_read.head(10))

# write to files
with open(w_filenameCSV,'w') as write_csv:
    write_csv.write(tsv_read.to_csv(sep=',', index=False))

with open(w_filenameTSV,'w') as write_tsv:
    write_tsv.write(csv_read.to_csv(sep='\t', index=False))