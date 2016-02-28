# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import sklearn.cluster as cl
import sklearn.metrics as mt

@hlp.timeit
def findClusters_kmeans(data):
    '''
        Cluster data using k-means
    '''
    # create the classifier object
    kmeans = cl.KMeans(
        n_clusters=4,
        n_jobs=-1,
        verbose=0,
        n_init=30
    )

    # fit the data
    return kmeans.fit(data)

# the file name of the dataset
r_filename = '../../Data/Chapter04/bank_contacts.csv'

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
cluster = findClusters_kmeans(selected)

# assess the clusters effectiveness
labels = cluster.labels_
centroids = cluster.cluster_centers_

hlp.printClustersSummary(selected, labels, centroids)