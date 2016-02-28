import pandas as pd
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

# read the data
riverFlows = pd.read_csv(data_folder + 'combined_flow.csv', 
    index_col=0, parse_dates=[0])

# plot the data
fig, ax = plt.subplots(2, 2, sharex=True) 

# set the size of the figure explicitly
fig.set_size_inches(8, 7)

# plot the charts for american
sm.graphics.tsa.plot_acf(
    riverFlows['american_flow'].squeeze(), 
    lags=40, ax=ax[0, 0])

sm.graphics.tsa.plot_pacf(
    riverFlows['american_flow'].squeeze(), 
    lags=40, ax=ax[0, 1])

# plot the charts for columbia
sm.graphics.tsa.plot_acf(
    riverFlows['columbia_flow'].squeeze(), 
    lags=40, ax=ax[1, 0])

sm.graphics.tsa.plot_pacf(
    riverFlows['columbia_flow'].squeeze(), 
    lags=40, ax=ax[1, 1])

# set titles for rows
ax[0, 0].set_ylabel('American')
ax[1, 0].set_ylabel('Columbia')

# save the chart
plt.savefig(data_folder + 'charts/acf_pacf.png', dpi=300)
