# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np
import mlpy as ml

@hlp.timeit
def regression_linear(x,y):
    '''
        Estimate a linear regression
    '''
    # create the model object
    ols = ml.OLS()

    # estimate the model
    ols.learn(x, y)

    # and return the fit model
    return ols

def get_score(y, predicted):
    '''
        Method to calculate R^2
    '''
    # calculate the mean of actuals
    mean_y = y.mean()

    # calculate the total sum of squares and residual
    # sum of squares
    sum_of_square_total = np.sum((y - mean_y)**2)
    sum_of_square_resid = np.sum((y - predicted)**2)

    return 1 - sum_of_square_resid / sum_of_square_total

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
x = np.array(csv_read[independent_reduced[0]]).reshape(-1,1)
y = csv_read[dependent]

# estimate the model using all variables (without PC)
regressor = regression_linear(x,y)

# predict the output
predicted = regressor.pred(x)

# and calculate the R^2
score = get_score(y, predicted)
print(score)