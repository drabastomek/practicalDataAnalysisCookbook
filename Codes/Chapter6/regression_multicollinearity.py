# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np
import sklearn.decomposition as dc

def reduce_PCA(x, n):
    '''
        Reduce the dimensions using Principal Component
        Analysis 
    '''
    # create the PCA object
    pca = dc.PCA(n_components=n, whiten=True)

    # learn the principal components from all the features
    return pca.fit(x)

# the file name of the dataset
r_filename = '../../Data/Chapter6/power_plant_dataset.csv'

# read the data
csv_read = pd.read_csv(r_filename)

x = csv_read[csv_read.columns[:-1]].copy()
y = csv_read[csv_read.columns[-1]]

# produce correlation matrix for the independent variables
corr = x.corr()

# and check the eigenvectors and eigenvalues of the matrix
w, v = np.linalg.eig(corr)
print('Eigenvalues: ', w)

# values that are close to 0 indicate multicollinearity
s = np.nonzero(w < 0.01)
# inspect which variables are collinear
print('Indices of eigenvalues close to 0:', s[0])

all_columns = []
for i in s[0]:
    print('\nIndex: {0}. '.format(i))

    t = np.nonzero(abs(v[:,i]) > 0.33)
    all_columns += list(t[0]) + [i]
    print('Collinear: ', t[0])

for i in np.unique(all_columns):
    print('Variable {0}: {1}'.format(i, x.columns[i]))

# and reduce the data keeping only 3 principal components
n_components = 5
z = reduce_PCA(x, n=n_components)
pc = z.transform(x)

# how much variance each component explains?
print('\nVariance explained by each principal component: ', 
    z.explained_variance_ratio_)

# and total variance accounted for
print('Total variance explained: ', 
    np.sum(z.explained_variance_ratio_))

# append the reduced dimensions to the dataset
for i in range(0, n_components):
    col_name = 'p_{0}'.format(i)
    x[col_name] = pd.Series(pc[:, i])
    
x[csv_read.columns[-1]] = y
csv_read = x

# output to file
w_filename = '../../Data/Chapter6/power_plant_dataset_pc.csv'
with open(w_filename, 'w') as output:
    output.write(csv_read.to_csv(index=False))
