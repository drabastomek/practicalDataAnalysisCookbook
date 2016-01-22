# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import numpy as np
import sklearn.decomposition as dc

def reduce_PCA(x):
    '''
        Reduce the dimensions using Principal Component
        Analysis 
    '''
    # create the PCA object
    pca = dc.PCA(n_components=2, whiten=True)

    # learn the principal components from all the features
    return pca.fit(x)

def reduce_randomizedPCA(x):
    '''
        Reduce the dimensions using Randomized PCA algorithm
    '''
    # create the CCA object
    randomPCA = dc.RandomizedPCA(n_components=2, whiten=True,
        copy=False)

    # learn the principal components from all the features
    return randomPCA.fit(x)

def saveSurfacePlot(X_in,Y_in,Z,**f_params):
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import matplotlib as mt

    # adjust the font
    font = {'size': 8}
    mt.rc('font', **font)

    # create a mesh
    X, Y = np.meshgrid(X_in, Y_in)

    # create figure and add axes
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # plot the surface
    surf = ax.plot_surface(X, Y, Z, 
        rstride=1, cstride=1, 
        cmap=mt.cm.seismic,
        linewidth=0, antialiased=True)

    # set the limits on the z-axis
    ax.set_zlim(0, 7)

    # add labels to axes
    ax.set_xlabel('Sample size')
    ax.set_ylabel('Feature space')
    ax.set_zlabel('Time to estimate (s)')

    # rotate the chart
    ax.view_init(30, 130)

    # and save the figure
    fig.savefig(**f_params)

# prepare the sample
sampleSizes = np.arange(1000, 50000, 3000)
featureSpace = np.arange(100, 1000, 100)

# object to hold the results
Z = {'randomPCA': [], 'PCA': []}

for features in featureSpace:
    inner_z_randomPCA = []
    inner_z_PCA = []

    for sampleSize in sampleSizes:
        # get the sample
        x, y = hlp.produce_sample(
            sampleSize=sampleSize, features=features)

        print(
            'Processing: sample size {0} and {1} features'\
            .format(sampleSize, features))

        # reduce the dimensionality
        z_r, time_r     = hlp.timeExecution(
            reduce_randomizedPCA, x)
        z_pca, time_pca = hlp.timeExecution(
            reduce_PCA, x)

        inner_z_randomPCA.append(time_r)
        inner_z_PCA.append(time_pca)

    Z['randomPCA'].append(inner_z_randomPCA)
    Z['PCA'].append(inner_z_PCA)

# filename params for the standard PCA
f_params = {
    'filename':
        '../../Data/Chapter5/charts/time_pca_surf.png',
    'dpi': 300
}

# prepare and save the plot
saveSurfacePlot(sampleSizes, featureSpace, 
    Z['PCA'], **f_params)

# filename params for the randomized PCA
f_params = {
    'filename':
        '../../Data/Chapter5/charts/time_r_pca_surf.png',
    'dpi': 300
}

# prepare and save the plot
saveSurfacePlot(sampleSizes, featureSpace, 
    Z['randomPCA'], **f_params)
