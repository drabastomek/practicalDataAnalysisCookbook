import scipy.stats as st
import numpy as np

# name of the file to read from
r_filenameCSV = '../../Data/Chapter02/' + \
    'realEstate_trans_full.csv'

# read the data
csv_read = np.genfromtxt(
    r_filenameCSV, 
    delimiter=',',
    names=True,
    # only numeric columns
    usecols=[4,5,6,8,11,12,13,14,15,16,17,18,19,20]
)

# calculate the descriptives
desc = st.describe([list(item) for item in csv_read])

# and print out to the screen
print(desc)