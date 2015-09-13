# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import mlpy as ml

@hlp.timeit
def fitSVM(data):
    '''
        Build the SVM classifier
    '''
    # create the classifier object
    svm = ml.LibSvm(svm_type='c_svc', kernel_type='linear', gamma=10)

    # fit the data
    svm.learn(data[0],data[1])

    #return the classifier
    return svm

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
classifier = fitSVM((train_x, train_y))

# classify the unseen data
predicted = classifier.pred(test_x)

# print out the results
hlp.printModelSummary(test_y, predicted)