import pandas as pd 
import re # regular expressions

# regular expression to find any white spaces in a string
space = re.compile(r'\s+')

def fix_string_spaces(columnsToFix):
    '''
        Converts the spaces in the column name to underscore
    '''
    tempColumnNames = [] # list to hold fixed column names

    # loop through all the columns
    for item in columnsToFix:
        # if space is found
        if space.search(item):
            # fix and append to the list
            tempColumnNames \
                .append('_'.join(space.split(item)))
        else:
            # else append the original column name
            tempColumnNames.append(item)

    return tempColumnNames

# url to retrieve
url = 'https://en.wikipedia.org/wiki/' + \
      'List_of_airports_by_IATA_code:_A'

# extract the data from the HTML
url_read = pd.read_html(url, header = 0)[0]

# convert spaces to underscores in column names
url_read.columns = fix_string_spaces(url_read.columns)

# The table has section headings like -AA-
# Let's drop these rows and clean up the index
url_read.dropna(thresh=2, inplace=True)
url_read.index = range(0,len(url_read))

# print out top 10 IATA and Airport names
print(url_read.head(10)[['IATA', 'Airport_name']])