# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import statsmodels.api as sm

@hlp.timeit
def regression_ols(x,y):
    '''
        Estimate a linear regression
    '''
    # add a constant to the data
    x = sm.add_constant(x)

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
regressor = regression_ols(x,y)
print(regressor.summary())

# remove insignificant variables
significant = ['total_fuel_cons', 'total_fuel_cons_mmbtu']
x_red = x[significant]

# estimate the model with limited number of variables
regressor = regression_ols(x_red,y)
print(regressor.summary())