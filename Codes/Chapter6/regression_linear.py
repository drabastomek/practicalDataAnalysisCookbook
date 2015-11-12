# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np
import sklearn.linear_model as lm

@hlp.timeit
def regression_linear(x,y):
    '''
        Estimate a linear regression
    '''
    # create the regressor object
    linear = lm.LinearRegression(fit_intercept=True,
        normalize=True, copy_X=True, n_jobs=-1)

    # estimate the model
    linear.fit(x,y)

    # return the object
    return linear

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
z = regression_linear(x,y)

print(z.score(x,y))
print(z.coef_)
print(z.intercept_)

# estimate the model using Principal Components only
z_red = regression_linear(x_red,y)

print(z_red.score(x_red,y))
print(z_red.coef_)
print(z_red.intercept_)
