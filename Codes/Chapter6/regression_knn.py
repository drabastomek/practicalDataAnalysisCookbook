# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np
import sklearn.neighbors as nb

@hlp.timeit
def regression_kNN(x,y):
    '''
        Build the kNN classifier
    '''
    # create the classifier object
    knn = nb.KNeighborsRegressor(n_neighbors=20, 
        algorithm="kd_tree", n_jobs=-1)

    # fit the data
    knn.fit(x,y)

    #return the classifier
    return knn

# the file name of the dataset
r_filename = '../../Data/Chapter6/power_plant_dataset_pc.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# select the names of columns
dependent = csv_read.columns[-1]
independent_reduced = [
    col 
    for col 
    in csv_read.columns 
    if col.startswith('p')
]

independent = [
    col 
    for col 
    in csv_read.columns 
    if      col not in independent_reduced
        and col not in dependent
]

# split into independent and dependent features
x     = csv_read[independent]
x_red = csv_read[independent_reduced]
y     = csv_read[dependent]

# estimate the model using all variables (without PC)
regressor = regression_kNN(x,y)

print(regressor.score(x,y))

# estimate the model using Principal Components only
regressor_red = regression_kNN(x_red,y)

print(regressor_red.score(x_red,y))
