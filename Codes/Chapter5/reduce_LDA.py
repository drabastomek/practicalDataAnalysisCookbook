# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np
import mlpy as ml

@hlp.timeit
def reduce_LDA(x, y):
    '''
        Reduce the dimensions using Linear Discriminant 
        Analysis
    '''
    # create the PCA object
    lda = ml.LDA(method='fast')

    # learn the principal components from all the features
    lda.learn(x, y)

    return lda

# the file name of the dataset
r_filename = '../../Data/Chapter5/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# split into independent and dependent features
x = csv_read[csv_read.columns[:-1]]
y = csv_read[csv_read.columns[-1]]

# reduce the dimensionality
z = reduce_LDA(x, y)