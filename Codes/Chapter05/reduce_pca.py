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

    # return the object
    return pca

# the file name of the dataset
r_filename = '../../Data/Chapter05/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# split into independent and dependent features
x = csv_read[csv_read.columns[:-1]]
y = csv_read[csv_read.columns[-1]]

# reduce the dimensionality
z = reduce_PCA(x)

# plot and save the chart
# to vary the colors and markers for the points
color_marker = [('r','o'),('g','.')]

file_save_params = {
    'filename': '../../Data/Chapter05/charts/pca_3d.png', 
    'dpi': 300
}

hlp.plot_components(z.transform(x, k=3), y, 
    color_marker, **file_save_params)