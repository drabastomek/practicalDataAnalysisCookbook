# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import sklearn.neighbors as nb
import sklearn.cross_validation as cv

@hlp.timeit
def regression_kNN(x,y):
    '''
        Build the kNN classifier
    '''
    # create the classifier object
    knn = nb.KNeighborsRegressor(n_neighbors=80, 
        algorithm='kd_tree', n_jobs=-1)

    # fit the data
    knn.fit(x,y)

    #return the classifier
    return knn

# the file name of the dataset
r_filename = '../../Data/Chapter06/power_plant_dataset_pc.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# select the names of columns
dependent = csv_read.columns[-1]
independent_principal = [
    col 
    for col 
    in csv_read.columns 
    if col.startswith('p')
]

independent_significant = [
    'total_fuel_cons', 'total_fuel_cons_mmbtu'
]

# split into independent_significant and dependent features
x_sig = csv_read[independent_significant]
x_principal = csv_read[independent_principal]
y = csv_read[dependent]

# estimate the model using all variables (without PC)
regressor = regression_kNN(x_sig,y)

print('R2: ', regressor.score(x_sig,y))

# test the sensitivity of R2
scores = cv.cross_val_score(regressor, x_sig, y, cv=100)
print('Expected R2: {0:.2f} (+/- {1:.2f})'\
    .format(scores.mean(), scores.std()**2))

# estimate the model using Principal Components only
regressor_principal = regression_kNN(x_principal,y)

print('R2: ', regressor_principal.score(x_principal,y))

# test the sensitivity of R2
scores = cv.cross_val_score(regressor_principal, 
    x_principal, y, cv=100)
print('Expected R2: {0:.2f} (+/- {1:.2f})'\
    .format(scores.mean(), scores.std()**2))
