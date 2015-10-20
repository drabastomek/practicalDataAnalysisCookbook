# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np
import sklearn.decomposition as dc

@hlp.timeit
def reduce_KernelPCA(x, **kwd_params):
    '''
        Reduce the dimensions using Principal Component
        Analysis with different kernels
    '''
    # create the PCA object
    pca = dc.KernelPCA(**kwd_params)

    # learn the principal components from all the features
    return pca.fit(x)

# the file name of the dataset
r_filename = '../../Data/Chapter5/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# split into independent and dependent features
x = csv_read[csv_read.columns[:-1]]
y = csv_read[csv_read.columns[-1]]

# reduce the dimensionality
kwd_params = {
        'kernel': 'rbf',
        'gamma': 0.33,
        'n_components': 3,
        'max_iter': 1,
        'tol': 0.9,
        'eigen_solver': 'arpack'
    }

z = reduce_KernelPCA(x, **kwd_params)

# plot and save the chart
# vary the colors and markers for the points
color_marker = [('r','^'),('g','o')]

file_save_params = {
    'filename': '../../Data/Chapter5/charts/kernel_pca_3d.png', 
    'dpi': 300
}

hlp.plot_components(z.transform(x), y, color_marker, 
    **file_save_params)