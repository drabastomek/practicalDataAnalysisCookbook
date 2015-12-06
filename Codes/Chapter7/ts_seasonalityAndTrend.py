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

# folder with data
data_folder = '../../Data/Chapter7/'

# colors 
colors = ['#FF6600', '#000000', '#29407C', '#660000']

# read the data
riverFlows = pd.read_csv(data_folder + 'combined_flow.csv', 
    index_col=0, parse_dates=[0])

# detrend the data
detrended = sm.tsa.tsatools.detrend(riverFlows, 
    order=1, axis=0)

# create a data frame with the detrended data
detrended = pd.DataFrame(detrended, index=riverFlows.index, columns=['american_flow_d', 'colum_flow_d'])

# join to the main dataset
riverFlows = riverFlows.join(detrended)

# calculate trend
riverFlows['american_flow_t'] = riverFlows['american_flow'] - riverFlows['american_flow_d']
riverFlows['colum_flow_t'] = riverFlows['colum_flow'] - riverFlows['colum_flow_d']

# plot the data
fig, ax = plt.subplots(2, 3, sharex=True, sharey=True) 

# set the size of the figure explicitly
fig.set_size_inches(12, 7)

# plot the charts for american
ax[0, 0].plot(riverFlows['american_flow'],   colors[0])
ax[0, 1].plot(riverFlows['american_flow_d'], colors[1]) 
ax[0, 2].plot(riverFlows['american_flow_t'], colors[2]) 

# plot the charts for colum
ax[1, 0].plot(riverFlows['colum_flow'],   colors[0])
ax[1, 1].plot(riverFlows['colum_flow_d'], colors[1]) 
ax[1, 2].plot(riverFlows['colum_flow_t'], colors[2]) 

# set titles for columns
ax[0, 0].set_title('Original')
ax[0, 1].set_title('Detrended')
ax[0, 2].set_title('Trend')

# set titles for rows
ax[0, 0].set_ylabel('American')
ax[1, 0].set_ylabel('Colum')

# save the chart
plt.savefig(data_folder + 'charts/detrended.png', dpi=300)
