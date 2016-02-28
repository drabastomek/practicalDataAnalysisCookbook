# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
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

# get the sample
x, y = hlp.produce_XOR(sampleSize=5000)

# reduce the dimensionality
kwd_params = [{ 'kernel': 'linear',
        'n_components': 2,'max_iter': 3,
        'tol': 1.0, 'eigen_solver': 'arpack'
    }, { 'kernel': 'poly',
        'degree': 2,'n_components': 2,'max_iter': 3,
        'tol': 1.0, 'eigen_solver': 'arpack'
    }, { 'kernel': 'sigmoid',
        'n_components': 2,'max_iter': 3,
        'tol': 1.0, 'eigen_solver': 'arpack'
    }, { 'kernel': 'cosine',
        'degree': 2,'n_components': 2,'max_iter': 3,
        'tol': 1.0, 'eigen_solver': 'arpack'}
]

# “linear” | “poly”| “sigmoid” | “cosine” 

color_marker = [('r','^'),('g','o')]

for params in kwd_params:
    z = reduce_KernelPCA(x, **params)

    # plot and save the chart
    # vary the colors and markers for the points
    file_save_params = {
        'filename': 
            '../../Data/Chapter05/charts/kernel_pca_3d_{0}.png'\
            .format(params['kernel']), 
        'dpi': 300
    }

    hlp.plot_components_2d(z.transform(x), y, color_marker, 
        **file_save_params)