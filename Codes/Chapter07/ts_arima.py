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

def plot_functions(data, name):
    '''
        Method to plot the ACF and PACF functions
    '''
    # create the figure
    fig, ax = plt.subplots(2)

    # plot the functions
    sm.graphics.tsa.plot_acf(data, lags=18, ax=ax[0])
    sm.graphics.tsa.plot_pacf(data, lags=18, ax=ax[1])

    # set titles for charts
    ax[0].set_title(name.split('_')[-1])
    ax[1].set_title('')

    # set titles for rows
    ax[0].set_ylabel('ACF')
    ax[1].set_ylabel('PACF')

    # save the figure
    plt.savefig(data_folder+'/charts/'+name+'.png', 
        dpi=300)

def fit_model(data, params, modelType, f, t):
    '''
        Wrapper method to fit and plot the model
    '''
    # create the model object
    model = sm.tsa.ARIMA(data, params)

    # fit the model
    model_res = model.fit(maxiter=600, trend='nc', 
        start_params=[.1] * (params[0]+params[2]), tol=1e06)

    # create figure
    fig, ax = plt.subplots(1, figsize=(12, 8))
    
    e = model.geterrors(model_res.params)
    ax.plot(e, colors[3])

    chartText = '{0}: ({1}, {2}, {3})'.format(
        modelType.split('_')[0], params[0], 
        params[1], params[2])

    # and put it on the chart
    ax.text(0.1, 0.95, chartText, transform=ax.transAxes)

    # and save the figure
    plt.savefig(data_folder+'/charts/'+modelType+'_errors.png', 
        dpi=300)


    # plot the model
    plot_model(data['1950':], model_res, params, 
        modelType, f, t)

    # and save the figure
    plt.savefig(data_folder+'/charts/'+modelType+'.png', 
        dpi=300)

def plot_model(data, model, params, modelType, f, t):
    '''
        Method to plot the predictions of the model
    '''
    # create figure
    fig, ax = plt.subplots(1, figsize=(12, 8))
    
    # plot the data
    data.plot(ax=ax, color=colors[0])

    # plot the forecast
    model.plot_predict(f, t, ax=ax, plot_insample=False)

    # define chart text
    chartText = '{0}: ({1}, {2}, {3})'.format(
        modelType.split('_')[0], params[0], 
        params[1], params[2])

    # and put it on the chart
    ax.text(0.1, 0.95, chartText, transform=ax.transAxes)

# folder with data
data_folder = '../../Data/Chapter07/'

# colors 
colors = ['#FF6600', '#000000', '#29407C', '#660000']

# read the data
riverFlows = pd.read_csv(data_folder + 'combined_flow_d.csv', 
    index_col=0, parse_dates=[0])

plot the ACF and PACF functions
plot_functions(riverFlows['american_flow_r'], 
    'ACF_PACF_American')
plot_functions(riverFlows['columbia_flow_r'], 
    'ACF_PACF_Columbia')


# fit american models
fit_model(riverFlows['american_flow_r'], (2, 0, 4), 
    'ARMA_American', '1960-11-30', '1962')
fit_model(riverFlows['american_flow_r'], (2, 1, 4), 
    'ARIMA_American', '1960-11-30', '1962')

# fit colum models
fit_model(riverFlows['columbia_flow_r'], (3, 0, 2), 
    'ARMA_Columbia', '1960-09-30', '1962')
fit_model(riverFlows['columbia_flow_r'], (3, 1, 2), 
    'ARIMA_Columbia', '1960-09-30', '1962')

# fit american models
fit_model(riverFlows['american_flow_r'], (3, 0, 5), 
    'ARMA_American', '1960-11-30', '1962')
fit_model(riverFlows['american_flow_r'], (3, 1, 5), 
    'ARIMA_American', '1960-11-30', '1962')

# fit colum models
fit_model(riverFlows['columbia_flow_r'], (3, 0, 2), 
    'ARMA_Columbia', '1960-09-30', '1962')
fit_model(riverFlows['columbia_flow_r'], (3, 1, 2), 
    'ARIMA_Columbia', '1960-09-30', '1962')