import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# change the font size
matplotlib.rc('xtick', labelsize=9)
matplotlib.rc('ytick', labelsize=9)
matplotlib.rc('font', size=14)

# time series tools
import statsmodels.api as sm

def fit_model(data, params, modelType, f, t):
    '''
        Wrapper method to fit and plot the model
    '''
    # create the model object
    model = sm.tsa.ARIMA(data, params)

    # fit the model
    model_res = model.fit(maxiter=600, trend='nc', 
        start_params=[.1] * (params[0] + params[2]), tol=1e06)

    # plot the model
    plot_model(data['1950':], model_res, params, 
        modelType, f, t)

    # and save the figure
    plt.savefig(data_folder + '/charts/' + modelType + '.png', 
        dpi=300)

def plot_model(data, model, params, modelType, f, t):
    # create figure
    fig, ax = plt.subplots(1, figsize=(12, 8))
    
    # plot the data
    data.plot(ax=ax, color=colors[0])

    # plot the forecast
    model.plot_predict(f, t, ax=ax, plot_insample=False)

    # define chart text
    chartText = '{0}: ({1}, {2}, {3})'.format(modelType.split('_')[0], params[0], params[1], params[2])

    # and put it on the chart
    ax.text(0.1, 0.95, chartText, verticalalignment='top', horizontalalignment='left',transform=ax.transAxes)

# folder with data
data_folder = '../../Data/Chapter7/'

# colors 
colors = ['#FF6600', '#000000', '#29407C', '#660000']

# read the data
riverFlows = pd.read_csv(data_folder + 'combined_flow_d.csv', 
    index_col=0, parse_dates=[0])

# fit american models
fit_model(riverFlows['american_flow_r'], (8, 0, 5), 
    'ARMA_American', '1960-11-30', '1962')
fit_model(riverFlows['american_flow_r'], (4, 1, 5), 
    'ARIMA_American', '1960-11-30', '1962')

# fit colum models
fit_model(riverFlows['columbia_flow_r'], (8, 0, 4), 
    'ARMA_Columbia', '1960-09-30', '1962')
fit_model(riverFlows['columbia_flow_r'], (4, 1, 5), 
    'ARIMA_Columbia', '1960-09-30', '1962')