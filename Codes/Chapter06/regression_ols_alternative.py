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

# the file name of the dataset
r_filename = '../../Data/Chapter06/power_plant_dataset_pc.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# remove insignificant variables
significant = ['total_fuel_cons_mmbtu']
x = csv_read[significant]

# x = np.array(csv_read[independent_reduced[0]]).reshape(-1,1)
y = csv_read[csv_read.columns[-1]]

# estimate the model using all variables (without PC)
regressor = regression_linear(x,y)

# predict the output
predicted = regressor.pred(x)

# and calculate the R^2
score = hlp.get_score(y, predicted)
print('R2: ', score)