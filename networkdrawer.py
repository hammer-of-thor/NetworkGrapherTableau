# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

G=nx.Graph()

inputedges = pd.read_csv('edges.csv')
inputnodes = pd.read_csv('nodes.csv')

for i,r in inputnodes.iterrows():
    G.add_node(r['ID'])
    
for i,r in inputedges.iterrows():
    G.add_edge(r['Source'],r['Target'], weight=r['Weight'])
    
pos=nx.spring_layout(G, k=0.19, iterations=20, scale=100)
#pos=nx.shell_layout(G)
#pos=nx.spectral_layout(G)
#pos=nx.random_layout(G)

# networkx ver 2.x swapped the positions of set_node_attributes' name and value arguments
nx.set_node_attributes(G,pos,'pos')

pos[-2] = [100.0, 0.0]
pos[-1] = [0.0, 100.0]

nx.draw(G, pos=pos)
plt.savefig("network_graph.png")
plt.show()

# networkx ver 2.x deprecated method .node
nodesframe = pd.DataFrame(G._node)

throughputframe = nodesframe.transpose()
outputframe = pd.concat([throughputframe['pos'].str[0],throughputframe['pos'].str[1]], axis=1)
outputframe.columns = ['X','Y']

outputframe.to_csv('nodepositions.csv', encoding='utf-16', index_label='ID')
