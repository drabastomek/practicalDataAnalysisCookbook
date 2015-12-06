import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# change the font size
matplotlib.rc('xtick', labelsize=9)
matplotlib.rc('ytick', labelsize=9)
matplotlib.rc('font', size=14)

def holt_transform(column, alpha):
    '''
        Method to apply Holt transform

        The transform is given as
        y(t) = alpha * x(t) + (1-alpha) y(t-1)
    '''
    # create an np.array from the column
    original = np.array(column)

    # starting point for the transformation
    transformed = [original[0]]

    # apply the transform to the rest of the data
    for i in range(1, len(original)):
        transformed.append(
            original[i] * alpha + 
            (1-alpha) * transformed[-1])

    return transformed

# time series tools
import statsmodels.api as sm

# folder with data
data_folder = '../../Data/Chapter7/'

# colors 
colors = ['#FF6600', '#000000', '#29407C', '#660000']

# read the data
riverFlows = pd.read_csv(data_folder + 'combined_flow.csv', 
    index_col=0, parse_dates=[0])

ma_transform12 = riverFlows.apply(
    lambda col: holt_transform(col, 0.5), axis=0)

# plot the data
fig, ax = plt.subplots(2, 2, sharex=True) 

# set the size of the figure explicitly
fig.set_size_inches(12, 7)

# plot the charts for american
ax[0, 0].plot(riverFlows['american_flow'],    colors[0])
ax[0, 1].plot(ma_transform12['american_flow'],colors[1]) 

# plot the charts for columbia
ax[1, 0].plot(riverFlows['columbia_flow'],    colors[0])
ax[1, 1].plot(ma_transform12['columbia_flow'],colors[1]) 

# set titles for columns
ax[0, 0].set_title('Original')
ax[0, 1].set_title('Holt transform')

# set titles for rows
ax[0, 0].set_ylabel('American')
ax[1, 0].set_ylabel('Columbia')

# save the chart
plt.savefig(data_folder + 'charts/holt_transform.png', 
    dpi=300)
