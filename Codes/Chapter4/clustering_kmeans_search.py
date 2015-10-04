# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import sklearn.cluster as cl
import numpy as np

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

def findOptimalClusterNumber(
        data, 
        keep_going = 1, 
        max_iter = 30
    ):
    '''
        A method that iteratively searches for the 
        number of clusters that minimizes the Davis-Bouldin
        criterion
    '''
    measures = [666]        # first element
    n_clusters = 2          # starting point
    
    # counter for the number of iterations past the local 
    # minimum
    keep_going_cnt = 0
    minimum_found = False   # flag for the minimum found
    
    def checkMinimum(keep_going):
        '''
            A method to check if minimum found
        '''
        global keep_going_cnt # access global counter

        # if the new measure is greater than for one of the 
        # previous runs
        if measures[-1] > np.min(measures[:-1]):
            # increase the counter
            keep_going_cnt += 1

            # if the counter is bigger than allowed 
            if keep_going_cnt > keep_going:
                # the minimum is found
                return True
        # else, reset the counter and return False
        else:
            keep_going_cnt = 0

        return False

    # main loop 
    # loop until minimum found or maximum iterations reached
    while not minimum_found and n_clusters < (max_iter + 2):
        # cluster the data
        cluster = findClusters_kmeans(data, n_clusters)

        # assess the clusters effectiveness
        labels = cluster.labels_
        centroids = cluster.cluster_centers_

        # store the measures
        measures.append(
            hlp.davis_bouldin(data,labels, centroids)
        )

        # check if minimum found
        minimum_found = checkMinimum(keep_going)

        # increase the iteration
        n_clusters += 1

    # once found -- return the index of the minimum
    return measures.index(np.min(measures))

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

# find the optimal number of clusters; that is, the number of
# clusters that minimizes the Davis-Bouldin criterion
optimal_n_clusters = findOptimalClusterNumber(selected)

print('Optimal number of clusters: {0}' \
    .format(optimal_n_clusters))

# cluster the data
cluster = findClusters_kmeans(selected, optimal_n_clusters)

# assess the clusters effectiveness
labels = cluster.labels_
centroids = cluster.cluster_centers_

print(hlp.pseudo_F(selected,labels, centroids))
print(hlp.davis_bouldin(selected,labels, centroids))