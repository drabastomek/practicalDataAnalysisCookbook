import matplotlib.pyplot as plt
import pandas as pd

# name of the file to read from
r_filenameCSV = '../../Data/Chapter2/' + \
    'realEstate_trans_full.csv'

# name of the output file
w_filenameCSV = '../../Data/Chapter2/' + \
    'realEstate_corellations.csv'

# read the data and select only sales of flats 
# with up to 4 beds
csv_read = pd.read_csv(r_filenameCSV)
csv_read = csv_read.query('beds < 5')

# generate the histograms
hist_price = csv_read.hist(column='price', figsize=(9,7))
hist_pricebyBeds = csv_read.hist(
    column='price', 
    by='beds', 
    xlabelsize=7, 
    ylabelsize=7, 
    sharex=True, 
    figsize=(9,7)
)

# show the figures
plt.show()