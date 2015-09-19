# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import mlpy as ml

@hlp.timeit
def fitLinearSVM(data):
    '''
        Build the linear SVM classifier
    '''
    # create the classifier object
    svm = ml.LibSvm(svm_type='c_svc', 
        kernel_type='linear', C=20.0)

    # fit the data
    svm.learn(data[0],data[1])

    # return the classifier
    return svm

@hlp.timeit
def fitRBFSVM(data):
    '''
        Build the linear SVM classifier
    '''
    # create the classifier object
    svm = ml.LibSvm(svm_type='c_svc', kernel_type='rbf', 
        gamma=0.001, C=20.0)

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
classifier_l = fitLinearSVM((train_x, train_y))
classifier_r = fitRBFSVM((train_x, train_y))

# classify the unseen data
predicted_l = classifier_l.pred(test_x)
predicted_r = classifier_r.pred(test_x)

# print out the results
hlp.printModelSummary(test_y, predicted_l)
hlp.printModelSummary(test_y, predicted_r)