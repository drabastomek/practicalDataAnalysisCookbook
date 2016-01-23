import statsmodels.api as sm
import numpy as np

# Load the data from Spector and Mazzeo (1980)
spector_data = sm.datasets.spector.load()

print(spector_data.data)
print(spector_data.endog)
print(spector_data.exog)

print(spector_data.endog_name)
print(spector_data.exog_name)

x = np.array([(1.0, 2), (3.0, 4)], dtype=[('x', float), ('y', int)])

print(x.data)

# spector_data.exog = sm.add_constant(spector_data.exog)

# # Logit Model
# logit_mod = sm.Logit(spector_data.endog, spector_data.exog)
# logit_res = logit_mod.fit()
# print(logit_res.summary())