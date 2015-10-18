# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np

import mlpy as ml

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

@hlp.timeit
def reduce_PCA(x):
    pca = ml.PCA(whiten=True)
    pca.learn(x)

    return pca.transform(x, k=3)

# the file name of the dataset
r_filename = '../../Data/Chapter5/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

x = csv_read[csv_read.columns[:-1]]
y = csv_read[csv_read.columns[-1]]
y_np = np.array(y)

z = reduce_PCA(x)

# print(y.unique())

# plt.set_cmap(plt.cm.Paired)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

color_marker = [('r','o'),('g','^'),('b','.')]

for i in range(0, len(y.unique())):
    ax.scatter(
        z[y_np == i, 0], 
        z[y_np == i, 1], 
        z[y_np == i, 2], 
        c=color_marker[i][0], 
        marker=color_marker[i][1])

    # print(i,z[y[y == i], 0], 
    #     z[y[y == i], 1], 
    #     z[y[y == i], 2], 
    #     color_marker[i][0], 
    #     color_marker[i][1])


# print(z[0:3], z[y_np == 0, 0])

# plt.show()
plt.savefig('../../Data/Chapter5/charts/pca_3d.png', dpi=300)

# print(csv_read.columns[:-1])