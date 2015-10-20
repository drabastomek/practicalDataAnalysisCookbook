# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np
import sklearn.decomposition as cd

@hlp.timeit
def reduce_CCA(x, y):
    '''
        Reduce the dimensions using Canonical Correlation
        Analysis
    '''
    # create the CCA object
    cca = cd.RandomizedPCA(n_components=3, whiten=True,
        copy=True)

    # learn the principal components from all the features
    return cca.fit(x, y)

# the file name of the dataset
r_filename = '../../Data/Chapter5/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# split into independent and dependent features
x = csv_read[csv_read.columns[:-1]]
y = csv_read[csv_read.columns[-1]]

# reduce the dimensionality
z = reduce_CCA(x, y)

# plot and save the chart
# to vary the colors and markers for the points
color_marker = [('r','o'),('g','.')]

file_save_params = {
    'filename': '../../Data/Chapter5/charts/randomized_pca_3d.png', 
    'dpi': 300
}

hlp.plot_components(z.transform(x), y, color_marker, 
    **file_save_params)