import csv 

# names of files to read from
r_filenameCSV = '../../Data/Chapter1/realEstate_trans.csv'
r_filenameTSV = '../../Data/Chapter1/realEstate_trans.tsv'

# data structures to hold the data
csv_labels = []
tsv_labels = []
csv_data = []
tsv_data = []

# read the data
with open(r_filenameCSV, 'r') as csv_in:
    csv_reader = csv.reader(csv_in)

    # read the first line that holds column labels
    csv_labels = csv_reader.__next__()
    
    # iterate through all the records
    for record in csv_reader:
        csv_data.append(record)

with open(r_filenameTSV, 'r') as tsv_in:
    tsv_reader = csv.reader(tsv_in, delimiter='\t')

    tsv_labels = tsv_reader.__next__()
    
    for record in tsv_reader:
        tsv_data.append(record)

# print the labels
print(csv_labels, '\n')
print(tsv_labels, '\n')

# print the first 10 records
print(csv_data[0:10],'\n')
print(tsv_data[0:10],'\n')

