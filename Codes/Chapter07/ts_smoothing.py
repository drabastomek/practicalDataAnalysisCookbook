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
data_folder = '../../Data/Chapter07/'

# colors 
colors = ['#FF6600', '#000000', '#29407C', '#660000']

# read the data
riverFlows = pd.read_csv(data_folder + 'combined_flow.csv', 
    index_col=0, parse_dates=[0])

ma_transform12  = pd.rolling_mean(riverFlows, window=12)
ma_transformExp = pd.ewma(riverFlows, span=3)
log_transfrom   = riverFlows.apply(np.log)

# plot the data
fig, ax = plt.subplots(2, 4, sharex=True) 

# set the size of the figure explicitly
fig.set_size_inches(16, 7)

# plot the charts for american
ax[0, 0].plot(riverFlows['american_flow'],     colors[0])
ax[0, 1].plot(ma_transform12['american_flow'], colors[1]) 
ax[0, 2].plot(ma_transformExp['american_flow'],colors[2]) 
ax[0, 3].plot(log_transfrom['american_flow'],  colors[3])

# plot the charts for columbia
ax[1, 0].plot(riverFlows['columbia_flow'],     colors[0])
ax[1, 1].plot(ma_transform12['columbia_flow'], colors[1]) 
ax[1, 2].plot(ma_transformExp['columbia_flow'],colors[2]) 
ax[1, 3].plot(log_transfrom['columbia_flow'],  colors[3])

# set titles for columns
ax[0, 0].set_title('Original')
ax[0, 1].set_title('MA (year)')
ax[0, 2].set_title('MA (exponential)')
ax[0, 3].set_title('Log-transform')

# set titles for rows
ax[0, 0].set_ylabel('American')
ax[1, 0].set_ylabel('Columbia')

# save the chart
plt.savefig(data_folder + 'charts/transform.png', dpi=300)
