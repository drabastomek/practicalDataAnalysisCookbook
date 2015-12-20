import networkx as nx
import networkx.algorithms as alg
import numpy as np
import matplotlib.pyplot as plt

# create graph object
twitter = nx.Graph()

# add users
twitter.add_node('Tom', {'age': 34})
twitter.add_node('Rachel', {'age': 33})
twitter.add_node('Skye', {'age': 29})
twitter.add_node('Bob', {'age': 45})
twitter.add_node('Mike', {'age': 23})
twitter.add_node('Peter', {'age': 46})
twitter.add_node('Matt', {'age': 58})
twitter.add_node('Lester', {'age': 65})
twitter.add_node('Jack', {'age': 32})
twitter.add_node('Max', {'age': 75})
twitter.add_node('Linda', {'age': 23})
twitter.add_node('Rory', {'age': 18})
twitter.add_node('Richard', {'age': 24})
twitter.add_node('Jackie', {'age': 25})
twitter.add_node('Alex', {'age': 24})
twitter.add_node('Bart', {'age': 33})
twitter.add_node('Greg', {'age': 45})
twitter.add_node('Rob', {'age': 19})
twitter.add_node('Markus', {'age': 21})
twitter.add_node('Glenn', {'age': 24})

# add posts
twitter.node['Rory']['posts'] = 182
twitter.node['Rob']['posts'] = 111
twitter.node['Markus']['posts'] = 159
twitter.node['Linda']['posts'] = 128
twitter.node['Mike']['posts'] = 289
twitter.node['Alex']['posts'] = 188
twitter.node['Glenn']['posts'] = 252
twitter.node['Richard']['posts'] = 106
twitter.node['Jackie']['posts'] = 138
twitter.node['Skye']['posts'] = 78
twitter.node['Jack']['posts'] = 62
twitter.node['Bart']['posts'] = 38
twitter.node['Rachel']['posts'] = 89
twitter.node['Tom']['posts'] = 23
twitter.node['Bob']['posts'] = 21
twitter.node['Greg']['posts'] = 41
twitter.node['Peter']['posts'] = 64
twitter.node['Matt']['posts'] = 8
twitter.node['Lester']['posts'] = 4
twitter.node['Max']['posts'] = 2

# add followers
twitter.add_edge('Rob', 'Rory', {'Weight': 1})
twitter.add_edge('Markus', 'Rory', {'Weight': 1})
twitter.add_edge('Markus', 'Rob', {'Weight': 5})
twitter.add_edge('Mike', 'Rory', {'Weight': 1})
twitter.add_edge('Mike', 'Rob', {'Weight': 1})
twitter.add_edge('Mike', 'Markus', {'Weight': 1})
twitter.add_edge('Mike', 'Linda', {'Weight': 5})
twitter.add_edge('Alex', 'Rob', {'Weight': 1})
twitter.add_edge('Alex', 'Markus', {'Weight': 1})
twitter.add_edge('Alex', 'Mike', {'Weight': 1})
twitter.add_edge('Glenn', 'Rory', {'Weight': 1})
twitter.add_edge('Glenn', 'Rob', {'Weight': 1})
twitter.add_edge('Glenn', 'Markus', {'Weight': 1})
twitter.add_edge('Glenn', 'Linda', {'Weight': 2})
twitter.add_edge('Glenn', 'Mike', {'Weight': 1})
twitter.add_edge('Glenn', 'Alex', {'Weight': 1})
twitter.add_edge('Richard', 'Rob', {'Weight': 1})
twitter.add_edge('Richard', 'Linda', {'Weight': 1})
twitter.add_edge('Richard', 'Mike', {'Weight': 1})
twitter.add_edge('Richard', 'Alex', {'Weight': 1})
twitter.add_edge('Richard', 'Glenn', {'Weight': 1})
twitter.add_edge('Jackie', 'Linda', {'Weight': 1})
twitter.add_edge('Jackie', 'Mike', {'Weight': 1})
twitter.add_edge('Jackie', 'Glenn', {'Weight': 1})
twitter.add_edge('Jackie', 'Skye', {'Weight': 1})
twitter.add_edge('Tom', 'Rachel', {'Weight': 5})
twitter.add_edge('Rachel', 'Bart', {'Weight': 1})
twitter.add_edge('Tom', 'Bart', {'Weight': 2})
twitter.add_edge('Jack', 'Skye', {'Weight': 1})
twitter.add_edge('Bart', 'Skye', {'Weight': 1})
twitter.add_edge('Rachel', 'Skye', {'Weight': 1})
twitter.add_edge('Greg', 'Bob', {'Weight': 1})
twitter.add_edge('Peter', 'Greg', {'Weight': 1})
twitter.add_edge('Lester', 'Matt', {'Weight': 1})
twitter.add_edge('Max', 'Matt', {'Weight': 1})
twitter.add_edge('Rachel', 'Linda', {'Weight': 1})
twitter.add_edge('Tom', 'Linda', {'Weight': 1})
twitter.add_edge('Bart', 'Greg', {'Weight': 2})
twitter.add_edge('Tom', 'Greg', {'Weight': 2})
twitter.add_edge('Peter', 'Lester', {'Weight': 2})
twitter.add_edge('Tom', 'Mike', {'Weight': 1})
twitter.add_edge('Rachel', 'Mike', {'Weight': 1})
twitter.add_edge('Rachel', 'Glenn', {'Weight': 1})
twitter.add_edge('Lester', 'Max', {'Weight': 1})
twitter.add_edge('Matt', 'Peter', {'Weight': 1})

