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
data_folder = '../../Data/Chapter7/'

# read the data
riverFlows = pd.read_csv(data_folder + 'combined_flow.csv', 
    index_col=0, parse_dates=[0])

# autocorrelation function
acf = {}    # to store the results

for col in riverFlows.columns:
    acf[col] = sm.tsa.stattools.acf(riverFlows[col])

# partial autocorrelation function
pacf = {}

for col in riverFlows.columns:
    pacf[col] = sm.tsa.stattools.pacf(riverFlows[col])

# periodogram (spectral density)
sd = {}

for col in riverFlows.columns:
    sd[col] = sm.tsa.stattools.periodogram(riverFlows[col])

# plot the data
fig, ax = plt.subplots(2, 3) # 2 rows and 3 columns

# set the size of the figure explicitly
fig.set_size_inches(12, 7)

# plot the charts for american
ax[0, 0].plot(acf['american_flow'], 'r')
ax[0, 1].plot(pacf['american_flow'], 'b')
ax[0, 2].plot(sd['american_flow'], 'g')
ax[0, 2].yaxis.tick_right() # shows the numbers on the right

# plot the charts for colum
ax[1, 0].plot(acf['colum_flow'], 'r')
ax[1, 1].plot(pacf['colum_flow'], 'b')
ax[1, 2].plot(sd['colum_flow'], 'g')
ax[1, 2].yaxis.tick_right()

# set titles for columns
ax[0, 0].set_title('ACF')
ax[0, 1].set_title('PACF')
ax[0, 2].set_title('Spectral density')

# set titles for rows
ax[0, 0].set_ylabel('American')
ax[1, 0].set_ylabel('Colum')

# save the chart
plt.savefig(data_folder + 'charts/acf_pacf_sd.png', dpi=300)
