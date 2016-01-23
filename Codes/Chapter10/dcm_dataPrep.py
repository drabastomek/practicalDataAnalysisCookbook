import pandas as pd
import numpy as np

# read datasets
choices_filename      = '../../Data/Chapter10/choices.csv'
alternatives_filename = '../../Data/Chapter10/options.json'

choices      = pd.read_csv(choices_filename)
alternatives = pd.read_json(alternatives_filename).transpose()

# retrieve all considered alternatives
considered = [alt.split(';') 
    for alt in list(choices['available'])]

# create flag of all available alternatives
available = []
alternatives_list = list(alternatives.index)
no_of_alternatives = len(alternatives_list)

for cons in considered:
    f = np.zeros(len(alternatives_list))

    for i, alt in enumerate(alternatives_list):
        if alt in cons:
            f[i] = 1

    available.append(list(f))

# append to the choices DataFrame
alternatives_av = [alt + '_AV' for alt in alternatives_list]
available = pd.DataFrame(available, columns=alternatives_av)

# drop the available column as we don't need it anymore
del choices['available']

# encode the choice variable
choice = list(choices['choice'])
choice = [alternatives_list.index(c) + 1 for c in choice]

choices['choice'] = pd.Series(choice)

# and add the alternatives' attributes
# first, normalize price to be between 0 and 1
max_price = np.max(alternatives['price'])
alternatives['price'] = alternatives['price'] / max_price

# next, create a vector with all attributes
attributes = []
attributes_list = list(alternatives.values)

for attribute in attributes_list:
    attributes += list(attribute)

# fill in to match the number of rows
attributes = [attributes] * len(choices)

# and their names
attributes_names = []

for alternative in alternatives_list:
    for attribute in alternatives.columns:
        attributes_names.append(alternative + '_' + attribute)

# convert to a DataFrame
attributes = pd.DataFrame(attributes, 
    columns=attributes_names)

# and join with the main dataset
choices = choices.join(attributes)

# save as a TSV with .dat extension
with open('../../Data/Chapter10/choices.dat', 'w') as f:
    f.write(choices.to_csv(sep='\t', index=False))