# add relationship
twitter['Rob']['Rory']['relationship'] = 'friend'
twitter['Markus']['Rory']['relationship'] = 'friend'
twitter['Markus']['Rob']['relationship'] = 'spouse'
twitter['Mike']['Rory']['relationship'] = 'friend'
twitter['Mike']['Rob']['relationship'] = 'friend'
twitter['Mike']['Markus']['relationship'] = 'friend'
twitter['Mike']['Linda']['relationship'] = 'spouse'
twitter['Alex']['Rob']['relationship'] = 'friend'
twitter['Alex']['Markus']['relationship'] = 'friend'
twitter['Alex']['Mike']['relationship'] = 'friend'
twitter['Glenn']['Rory']['relationship'] = 'friend'
twitter['Glenn']['Rob']['relationship'] = 'friend'
twitter['Glenn']['Markus']['relationship'] = 'friend'
twitter['Glenn']['Linda']['relationship'] = 'sibling'
twitter['Glenn']['Mike']['relationship'] = 'friend'
twitter['Glenn']['Alex']['relationship'] = 'friend'
twitter['Richard']['Rob']['relationship'] = 'friend'
twitter['Richard']['Linda']['relationship'] = 'friend'
twitter['Richard']['Mike']['relationship'] = 'friend'
twitter['Richard']['Alex']['relationship'] = 'friend'
twitter['Richard']['Glenn']['relationship'] = 'friend'
twitter['Jackie']['Linda']['relationship'] = 'friend'
twitter['Jackie']['Mike']['relationship'] = 'friend'
twitter['Jackie']['Glenn']['relationship'] = 'friend'
twitter['Jackie']['Skye']['relationship'] = 'friend'
twitter['Tom']['Rachel']['relationship'] = 'spouse'
twitter['Rachel']['Bart']['relationship'] = 'friend'
twitter['Tom']['Bart']['relationship'] = 'sibling'
twitter['Jack']['Skye']['relationship'] = 'friend'
twitter['Bart']['Skye']['relationship'] = 'friend'
twitter['Rachel']['Skye']['relationship'] = 'friend'
twitter['Greg']['Bob']['relationship'] = 'friend'
twitter['Peter']['Greg']['relationship'] = 'friend'
twitter['Lester']['Matt']['relationship'] = 'friend'
twitter['Max']['Matt']['relationship'] = 'friend'
twitter['Rachel']['Linda']['relationship'] = 'friend'
twitter['Tom']['Linda']['relationship'] = 'friend'
twitter['Bart']['Greg']['relationship'] = 'sibling'
twitter['Tom']['Greg']['relationship'] = 'sibling'
twitter['Peter']['Lester']['relationship'] = 'generation'
twitter['Tom']['Mike']['relationship'] = 'friend'
twitter['Rachel']['Mike']['relationship'] = 'friend'
twitter['Rachel']['Glenn']['relationship'] = 'friend'
twitter['Lester']['Max']['relationship'] = 'friend'
twitter['Matt']['Peter']['relationship'] = 'friend'

# print nodes
print('\nJust nodes: ', twitter.nodes())
print('\nNodes with data: ', twitter.nodes(data=True))

# print edges
print('\nEdges with data: ', twitter.edges(data=True))

# graph's density and centrality
print('\nDensity of the graph: ', nx.density(twitter))

centrality = sorted(
    alg.centrality.degree_centrality(twitter).items(), 
    key=lambda e: e[1], reverse=True)
print('\nCentrality of nodes: ', centrality)

average_degree = sorted(
    alg.assortativity.average_neighbor_degree(twitter)\
    .items(), key=lambda e: e[1], reverse=True)

print('\nAverage degree: ', average_degree)

print(len(twitter['Glenn']) / 19)

# draw the graph
nx.draw_networkx(twitter)
plt.savefig('../../Data/Chapter8/twitter_networkx.png')

# save graph
nx.write_graphml(twitter, 
    '../../Data/Chapter8/twitter.graphml')