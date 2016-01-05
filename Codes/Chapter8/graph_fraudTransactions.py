import networkx as nx
import numpy as np
import collections as c

# import the graph
graph_file = '../../Data/Chapter8/fraud.gz'
fraud = nx.read_graphml(graph_file)

print('\nType of the graph: ', type(fraud))

# population and merchants
nodes = fraud.nodes()

nodes_population = [n for n in nodes if 'p_' in n]
nodes_merchants  = [n for n in nodes if 'm_' in n]

n_population = len(nodes_population)
n_merchants  = len(nodes_merchants)

print('\nTotal population: {0}, number of merchants: {1}' \
    .format(n_population, n_merchants))

# number of transactions
n_transactions = fraud.number_of_edges()
print('Total number of transactions: {0}' \
    .format(n_transactions))

# what do we know about a transaction
p_1_transactions = fraud.out_edges('p_1', data=True)
print('\nMetadata for a transaction: ', 
    list(p_1_transactions[0][2].keys()))

print('Total value of all transactions: {0}' \
    .format(np.sum([t[2]['amount'] 
        for t in fraud.edges(data=True)])))

# identify customers with stolen credit cards
all_disputed_transactions = \
    [dt for dt in fraud.edges(data=True) if dt[2]['disputed']]

print('\nDISPUTED TRANSACTIONS')
print('Total number of disputed transactions: {0}' \
    .format(len(all_disputed_transactions)))
print('Total value of disputed transactions: {0}' \
    .format(np.sum([dt[2]['amount'] 
        for dt in all_disputed_transactions])))

# a list of people scammed
people_scammed = list(set(
    [p[0] for p in all_disputed_transactions]))

print('Total number of people scammed: {0}' \
    .format(len(people_scammed)))

# a list of all disputed transactions
print('All disputed transactions:')

for dt in sorted(all_disputed_transactions, 
    key=lambda e: e[0]):
    print('({0}, {1}: {{time:{2}, amount:{3}}})'\
        .format(dt[0], dt[1], 
         dt[2]['amount'], dt[2]['amount']))

# how much each person lost
transactions = c.defaultdict(list)

for p in all_disputed_transactions:
    transactions[p[0]].append(p[2]['amount'])

for p in sorted(transactions.items(), 
    key=lambda e: np.sum(e[1]), reverse=True):
    print('Value lost by {0}: \t{1}'\
        .format(p[0], np.sum(p[1])))
