# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import numpy as np
import sklearn.svm as sv
import matplotlib.pyplot as plt
import optunity as opt
import optunity.metrics as mt

# simulated dataset
x = np.arange(-2, 2, 0.002)
errors = np.random.normal(0, 0.5, size=len(x))
y = 0.8 * x**4 - 2 * x**2 +  errors

# reshape the x array so its in a column form
x_reg = x.reshape(-1, 1)

@opt.cross_validated(x=x_reg, y=y, num_folds=10, num_iter=5)
def regression_svm(
    x_train, y_train, x_test, y_test, logC, logGamma):
    '''
        Estimate a SVM regressor
    '''
    # create the regressor object
    svm = sv.SVR(kernel='rbf', 
        C=0.1 * logC, gamma=0.1 * logGamma)

    # estimate the model
    svm.fit(x_train,y_train)

    # decision function
    decision_values = svm.decision_function(x_test)

    # return the object
    return mt.roc_auc(y_test, decision_values)

# find the optimal values of C and gamma
hps, _, _ = opt.maximize(regression_svm, num_evals=10, 
    logC=[3, 10], logGamma=[3, 20])

# and the values are...
print('The optimal values are: C - {0:.2f}, gamma - {1:.2f}'\
    .format(0.1 * hps['logC'], 0.1 * hps['logGamma']))

# estimate the model with optimal values
regressor = sv.SVR(kernel='rbf', 
            C=0.1 * hps['logC'], 
            gamma=0.1 * hps['logGamma'])\
        .fit(x_reg, y)

# predict the output
predicted = regressor.predict(x_reg)

# and calculate the R^2
score = hlp.get_score(y, predicted)
print('R2: ', score)

# plot the chart
plt.scatter(x, y)
plt.plot(x, predicted, color='r')
plt.title('Kernel: RBF')
plt.ylim([-4, 8])
plt.text(.9, .9, ('R^2: {0:.2f}'.format(score)),
             transform=plt.gca().transAxes, size=15,
             horizontalalignment='right')

plt.savefig(
    '../../data/Chapter06/charts/regression_svm_alt.png',
    dpi=300
)
