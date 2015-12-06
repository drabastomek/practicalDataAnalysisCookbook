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
linear_filter = [1 - d * (1/12) for d in range(0,13)]
high_filter   = [0] * 6 + [1] * 6
gaussian      = sc.signal.gaussian(12, 2)

# convolve
conv_linear   = riverFlows.apply(
    lambda col: sm.tsa.filters.convolution_filter(
        col, linear_filter), axis=0).dropna()

conv_high = riverFlows.apply(
    lambda col: sm.tsa.filters.convolution_filter(
        col, high_filter), axis=0).dropna()

conv_gauss    = riverFlows.apply(
    lambda col: sm.tsa.filters.convolution_filter(
        col, gaussian), axis=0).dropna()

# plot the data
fig, ax = plt.subplots(2, 4, sharex=True) 

# set the size of the figure explicitly
fig.set_size_inches(16, 7)

# plot the charts for american
ax[0, 0].plot(riverFlows['american_flow'],  colors[0])
ax[0, 1].plot(conv_linear['american_flow'], colors[1]) 
ax[0, 2].plot(conv_high['american_flow'],   colors[2]) 
ax[0, 3].plot(conv_gauss['american_flow'],  colors[3]) 

# plot the charts for colum
ax[1, 0].plot(riverFlows['colum_flow'],     colors[0])
ax[1, 1].plot(conv_linear['colum_flow'],    colors[1]) 
ax[1, 2].plot(conv_high['colum_flow'],      colors[2]) 
ax[1, 3].plot(conv_gauss['colum_flow'],     colors[3]) 

# set titles for columns
ax[0, 0].set_title('Original')
ax[0, 1].set_title('Linear')
ax[0, 2].set_title('High pass')
ax[0, 3].set_title('Gaussian')

# set titles for rows
ax[0, 0].set_ylabel('American')
ax[1, 0].set_ylabel('Colum')

# save the chart
plt.savefig(data_folder + 'charts/filtering.png', 
    dpi=300)