# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import mlpy as ml

@hlp.timeit
def fitDecisionTree(data):
    '''
        Build a decision tree classifier
    '''
    # create the classifier object
    tree = ml.ClassTree(minsize=50)

    # fit the data
    tree.learn(data[0],data[1])

    # return the classifier
    return tree

# the file name of the dataset
r_filename = '../../Data/Chapter3/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# split the data into training and testing
train_x, train_y, \
test_x,  test_y, \
labels = hlp.split_data(
    csv_read, 
    y = 'credit_application'
)

# train the model
classifier = fitDecisionTree((train_x, train_y))

# classify the unseen data
predicted = classifier.pred(test_x)

# print out the results
hlp.printModelSummary(test_y, predicted)