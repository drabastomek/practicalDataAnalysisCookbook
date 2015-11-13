# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np
import sklearn.svm as sv

import matplotlib.pyplot as plt


@hlp.timeit
def regression_svm(x, y, **kw_params):
    '''
        Estimate a SVM regressor
    '''
    # create the regressor object
    svm = sv.SVR(**kw_params)

    # estimate the model
    svm.fit(x,y)

    # return the object
    return svm

# simulate dataset
errors = np.random.normal(0, 0.5, size=1000)
x = np.arange(-2, 2, 0.004)
y = 0.8 * x**4 - 2 * x**2 +  errors

# reshape the x array so its in a column form
x_reg = x.reshape(-1, 1)

models_to_test = [
    {'kernel': 'linear'}, 
    {'kernel': 'poly','gamma': 0.5, 'C': 0.9, 'degree': 4}, 
    {'kernel': 'poly','gamma': 0.5, 'C': 0.9, 'degree': 6}, 
    {'kernel': 'rbf','gamma': 0.5, 'C': 0.9}
]

plt.figure(figsize=(len(models_to_test) * 2 + 3, 9.5))
plt.subplots_adjust(left=.05, right=.95, 
    bottom=.05, top=.96, wspace=.1, hspace=.15)


for i, model in enumerate(models_to_test):
    # estimate the model
    regressor = regression_svm(x_reg, y, **model)

    # score 
    score = regressor.score(x_reg, y)

    # plot the chart
    plt.subplot(2, 2, i + 1)
    if model['kernel'] == 'poly':
        plt.title('Kernel: {0}, deg: {1}'\
            .format(model['kernel'], model['degree']))
    else:
        plt.title('Kernel: {0}'.format(model['kernel']))
    plt.ylim([-4, 8])
    plt.scatter(x, y)
    plt.plot(x, regressor.predict(x_reg), color='r')
    plt.text(.9, .9, ('R^2: {0:.2f}'.format(score)),
                 transform=plt.gca().transAxes, size=15,
                 horizontalalignment='right')

plt.savefig('../../data/Chapter6/charts/regression_svm.pdf')
