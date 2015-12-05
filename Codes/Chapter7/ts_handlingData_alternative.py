import pandas as pd
import matplotlib.pyplot as plt
import bokeh.plotting as bkh

# folder with data
data_folder = '../../Data/Chapter7/'

# read the data
riverFlows = pd.read_csv(data_folder + 'combined_flow.csv', 
    index_col=0, parse_dates=[0])

# yearly average
year = riverFlows.resample('A', how='mean')

# defining what tools to show on the charts
TOOLS = 'pan,wheel_zoom,box_zoom,reset,save'

# output file
bkh.output_file(data_folder + 'correlation.html', 
    title='River flows')

# plot data for american river
a = bkh.figure(x_axis_type = 'datetime', tools=TOOLS,
    plot_width=900, plot_height=300)

# plot the lines
a.line(riverFlows.index, riverFlows['american_flow'], 
    color='#1F78B4', legend='Monthly average')
a.line(year.index, year['american_flow'], 
    color='#660033', legend='Yearly average')

# define title and fade the grid lines
a.title = 'American river flow'
a.grid.grid_line_alpha=0.3

# plot data for colum river
c = bkh.figure(x_axis_type = 'datetime', tools=TOOLS,
    plot_width=900, plot_height=300)

# plot the lines
c.line(riverFlows.index, riverFlows['colum_flow'], 
    color='#1F78B4', legend='Monthly average')
c.line(year.index, year['colum_flow'], 
    color='#660033', legend='Yearly average')

# define title and fade the grid lines
c.title = 'Colum river flow'
c.grid.grid_line_alpha=0.3

# show the charts in the browser
bkh.show(bkh.vplot(a, c))