import networkx as nx
import numpy as np

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
print('Total value of all transactions: {0}' \
    .format(np.sum([dt[2]['amount'] 
        for dt in fraud.edges(data=True)])))

# what do we know about a transaction
p_1_transactions = fraud.out_edges('p_1', data=True)
print('\nData for p_1 purchase from m_1: ', 
    p_1_transactions[0])

p_1_total_amount = np.sum([t[2]['amount'] 
    for t in p_1_transactions])
print('Total amount spent by p_1: {0}' \
    .format(p_1_total_amount))

# are there any disputed transactions?
p_1_disputed_transactions = [t for t in p_1_transactions 
    if t[2]['disputed']]

print('The p_1 has {0} disputed transactions.' \
    .format(len(p_1_disputed_transactions)))

# identify customers with stolen credit cards
all_disputed_transactions = \
    [dt for dt in fraud.edges(data=True) if dt[2]['disputed']]

print('\nDISPUTED TRANSACTIONS')
print('Total number of disputed transactions: {0}' \
    .format(len(all_disputed_transactions)))
print('Total value of disputed transactions: {0}' \
    .format(np.sum([dt[2]['amount'] 
        for dt in all_disputed_transactions])))

people_scammed = list(set(
    [p[0] for p in all_disputed_transactions]))

print('Total number of people scammed: {0}' \
    .format(len(people_scammed)))

print('All disputed transactions:')

for dt in sorted(all_disputed_transactions, 
    key=lambda e: e[0]):
    
    print(dt)