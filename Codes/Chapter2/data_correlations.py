import pandas as pd 

# name of the file to read from
r_filenameCSV = '../../Data/Chapter2/' + \
    'realEstate_trans_full.csv'

# name of the output file
w_filenameCSV = '../../Data/Chapter2/' + \
    'realEstate_corellations.csv'

# read the data and select only 4 variables
csv_read = pd.read_csv(r_filenameCSV)
csv_read = csv_read[['beds','baths','sq__ft','price']]

# calculate the correlations
coefficients = ['pearson', 'kendall', 'spearman']

csv_corr = {}

for coefficient in coefficients:
    csv_corr[coefficient] = csv_read \
        .corr(method=coefficient) \
        .transpose()

# output to a file
with open(w_filenameCSV,'w') as write_csv:
    for corr in csv_corr:
        write_csv.write(corr + '\n')
        write_csv.write(csv_corr[corr].to_csv(sep=','))
        write_csv.write('\n')