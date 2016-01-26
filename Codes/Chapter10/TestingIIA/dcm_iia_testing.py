import pandas as pd

# read the html tables
old_model = 'dcm_mnl_simul.html'
new_model = 'dcm_iia_simul.html'

old_model_p = pd.read_html(old_model, header = 0)[3]
new_model_p = pd.read_html(new_model, header = 0)[3]

# let's look at only two columns
cols = ['P_AA777_Y', 'P_AA777_V']

# make sure that there are no zeros
old_model_p = old_model_p[cols]
old_model_p = old_model_p[old_model_p[cols[0]] != 0]
old_model_p = old_model_p[old_model_p[cols[1]] != 0]

new_model_p = new_model_p[cols]
new_model_p = new_model_p[new_model_p[cols[0]] != 0]
new_model_p = new_model_p[new_model_p[cols[1]] != 0]

# calculate the ratios
old_model_p['ratios_old'] = old_model_p \
    .apply(lambda row: row['P_AA777_V'] / row['P_AA777_Y'], 
        axis=1)

new_model_p['ratios_new'] = new_model_p \
    .apply(lambda row: row['P_AA777_V'] / row['P_AA777_Y'], 
        axis=1)

# join with the old model results 
differences = old_model_p.join(new_model_p, rsuffix='_new')

# and calculate the differences
differences['diff'] = differences\
    .apply(lambda row: row['ratios_new'] - row['ratios_old'],
        axis=1)

# calculate the descriptive stats for the columns
print(differences[['ratios_old', 'ratios_new', 'diff']] \
    .describe())