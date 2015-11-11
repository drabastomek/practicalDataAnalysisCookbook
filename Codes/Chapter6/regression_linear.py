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
x     = csv_read[independent]
x_red = csv_read[independent_reduced]
y     = csv_read[dependent]

# estimate the model using all variables (without PC)
z = regression_linear(x,y)
print(z.summary())

# estimate the model using principal components
z_red = regression_linear(x_red,y)
print(z_red.summary())
