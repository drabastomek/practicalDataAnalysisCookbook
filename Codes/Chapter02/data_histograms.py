import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sqlalchemy as sa

# database credentials
usr  = 'drabast'
pswd = 'pAck7!B0ok'

# create the connection to the database
engine = sa.create_engine(
    'postgresql://{0}:{1}@localhost:5432/{0}' \
    .format(usr, pswd)
)

# read prices from the database
query = 'SELECT price FROM real_estate'
price = pd.read_sql_query(query, engine)

# generate the histograms
ax = sns.distplot(
    price, 
    bins=10, 
    kde=True    # show estimated kernel function
)

# set the title for the plot
ax.set_title('Price histogram with estimated kernel function')

# and save to a file
plt.savefig('../../Data/Chapter02/Figures/price_histogram.pdf')

# finally, show the plot
plt.show()