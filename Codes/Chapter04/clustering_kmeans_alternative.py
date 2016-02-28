# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import scipy.cluster.vq as vq

@hlp.timeit
def findClusters_kmeans(data):
    '''
        Cluster data using k-means
    '''
    # whiten the observations
    data_w = vq.whiten(data)

    # create the classifier object
    kmeans, labels = vq.kmeans2(
        data_w,
        k=4,
        iter=30
    )

    # fit the data
    return kmeans, labels

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
centroids, labels = findClusters_kmeans(selected.as_matrix())

hlp.printClustersSummary(selected, labels, centroids)