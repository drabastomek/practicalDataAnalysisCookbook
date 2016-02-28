# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import scipy.cluster.hierarchy as cl
import numpy as np
import pylab as pl

@hlp.timeit
def findClusters_link(data):
    '''
        Cluster data using single linkage hierarchical 
        clustering
    '''
    # return the linkage object
    return cl.linkage(data, method='single')

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

# plot the clusters
fig  = pl.figure(figsize=(16,9))
ax   = fig.add_axes([0.1, 0.1, 0.8, 0.8])
dend = cl.dendrogram(cluster, truncate_mode='level', p=20)
ax.set_xticks([])
ax.set_yticks([])

# save the figure
fig.savefig(
    '../../Data/Chapter04/hierarchical_dendrogram.png',
    dpi=300
)