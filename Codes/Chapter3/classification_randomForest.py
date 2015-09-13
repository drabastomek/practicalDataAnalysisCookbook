# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import sklearn.ensemble as en

@hlp.timeit
def fitRandomForest(data):
    '''
        Build a random forest classifier
    '''
    # create the classifier object
    forest = en.RandomForestClassifier(n_jobs=-1, 
        min_samples_split=10, n_estimators=1000, 
        class_weight="auto")

    # fit the data
    return forest.fit(data[0],data[1])

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
classifier = fitRandomForest((train_x, train_y))

# classify the unseen data
predicted = classifier.predict(test_x)

# print out the results
hlp.printModelSummary(test_y, predicted)

# print out the importance of features
coef = {nm: coeff 
    for (nm, coeff) 
    in zip(labels, classifier.feature_importances_)
}
print(coef)