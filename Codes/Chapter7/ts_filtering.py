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
import scipy as sc

# folder with data
data_folder = '../../Data/Chapter7/'

# colors 
colors = ['#FF6600', '#000000', '#29407C', '#660000']

# read the data
riverFlows = pd.read_csv(data_folder + 'combined_flow.csv', 
    index_col=0, parse_dates=[0])

# prepare different filters
MA_filter     = [1] * 12
linear_filter = [d * (1/12) for d in range(0,13)]
gaussian      = [0] * 6 + list(sc.signal.gaussian(13, 2)[:7])

# convolve
conv_ma       = riverFlows.apply(
    lambda col: sm.tsa.filters.convolution_filter(
        col, MA_filter), axis=0).dropna()

conv_linear   = riverFlows.apply(
    lambda col: sm.tsa.filters.convolution_filter(
        col, linear_filter), axis=0).dropna()

conv_gauss    = riverFlows.apply(
    lambda col: sm.tsa.filters.convolution_filter(
        col, gaussian), axis=0).dropna()

# plot the data
fig, ax = plt.subplots(1, 3, sharex=True, sharey=True) 

# set the size of the figure explicitly
fig.set_size_inches(16, 7)

# plot the charts for american
ax[0].plot(MA_filter,     colors[0])
ax[1].plot(linear_filter, colors[1]) 
ax[2].plot(gaussian,  colors[2]) 

# set titles for columns
ax[0].set_title('MA filter')
ax[1].set_title('Linear filter')
ax[2].set_title('Gaussian filter')

ax[0].set_ylim([0,2])

# save the chart
plt.savefig(data_folder + 'charts/filters.png', 
    dpi=300)
plt.close()

# plot the data
fig, ax = plt.subplots(2, 3, sharex=True, sharey=True) 

# set the size of the figure explicitly
fig.set_size_inches(16, 7)

# plot the charts for american
ax[0, 0].plot(conv_ma['american_flow'],     colors[0])
ax[0, 1].plot(conv_linear['american_flow'], colors[1]) 
ax[0, 2].plot(conv_gauss['american_flow'],  colors[2]) 

# plot the charts for columbia
ax[1, 0].plot(conv_ma['columbia_flow'],        colors[0])
ax[1, 1].plot(conv_linear['columbia_flow'],    colors[1]) 
ax[1, 2].plot(conv_gauss['columbia_flow'],     colors[2]) 

# set titles for columns
ax[0, 0].set_title('MA via convolution')
ax[0, 1].set_title('Linear')
ax[0, 2].set_title('Gaussian')

# set titles for rows
ax[0, 0].set_ylabel('American')
ax[1, 0].set_ylabel('Columbia')

# save the chart
plt.savefig(data_folder + 'charts/filtering.png', 
    dpi=300)