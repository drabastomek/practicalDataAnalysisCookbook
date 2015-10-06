# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import sklearn.cluster as cl
import numpy as np

@hlp.timeit
def findClusters_DBSCAN(data):
    '''
        Cluster data using DBSCAN algorithm
    '''
    # create the classifier object
    dbscan = cl.DBSCAN(eps=1.2, min_samples=200)

    # fit the data
    return dbscan.fit(data)

def getCentroids(data, labels):
    '''
        Method to get the centroids of clusters in DBSCAN
    '''
    # create a copy of the data
    data = data.copy()

    # apply labels
    data['predicted'] = labels

    # and return the centroids
    return np.array(data.groupby('predicted').agg('mean'))

# the file name of the dataset
r_filename = '../../Data/Chapter3/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# select variables
selected = csv_read[['n_duration','n_nr_employed',
        'prev_ctc_outcome_success','n_euribor3m',
        'n_cons_conf_idx','n_age','month_oct',
        'n_cons_price_idx','edu_university_degree','n_pdays',
        'dow_mon','job_student','job_technician',
        'job_housemaid','edu_basic_6y']]

# cluster the data
cluster = findClusters_DBSCAN(selected)

# assess the clusters effectiveness
labels = cluster.labels_ + 1
centroids = getCentroids(selected, labels)

print('Number of clusters: {0}' \
    .format(len(np.unique(labels)))
)

print(hlp.pseudo_F(selected,labels, centroids))
print(hlp.davis_bouldin(selected,labels, centroids))