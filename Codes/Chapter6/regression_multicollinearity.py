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

x = csv_read[csv_read.columns[:-1]]
y = csv_read[csv_read.columns[-1]]

# produce correlation matrix for the independent variables
corr = x.corr()

# and check the eigenvectors and eigenvalues of the matrix
w, v = np.linalg.eig(corr)
print(w)

# values that are close to 0 indicate multicollinearity
s = np.nonzero(w < 0.01)
print(s, v[:,s[0]])

# inspect which variables are not collinear
t = np.nonzero(abs(v[:,s[0]]) > 0.01)
print(t[0])

# and reduce the data keeping only 3 principal components
z = reduce_PCA(x, n=3)
pc = z.transform(x)
print(pc)

# how much variance each component explains?
print(z.explained_variance_ratio_)

# and total variance accounted for
print(np.sum(z.explained_variance_ratio_))

# append the reduced dimensions to the dataset
for i in range(0, 3):
    x['p_{0}'.format(i)] = pc[:, i]
    
x[csv_read.columns[-1]] = y
csv_read = x

# output to file
w_filename = '../../Data/Chapter6/power_plant_dataset_pc.csv'
with open(w_filename, 'w') as output:
    output.write(csv_read.to_csv(index=False))
