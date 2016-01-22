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
regressor = regression_linear(x,y)

# print model summary
print('\nR^2: {0}'.format(regressor.score(x,y)))
coeff = [(nm, coeff) 
    for nm, coeff 
    in zip(x.columns, regressor.coef_)]
intercept = regressor.intercept_
print('Coefficients: ', coeff)
print('Intercept', intercept)
print('Total number of variables: ', 
    len(coeff) + 1)

# estimate the model using Principal Components only
regressor_red = regression_linear(x_red,y)

# print model summary
print('\nR^2: {0}'.format(regressor_red.score(x_red,y)))
coeff = [(nm, coeff) 
    for nm, coeff 
    in zip(x_red.columns, regressor_red.coef_)]
intercept = regressor_red.intercept_
print('Coefficients: ', coeff)
print('Intercept', intercept)
print('Total number of variables: ', 
    len(coeff) + 1)

# removing the state variables and keeping only fuel and state
columns = [col for col in independent if 'state' not in col and col != 'total_fuel_cons']
x_no_state = x[columns]

# estimate the model
regressor_nm = regression_linear(x_no_state,y)

# print model summary
print('\nR^2: {0}'.format(regressor_nm.score(x_no_state,y)))
coeff = [(nm, coeff) 
    for nm, coeff 
    in zip(x_no_state.columns, regressor_nm.coef_)]
intercept = regressor_nm.intercept_
print('Coefficients: ', coeff)
print('Intercept', intercept)
print('Total number of variables: ', 
    len(coeff) + 1)
