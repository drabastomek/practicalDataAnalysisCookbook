import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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
ax = sns.distplot(
    csv_read['price'], 
    bins=10, 
    kde=True    # show estimated kernel function
)

# set the title for the plot
ax.set_title('Price histogram with estimated kernel function')

# and save to a file
plt.savefig('../../Data/Chapter2/Figures/price_histogram.pdf')

# finally, show the plot
plt.show()