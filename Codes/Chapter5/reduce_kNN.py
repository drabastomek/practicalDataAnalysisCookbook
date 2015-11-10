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
        Build the kNN classifier
    '''
    # create the classifier object
    knn = nb.KNeighborsClassifier()

    # fit the data
    knn.fit(data[0],data[1])

    #return the classifier
    return knn

def prepare_data(data, principal_components, n_components):
    '''
        Prepare the data for the classification
    '''
    # prepare the column names
    cols = ['pc' + str(i) 
        for i in range(0, n_components)]

    # concatenate the data
    data = pd.concat(
        [data, 
            pd.DataFrame(principal_components, 
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

    return (train_x, train_y, test_x, test_y)

def class_fit_predict_print(data):
    '''
        Automating model estimation
    '''
    # train the model
    classifier = fit_kNN_classifier((data[0], data[1]))

    # classify the unseen data
    predicted = classifier.predict(data[2])

    # print out the results
    hlp.printModelSummary(data[3], predicted)

def fit_clean(data):
    '''
        Fit the model without any principal components
    '''
    # split the data into training and testing
    train_x, train_y, \
    test_x,  test_y, \
    labels = hlp.split_data(
        data, 
        y = 'credit_application'
    )

    # fit the model and print the summary
    class_fit_predict_print((train_x, train_y, 
        test_x, test_y))

def fit_pca(data):
    '''
        Fit the model with PCA principal components
    '''
    # keyword parameters for the PCA
    kwrd_params = {'n_components': 5, 'whiten': True}

    # reduce the data
    reduced = reduceDimensions(cd.PCA, data, **kwrd_params)

    # prepare the data for the classifier
    data_l = prepare_data(data, reduced, 
        kwrd_params['n_components'])

    # fit the model
    class_fit_predict_print(data_l)

def fit_fastICA(data):
    '''
        Fit the model with fast ICA principal components
    '''
    # keyword parameters for the PCA
    kwrd_params = {
        'n_components': 5, 
        'algorithm': 'parallel', 
        'whiten': True
    }

    # reduce the data
    reducced = reduceDimensions(cd.FastICA, 
        data, **kwrd_params)

    # prepare the data for the classifier
    data_l = prepare_data(data, reduced, 
        kwrd_params['n_components'])

    # fit the model
    class_fit_predict_print(data_l)

def fit_truncatedSVD(data):
    '''
        Fit the model with truncated SVD principal components
    '''
    # keyword parameters for the PCA
    kwrd_params = {
        'algorithm': 'randomized', 
        'n_components': 5, 
        'n_iter': 5,
        'random_state': 42, 
        'tol': 0.0
    }

    # reduce the data
    reduced = reduceDimensions(cd.TruncatedSVD, 
        data, **kwrd_params)

    # prepare the data for the classifier
    data_l = prepare_data(data, reduced, 
        kwrd_params['n_components'])

    # fit the model
    class_fit_predict_print(data_l)

# the file name of the dataset
r_filename = '../../Data/Chapter3/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# compare models
fit_clean(csv_read)
fit_pca(csv_read)
fit_fastICA(csv_read)
fit_truncatedSVD(csv_read)
