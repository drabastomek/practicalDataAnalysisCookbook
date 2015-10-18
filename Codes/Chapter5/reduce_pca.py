# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np
import mlpy as ml

@hlp.timeit
def reduce_PCA(x):
    '''
        Reduce the dimensions using Principal Component
        Analysis 
    '''
    # create the PCA object
    pca = ml.PCA(whiten=True)

    # learn the principal components from all the features
    pca.learn(x)

    # return only 3 principal components
    return pca.transform(x, k=3)

# the file name of the dataset
r_filename = '../../Data/Chapter5/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# split into independent and dependent features
x = csv_read[csv_read.columns[:-1]]
y = csv_read[csv_read.columns[-1]]

# reduce the dimensionality
z = reduce_PCA(x)

# plot and save the chart
file_save_params = {
    'filename': '../../Data/Chapter5/charts/pca_3d.png', 
    'dpi': 300
}

hlp.plot_components(z, y, **file_save_params)