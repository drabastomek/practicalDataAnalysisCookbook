# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np
import statsmodels.api as sm

@hlp.timeit
def regression_linear(x,y):
    '''
        Estimate a linear regression
    '''
    # create the model object
    model = sm.OLS(y, x)

    # and return the fit model
    return model.fit()

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
regressor = regression_linear(x,y)
print(regressor.summary())

# remove insignificant variables
significant = [
    'fuel_aer_COL', 'fuel_aer_DFO', 'fuel_aer_HYC', 
    'fuel_aer_NUC', 'mover_CT', 'mover_HY', 'state_KY', 
    'state_TX', 'state_WV', 'mover_ST', 'state_AL', 
    'mover_GT']

x_red = x[significant]

# estimate the model with limited number of variables
regressor = regression_linear(x_red,y)
print(regressor.summary())