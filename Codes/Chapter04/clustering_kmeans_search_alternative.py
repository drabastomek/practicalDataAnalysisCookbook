# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import sklearn.cluster as cl
# import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

@hlp.timeit
def findClusters_kmeans(data, no_of_clusters):
    '''
        Cluster data using k-means
    '''
    # create the classifier object
    kmeans = cl.KMeans(
        n_clusters=no_of_clusters,
        n_jobs=-1,
        verbose=0,
        n_init=30
    )

    # fit the data
    return kmeans.fit(data)

def plotInteractions(data, n_clusters):
    '''
        Plot the interactions between variables
    '''
    # cluster the data
    cluster = findClusters_kmeans(data, n_clusters)

    # append the labels to the dataset for ease of plotting
    data['clus'] = cluster.labels_

    # prepare the plot
    ax = sns.pairplot(selected, hue='clus')

    # and save the figure
    ax.savefig(
        '../../Data/Chapter04/k_means_{0}_clusters.png' \
        .format(n_clusters)
    )


# the file name of the dataset
r_filename = '../../Data/Chapter04/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# which columns we'll use
columns = ['n_duration','n_cons_price_idx','n_euribor3m']

# select variables
selected = csv_read[columns]

# plot the interactions
plotInteractions(selected, 14)