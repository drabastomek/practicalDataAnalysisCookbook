# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import sklearn.cluster as cl
import sklearn.datasets as dt
import sklearn.manifold as mn
import sklearn.metrics as mt

@hlp.timeit
def findClusters_kmeans(data):
    '''
        Cluster data using k-means
    '''
    # create the classifier object
    kmeans = cl.KMeans(
        n_clusters=10,
        n_jobs=-1,
        verbose=2,
        n_init=100
    )

    # fit the data
    return kmeans.fit(data)

# # the file name of the dataset
# r_filename = '../../Data/Chapter3/bank_contacts.csv'

# # read the data
# csv_read = pd.read_csv(r_filename)

# print(csv_read.head(10))

digits = dt.load_digits(n_class=10)
X = digits.data
y = digits.target

X_red = mn.SpectralEmbedding(n_components=2).fit_transform(X)

cluster = findClusters_kmeans(X_red)

pred = cluster.predict(X_red)

print(mt.homogeneity_score(pred, y))
print(mt.completeness_score(pred, y))

# print(cluster.predict(csv_read))