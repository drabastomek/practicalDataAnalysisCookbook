# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import sklearn.cluster as cl
import numpy as np

@hlp.timeit
def findClusters_Birch(data):
    '''
        Cluster data using BIRCH algorithm
    '''
    # create the classifier object
    birch = cl.Birch(
        branching_factor=100,
        n_clusters=4,
        compute_labels=True,
        copy=True
    )

    # fit the data
    return birch.fit(data)

# the file name of the dataset
r_filename = '../../Data/Chapter4/bank_contacts.csv'

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
cluster = findClusters_Birch(selected)

# assess the clusters effectiveness
labels = cluster.labels_
centroids = hlp.getCentroids(selected, labels)

hlp.printClustersSummary(selected, labels, centroids)