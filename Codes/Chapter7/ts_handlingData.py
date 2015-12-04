import pandas as pd

# files we'll be working with
files=['american.csv', 'judith.csv']

# loop through files
for f in files:
    # read in the dataset
    csv_read = pd.read_csv(
        '../../Data/Chapter7/' + f, 
        index_col=0, parse_dates=[0])

    # index is a DatetimeIndex
    print('\nIndex of {0}'.format(f))
    print(csv_read.index)

    # different ways of selecting data
    print('\nDifferent ways of selecting time series data')
    print('csv_read[:6]')
    print(csv_read[:6])
    print('\ncsv_read.head(6)')
    print(csv_read.head(6))
    print('\ncsv_read[\'1930-01\':\'1930-06\']')
    print(csv_read['1930-01':'1930-06'])

    # shifting the data
    by_month = csv_read.shift(1, freq='M')
    print('\nShifting one month forward')
    print(by_month.head(6))

    by_year = csv_read.shift(12, freq='M')
    print('\nShifting one year forward')
    print(by_year.head(6))

    # averaging by quarter
    quarter = csv_read.resample('Q', how='mean')
    print('\nAveraging by quarter')
    print(quarter.head(2))
