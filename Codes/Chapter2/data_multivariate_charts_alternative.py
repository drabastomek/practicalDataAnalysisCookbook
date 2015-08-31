import seaborn as sns
import sqlalchemy as sa
import pandas as pd
import matplotlib.pyplot as plt

# set the style to white background and grey grid
sns.set_style("whitegrid")

# database credentials
usr  = 'drabast'
pswd = 'pAck7!B0ok'

# create the connection to the database
engine = sa.create_engine(
    'postgresql://{0}:{1}@localhost:5432/{0}' \
    .format(usr, pswd)
)

# prepare the query to extract the data from the database
query = 'SELECT beds, price / 1000 AS price \
    FROM real_estate \
    WHERE sq__ft > 0 \
    AND beds BETWEEN 2 AND 4'

# extract the data
data = pd.read_sql_query(query, engine)

# draw the price distribution for different property sizes
sns.violinplot(x="beds", y="price", data=data, 
    palette="muted"
)

# save the plot to a file
plt.savefig(
    '../../Data/Chapter2/Figures/price_bed_dist.png',
    dpi=300
)