# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np
import mlpy as ml

@hlp.timeit
def reduce_KernelPCA(x, **kwd_params):
    '''
        Reduce the dimensions using Principal Component
        Analysis with different kernels
    '''
    # create the PCA object
    pca = ml.KPCA()

    # learn the principal components from all the features
    pca.learn(x)

    return pca

# the file name of the dataset
r_filename = '../../Data/Chapter5/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# split into independent and dependent features
x = csv_read[csv_read.columns[:-1]]
y = csv_read[csv_read.columns[-1]]

# prepare the kernel
kernel_gauss = ml.kernel_gaussian(x, x, sigma=1)

# reduce the dimensionality
z = reduce_KernelPCA(kernel_gauss)

# plot and save the chart
# vary the colors and markers for the points
color_marker = [('r','^'),('g','o')]

file_save_params = {
    'filename': \
        '../../Data/Chapter5/charts/kernel_pca_3d_alt.png', 
    'dpi': 300
}

hlp.plot_components(z.transform(kernel_gauss, k = 3), 
    y, color_marker, **file_save_params)