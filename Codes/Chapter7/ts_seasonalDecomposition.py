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

for col in riverFlows.columns:
    # seasonal decomposition of the data
    sd = sm.tsa.seasonal_decompose(riverFlows[col], model='a', freq=12)

    riverFlows[col + '_resid'] = sd.resid \
        .fillna(np.mean(sd.resid))

    riverFlows[col + '_trend'] = sd.trend \
        .fillna(np.mean(sd.trend))

    riverFlows[col + '_seas'] = sd.seasonal \
        .fillna(np.mean(sd.seasonal))

# plot the data
fig, ax = plt.subplots(2, 3, sharex=True, sharey=True) 

# set the size of the figure explicitly
fig.set_size_inches(12, 7)

# plot the charts for american
ax[0, 0].plot(riverFlows['american_flow_resid'], colors[0])
ax[0, 1].plot(riverFlows['american_flow_trend'], colors[1]) 
ax[0, 2].plot(riverFlows['american_flow_seas'],  colors[2]) 

# plot the charts for columbia
ax[1, 0].plot(riverFlows['columbia_flow_resid'], colors[0])
ax[1, 1].plot(riverFlows['columbia_flow_trend'], colors[1]) 
ax[1, 2].plot(riverFlows['columbia_flow_seas'],  colors[2]) 

# set titles for columns
ax[0, 0].set_title('Residuals')
ax[0, 1].set_title('Trend')
ax[0, 2].set_title('Seasonality')

# set titles for rows
ax[0, 0].set_ylabel('American')
ax[1, 0].set_ylabel('Columbia')

# save the chart
plt.savefig(data_folder + 'charts/decomposed.png', dpi=300)
