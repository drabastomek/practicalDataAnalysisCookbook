# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import statsmodels.api as sm
import statsmodels.genmod.families.links as fm

@hlp.timeit
def fitLogisticRegression(data):
    '''
        Build the logistic regression classifier
    '''
    # create the classifier object
    logistic_classifier = sm.GLM(data[1], data[0], 
        family=sm.families.Binomial(link=fm.logit))

    # fit the data
    return logistic_classifier.fit()

# the file name of the dataset
r_filename = '../../Data/Chapter03/bank_contacts.csv'

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
classifier = fitLogisticRegression((train_x, train_y))

# classify the unseen data
predicted = classifier.predict(test_x)

# assign the class
predicted = [1 if elem > 0.5 else 0 for elem in predicted]

# print out the results
hlp.printModelSummary(test_y, predicted)

# print out the parameters
print(classifier.summary())