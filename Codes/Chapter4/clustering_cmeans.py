# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import skfuzzy.cluster as cl
import numpy as np

@hlp.timeit
def findClusters_cmeans(data):
    '''
        Cluster data using fuzzy c-means clustering 
        algorithm
    '''
    # create the classifier object
    return cl.cmeans(
        data,
        c = 5,          # number of clusters
        m = 2,          # exponentiation factor
        
        # stopping criteria
        error = 0.01,
        maxiter = 300
    )

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
centroids, u, u0, d, jm, p, fpc = findClusters_cmeans(
    selected.transpose()
)

print(u[0:10])

# assess the clusters effectiveness
labels = [
    np.argmax(elem) for elem in u.transpose()
]


hlp.printClustersSummary(selected, labels, centroids)