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

bkfilter = sm.tsa.filters.bkfilter(riverFlows, 18, 96, 12)
hpcycle, hptrend = sm.tsa.filters.hpfilter(riverFlows, 129600)
cfcycle, cftrend = sm.tsa.filters.cffilter(riverFlows, 
    18, 96, False)

# plot the data
fig, ax = plt.subplots(2, 4, sharex=True, sharey=True) 

# set the size of the figure explicitly
fig.set_size_inches(16, 7)

# plot the charts for american
ax[0, 0].plot(riverFlows['american_flow'],  colors[0])
ax[0, 1].plot(bkfilter['american_flow'], colors[1]) 
ax[0, 2].plot(hpcycle['american_flow'],   colors[2]) 
ax[0, 2].plot(hptrend['american_flow'],   colors[3]) 
ax[0, 3].plot(cfcycle['american_flow'],  colors[2]) 
ax[0, 3].plot(cftrend['american_flow'],  colors[3]) 

# plot the charts for columbia
ax[1, 0].plot(riverFlows['columbia_flow'],  colors[0])
ax[1, 1].plot(bkfilter['columbia_flow'], colors[1]) 
ax[1, 2].plot(hpcycle['columbia_flow'],   colors[2]) 
ax[1, 2].plot(hptrend['columbia_flow'],   colors[3]) 
ax[1, 3].plot(cfcycle['columbia_flow'],  colors[2]) 
ax[1, 3].plot(cftrend['columbia_flow'],  colors[3]) 

# set titles for columns
ax[0, 0].set_title('Original')
ax[0, 1].set_title('Baxter-King')
ax[0, 2].set_title('Hodrick-Prescott')
ax[0, 3].set_title('Christiano-Fitzgerald')

# set titles for rows
ax[0, 0].set_ylabel('American')
ax[1, 0].set_ylabel('Columbia')

# save the chart
plt.savefig(data_folder + 'charts/filtering_alternative.png', 
    dpi=300)