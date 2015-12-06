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

def period_mean(data, freq):
    '''
        Method to calculate mean for each frequency
    '''
    return np.array(
        [np.mean(data[i::freq]) for i in range(freq)])

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
detrended = pd.DataFrame(detrended, index=riverFlows.index, 
    columns=['american_flow_d', 'colum_flow_d'])

# join to the main dataset
riverFlows = riverFlows.join(detrended)

# calculate trend
riverFlows['american_flow_t'] = riverFlows['american_flow'] \
    - riverFlows['american_flow_d']
riverFlows['colum_flow_t'] = riverFlows['colum_flow'] \
    - riverFlows['colum_flow_d']

nobs = len(riverFlows)
freq = 12   # yearly seasonality

seasonal = pd.DataFrame()
resid = pd.DataFrame()

for col in ['american_flow', 'colum_flow']:
    period_averages = period_mean(riverFlows[col], freq)
    riverFlows[col+'_s'] = np.tile(period_averages, nobs // freq + 1)[:nobs]
    riverFlows[col+'_r'] = np.array(riverFlows[col]) - np.array(riverFlows[col+'_s'])

# save the decomposed dataset
with open(data_folder + 'combined_flow_d.csv', 'w') as o:
    o.write(riverFlows.to_csv(ignore_index=True))

# plot the data
fig, ax = plt.subplots(2, 3, sharex=True, sharey=True) 

# set the size of the figure explicitly
fig.set_size_inches(12, 7)

# plot the charts for american
ax[0, 0].plot(riverFlows['american_flow_t'], colors[0])
ax[0, 1].plot(riverFlows['american_flow_s'], colors[1]) 
ax[0, 2].plot(riverFlows['american_flow_r'], colors[2]) 

# plot the charts for colum
ax[1, 0].plot(riverFlows['colum_flow_t'], colors[0])
ax[1, 1].plot(riverFlows['colum_flow_s'], colors[1]) 
ax[1, 2].plot(riverFlows['colum_flow_r'], colors[2]) 

# set titles for columns
ax[0, 0].set_title('Trend')
ax[0, 1].set_title('Seasonality')
ax[0, 2].set_title('Residuals')

# set titles for rows
ax[0, 0].set_ylabel('American')
ax[1, 0].set_ylabel('Colum')

# save the chart
plt.savefig(data_folder + 'charts/detrended.png', dpi=300)
