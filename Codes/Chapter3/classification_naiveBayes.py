# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import sklearn.naive_bayes as nb

@hlp.timeit
def fitNaiveBayes(data):
    '''
        Build the Naive Bayes classifier
    '''
    # create the classifier object
    naiveBayes_classifier = nb.GaussianNB()

    # fit the model
    return naiveBayes_classifier.fit(data[0], data[1])

# the file name of the dataset
r_filename = '../../Data/Chapter3/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# split the data into training and testing
train_x, train_y, \
test_x,  test_y, \
labels = hlp.split_data(
    csv_read, y = 'credit_application')

# train the model
classifier = fitNaiveBayes((train_x, train_y))

# classify the unseen data
predicted = classifier.predict(test_x)

# print out the results
hlp.printModelSummary(test_y, predicted)