# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np
import sklearn.ensemble as en
import sklearn.cross_validation as cv

@hlp.timeit
def regression_rf(x,y):
    '''
        Estimate a random forest regressor
    '''
    # create the regressor object
    random_forest = en.RandomForestRegressor(
        min_samples_split=80, random_state=666, 
        max_depth=5, n_estimators=10)

    # estimate the model
    random_forest.fit(x,y)

    # return the object
    return random_forest

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
x = csv_read[independent]
y = csv_read[dependent]

# estimate the model using all variables (without PC)
regressor = regression_rf(x,y)

# print out the results
print('R: ', regressor.score(x,y))

# test the sensitivity of R2
scores = cv.cross_val_score(regressor, x, y, cv=100)
print('Expected R2: {0:.2f} (+/- {1:.2f})'\
    .format(scores.mean(), scores.std()**2))

# print features importance
for counter, (nm, label) \
    in enumerate(
        zip(x.columns, regressor.feature_importances_)
    ):
    print("{0}. {1}: {2}".format(counter, nm,label))

# estimate the model using only the most important feature
features = np.nonzero(regressor.feature_importances_ > 0.001)
x_red = csv_read[features[0]]
regressor_red = regression_rf(x_red,y)

# print out the results
print('R: ', regressor_red.score(x_red,y))

# test the sensitivity of R2
scores = cv.cross_val_score(regressor_red, x_red, y, cv=100)
print('Expected R2: {0:.2f} (+/- {1:.2f})'\
    .format(scores.mean(), scores.std()**2))

# print features importance
for counter, (nm, label) \
    in enumerate(
        zip(x_red.columns, regressor_red.feature_importances_)
    ):
    print("{0}. {1}: {2}".format(counter, nm,label))