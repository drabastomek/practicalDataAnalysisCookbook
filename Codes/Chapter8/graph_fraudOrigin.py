import networkx as nx
import numpy as np
import collections as c

# import the graph
graph_file = '../../Data/Chapter8/fraud.gz'
fraud = nx.read_graphml(graph_file)

# identify customers with stolen credit cards
people_scammed = c.defaultdict(list)

for (person, merchant, data) in fraud.edges(data=True):
    if data['disputed']:
        people_scammed[person].append(data['time'])

print('\nTotal number of people scammed: {0}' \
    .format(len(people_scammed)))

# what was the time of the first disputed transaction for each
# scammed person
stolen_time = {}

for person in people_scammed:
    stolen_time[person] = \
        np.min(people_scammed[person])

# let's find the common merchants for all those scammed
merchants = c.defaultdict(list)
for person in people_scammed:
    edges = fraud.out_edges(person, data=True)
    
    for (person, merchant, data) in edges:
        if  stolen_time[person] - data['time'] <= 2 and \
            stolen_time[person] - data['time'] >= 0:

            merchants[merchant].append(person)

# for merchant in merchants:
#     merchants[merchant] = len(set(merchants[merchant]))

merchants = [(merch, len(set(merchants[merch]))) for merch in merchants]

print('\nTop 5 merchants where people made purchases')
print('shortly before their credit cards were stolen')
print(sorted(merchants, key=lambda e: e[1], reverse=True)[:5])