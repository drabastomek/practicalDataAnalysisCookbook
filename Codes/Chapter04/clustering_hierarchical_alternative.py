# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import mlpy as ml
import numpy as np

@hlp.timeit
def findClusters_ward(data):
    '''
        Cluster data using Ward's hierarchical clustering
    '''
    # create the classifier object
    ward = ml.MFastHCluster(
        method='ward'
    )

    # fit the data
    ward.linkage(data)

    return ward

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
cluster = findClusters_ward(selected)

# assess the clusters effectiveness
labels = cluster.cut(20)
centroids = hlp.getCentroids(selected, labels)

hlp.printClustersSummary(selected, labels, centroids)