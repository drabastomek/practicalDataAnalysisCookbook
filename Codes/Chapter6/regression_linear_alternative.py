# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sns
sns.set(style="ticks")

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

# split into independent and dependent features
x_red = csv_read[independent_reduced]
y     = csv_read[dependent]

# stack up the principal components
pc_stack = pd.DataFrame()

# stack up the principal components
for col in x_red.columns:
    series = pd.DataFrame()
    series['x'] = x_red[col]
    series['y'] = y
    series['PC'] = col
    pc_stack = pc_stack.append(series)

# Show the results of a linear regression within each
# principal component
sns.lmplot(x='x', y='y', col='PC', hue='PC', data=pc_stack,
           col_wrap=2, size=5)

pl.savefig('../../Data/Chapter6/charts/regression_linear.png',
    dpi=300)

# select only the fel consumption
fuel_cons = ['total_fuel_cons','total_fuel_cons_mmbtu']
x = csv_read[fuel_cons]

# stack up the fuel variables
fuel_stack = pd.DataFrame()

# stack up the fuel consumption variables
for col in fuel_cons:
    series = pd.DataFrame()
    series['x'] = x[col]
    series['y'] = y
    series['fuel'] = col
    fuel_stack = fuel_stack.append(series)

# Show the results of a linear regression for each fuel
# consumption variable
sns.lmplot(x='x', y='y', col='fuel', hue='fuel',
    data=fuel_stack, col_wrap=2, size=5)

pl.savefig(
    '../../Data/Chapter6/charts/regression_linear_fuel.png',
    dpi=300)
