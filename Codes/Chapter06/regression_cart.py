# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import sklearn.tree as sk

@hlp.timeit
def regression_cart(x,y):
    '''
        Estimate a CART regressor
    '''
    # create the regressor object
    cart = sk.DecisionTreeRegressor(min_samples_split=80,
        max_features="auto", random_state=66666, 
        max_depth=5)

    # estimate the model
    cart.fit(x,y)

    # return the object
    return cart

# the file name of the dataset
r_filename = '../../Data/Chapter06/power_plant_dataset_pc.csv'

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
regressor = regression_cart(x,y)

# print out the results
print('R2: ', regressor.score(x,y))

for counter, (nm, label) \
    in enumerate(
        zip(x.columns, regressor.feature_importances_)
    ):
    print("{0}. {1}: {2}".format(counter, nm,label))

# and export to a .dot file
sk.export_graphviz(regressor, 
    out_file='../../Data/Chapter06/CART/tree.dot')

# estimate the model using Principal Components only
regressor_red = regression_cart(x_red,y)

# print out the results
print('R: ', regressor_red.score(x_red,y))

for counter, (nm, label) \
    in enumerate(
        zip(x_red.columns, regressor_red.feature_importances_)
    ):
    print("{0}. {1}: {2}".format(counter, nm,label))

# and export to a .dot file
sk.export_graphviz(regressor_red, 
    out_file='../../Data/Chapter06/CART/tree_red.dot')
