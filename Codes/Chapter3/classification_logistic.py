# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
# import sklearn.linear_model as lm
# import sklearn.cross_validation as cv

import statsmodels.api as sm

# data = sm.datasets.scotland.load()
# # print(data.exog)

# # data.exog = sm.add_constant(data.exog)

# # print(data)
# gamma_model = sm.GLM(data.endog, data.exog, family=sm.families.Gamma())
# gamma_results = gamma_model.fit()

# print(gamma_results.params)
# print(gamma_results.pvalues)

@hlp.timeit
def fitLogisticRegression(data):
    '''
        Build the logistic regression classifier
    '''
    # create the classifier object
    logistic_classifier = sm.GLM(data[1], data[0], family=sm.families.Binomial())

    # fit the data
    return logistic_classifier.fit()

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
classifier = fitLogisticRegression((train_x, train_y))

# classify the unseen data
predicted = classifier.predict(test_x)

# assign the class
predicted = [1 if elem > 0.5 else 0 for elem in predicted]

# print out the results
hlp.printModelSummary(test_y, predicted)

# print out the parameters
print(classifier.summary())