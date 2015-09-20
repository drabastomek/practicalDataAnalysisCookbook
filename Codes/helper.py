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
        and testing. Assumes single valued output
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
    for i in range(len(x)):
        dataset.addSample(x[i], y[i])

    return dataset