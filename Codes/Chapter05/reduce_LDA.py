# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
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

# the file name of the dataset
r_filename = '../../Data/Chapter05/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# split into independent and dependent features
x = csv_read[csv_read.columns[:-1]]
y = csv_read[csv_read.columns[-1]]

# split the original data into training and testing
train_x_orig, train_y_orig, \
test_x_orig,  test_y_orig, \
labels_orig = hlp.split_data(
    csv_read, 
    y = 'credit_application'
)

# reduce the dimensionality
csv_read['reduced'] = reduce_LDA(x, y).transform(x)

# split the reduced data into training and testing
train_x_r, train_y_r, \
test_x_r,  test_y_r, \
labels_r = hlp.split_data(
    csv_read, 
    y = 'credit_application',
    x = ['reduced']
)

# train the models
classifier_r    = fitLinearSVM((train_x_r, train_y_r))
classifier_orig = fitLinearSVM((train_x_orig, train_y_orig))

# classify the unseen data
predicted_r    = classifier_r.pred(test_x_r)
predicted_orig = classifier_orig.pred(test_x_orig)

# print out the results
hlp.printModelSummary(test_y_r, predicted_r)
hlp.printModelSummary(test_y_orig, predicted_orig)
