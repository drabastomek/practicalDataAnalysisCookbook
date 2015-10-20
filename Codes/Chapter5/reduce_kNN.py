# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import sklearn.decomposition as cd
import sklearn.neighbors as nb

@hlp.timeit
def reduceDimensions(method, data, **kwrd_params):
    '''
        Reduce the dimensions
    '''
    # split into independent and dependent features
    x = data[data.columns[:-1]]
    y = data[data.columns[-1]]

    # create the reducer object
    reducer = method(**kwrd_params)

    # fit the data
    reducer.fit(x)

    # return the classifier
    return reducer.transform(x)

@hlp.timeit
def fit_kNN_classifier(data):
    '''
        Build the linear SVM classifier
    '''
    # create the classifier object
    knn = nb.KNeighborsClassifier(n_neighbors=3)

    # fit the data
    knn.fit(data[0],data[1])

    #return the classifier
    return knn

def class_fit_predict_print(train_x, train_y, test_x, test_y):
    # train the model
    classifier = fit_kNN_classifier((train_x, train_y))

    # classify the unseen data
    predicted = classifier.predict(test_x)

    # print out the results
    hlp.printModelSummary(test_y, predicted)

def fit_clean(data):
    # split the data into training and testing
    train_x, train_y, \
    test_x,  test_y, \
    labels = hlp.split_data(
        data, 
        y = 'credit_application'
    )

    class_fit_predict_print(train_x, train_y, test_x, test_y)

def fit_pca(data):
    kwrd_params = {'n_components': 5, 'whiten': True}

    reduced = reduceDimensions(cd.PCA, data, **kwrd_params)

    cols = ['pc' + str(i) 
        for i in range(0, kwrd_params['n_components'])]

    data = pd.concat(
        [data, 
            pd.DataFrame(reduced, 
                columns=cols)], 
            axis=1, join_axes=[data.index])

    # split the data into training and testing
    train_x, train_y, \
    test_x,  test_y, \
    labels = hlp.split_data(
        data, 
        y = 'credit_application',
        x = cols
    )

    class_fit_predict_print(train_x, train_y, test_x, test_y) 

def fit_fastICA(data):
    kwrd_params = {
        'n_components': 5, 'algorithm': 'parallel', 'whiten': True
    }

    reduced = reduceDimensions(cd.FastICA, data, **kwrd_params)

    cols = ['pc' + str(i) 
        for i in range(0, kwrd_params['n_components'])]

    data = pd.concat(
        [data, 
            pd.DataFrame(reduced, 
                columns=cols)], 
            axis=1, join_axes=[data.index])

    # split the data into training and testing
    train_x, train_y, \
    test_x,  test_y, \
    labels = hlp.split_data(
        data, 
        y = 'credit_application',
        x = cols
    )

    class_fit_predict_print(train_x, train_y, test_x, test_y) 

def fit_truncatedSVD(data):
    kwrd_params = {
        'algorithm': 'randomized', 'n_components': 5, 'n_iter': 5,
        'random_state': 42, 'tol': 0.0
    }

    reduced = reduceDimensions(cd.TruncatedSVD, data, **kwrd_params)

    cols = ['pc' + str(i) 
        for i in range(0, kwrd_params['n_components'])]

    data = pd.concat(
        [data, 
            pd.DataFrame(reduced, 
                columns=cols)], 
            axis=1, join_axes=[data.index])

    # split the data into training and testing
    train_x, train_y, \
    test_x,  test_y, \
    labels = hlp.split_data(
        data, 
        y = 'credit_application',
        x = cols
    )

    class_fit_predict_print(train_x, train_y, test_x, test_y) 


# the file name of the dataset
r_filename = '../../Data/Chapter3/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# compare models
fit_clean(csv_read)
fit_pca(csv_read)
fit_fastICA(csv_read)
fit_truncatedSVD(csv_read)
