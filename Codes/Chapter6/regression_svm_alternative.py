# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np
import mlpy as ml
import matplotlib.pyplot as plt

@hlp.timeit
def regression_svm(x, y):
    '''
        Estimate a SVM regressor
    '''
    # create the regressor object
    svm = ml.LibSvm(svm_type='nu_svr', kernel_type='rbf', 
        C=0.9, gamma=0.5)

    # estimate the model
    svm.learn(x,y)

    # return the object
    return svm

# simulate dataset
errors = np.random.normal(0, 0.5, size=1000)
x = np.arange(-2, 2, 0.004)
y = 0.8 * x**4 - 2 * x**2 +  errors

# reshape the x array so its in a column form
x_reg = x.reshape(-1, 1)

# estimate the model
regressor = regression_svm(x_reg, y)

# predict the output
predicted = regressor.pred(x_reg)

# and calculate the R^2
score = hlp.get_score(y, predicted)
print(score)

# plot the chart
plt.scatter(x, y)
plt.plot(x, predicted, color='r')
plt.title('Kernel: RBF')
plt.ylim([-4, 8])
plt.text(.9, .9, ('R^2: {0:.2f}'.format(score)),
             transform=plt.gca().transAxes, size=15,
             horizontalalignment='right')

plt.savefig('../../data/Chapter6/charts/regression_svm_alt.pdf')
