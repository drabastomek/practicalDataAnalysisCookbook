import time             
import numpy as np
import sklearn.metrics as mt                          

def timeit(method):
    '''
        A decorator to time how long it takes to estimate
        the models
    '''

    def timed(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        end = time.time()

        print('The method {0} took {1:2.2f} sec to run.' \
              .format(method.__name__, end-start))
        return result

    return timed

def split_data(data, y, x = 'All', test_size = 0.33):
    '''
        Method to split the data into training and testing
    '''
    # dependent variable
    variables = {'y': y}

    # and all the independent
    if x == 'All':
        allColumns = list(data.columns)
        allColumns.remove(y)
        variables['x'] = allColumns
    else:
        if type(x) != list:
            print('The x parameter has to be a list...')
            sys.exit(1)
        else:
            variables['x'] = x

    # create a variable to flag the training sample
    data['train']  = np.random.rand(len(data)) < (1 - test_size) 

    # split the data into training and testing
    train_x = data[data.train] [variables['x']]
    train_y = data[data.train] [variables['y']]
    test_x  = data[~data.train][variables['x']]
    test_y  = data[~data.train][variables['y']]

    return train_x, train_y, test_x, test_y, variables['x']

def printModelSummary(actual, predicted):
    '''
        Method to print out model summaries
    '''
    print('Overall accuracy of the model is {0:.2f} percent'\
        .format(
            (actual == predicted).sum() / \
            len(actual) * 100))
    print('Classification report: \n', 
        mt.classification_report(actual, predicted))
    print('Confusion matrix: \n', 
        mt.confusion_matrix(actual, predicted))
    print('ROC: ', mt.roc_auc_score(actual, predicted))

def prepareANNDataset(data):
    '''
        Method to prepare the dataset for ANN training
        and testing
    '''
    # we only import this when preparing ANN dataset
    import pybrain.datasets as dt

    # supplementary method to convert list to tuple
    def extract(row):
        return tuple(row)

    # get the number of inputs and outputs
    inputs = len(data[0].columns)
    outputs = len(data[1].axes) + 1

    # create dataset object
    dataset = dt.SupervisedDataSet(inputs, outputs)

    # convert dataframes to lists of tuples
    x = list(data[0].apply(extract, axis=1))
    y = [(item,abs(item - 1)) for item in data[1]]

    # and add samples to the ANN dataset
    for x_item, y_item in zip(x,y):
        dataset.addSample(x_item, y_item)

    return dataset

'''
    The two methods below are introduced to measure
    the inter-cluster heterogeneity and intra-cluster 
    homogeneity.
'''

def pseudo_F(X, labels, centroids):
    '''
        The pseudo F statistic :
        pseudo F = [( [(T - PG)/(G - 1)])/( [(PG)/(n - G)])] 
        The pseudo F statistic was suggested by 
        Calinski and Harabasz (1974) in 
        Calinski, T. and J. Harabasz. 1974. 
            A dendrite method for cluster analysis. 
            Commun. Stat. 3: 1-27.
            http://dx.doi.org/10.1080/03610927408827101

        We borrowed this code from 
        https://github.com/scampion/scikit-learn/blob/master/
        scikits/learn/cluster/__init__.py
    '''
    mean = np.mean(X,axis=0) 
    B = np.sum([ (c - mean)**2 for c in centroids])

    X = X.as_matrix()
    W = np.sum([ (x-centroids[labels[i]])**2 
                 for i, x in enumerate(X)])

    c = len(centroids)
    n = len(X)
    return (B /(c-1))/(W/ (n-c))

def davis_bouldin(X, labels, centroids):
    '''
        The Davis-Bouldin statistic is an internal evaluation
        scheme for evaluating clustering algorithms. It
        encompasses the inter-cluster heterogeneity and 
        intra-cluster homogeneity in one metric.

        The measure was introduced by 
        Davis, D.L. and Bouldin, D.W. in 1979.
            A Cluster Separation Measure
            IEEE Transactions on Pattern Analysis and 
            Machine Intelligence, PAMI-1: 2, 224--227

            http://dx.doi.org/10.1109/TPAMI.1979.4766909
    '''
    distance = np.array([
        np.sqrt(np.sum((x - centroids[labels[i]])**2)) 
        for i, x in enumerate(X.as_matrix())])

    u, c = np.unique(labels, return_counts=True)

    Si = []

    for group, i in enumerate(u):
        Si.append(distance[labels == group].sum() / c[i])

    Mij = []

    for centroid in centroids:
        Mij.append([
            np.sqrt(np.sum((centroid - x)**2)) 
            for x in centroids])

    Rij = [] 
    for i in range(len(centroids)):
        Rij.append([
            0 if i == j 
            else (Si[i] + Si[j]) / Mij[i][j] 
            for j in range(len(centroids))])

    Di = [np.max(elem) for elem in Rij]

    return np.array(Di).sum() / len(centroids)

def getCentroids(data, labels):
    '''
        Method to get the centroids of clusters in clustering
        models that do not return the centroids explicitly
    '''
    # create a copy of the data
    data = data.copy()

    # apply labels
    data['predicted'] = labels

    # and return the centroids
    return np.array(data.groupby('predicted').agg('mean'))

def printClustersSummary(data, labels, centroids):
    '''
        Helper method to automate models assessment
    '''
    print('Pseudo_F: ', pseudo_F(data, labels, centroids))
    print('Davis-Bouldin: ', 
        davis_bouldin(data, labels, centroids))
    # print('Silhouette score: ', 
    #     mt.silhouette_score(data, labels, 
    #         metric='euclidean'))

