'''
Created by prasanthtootcat

'''

import networkx as nx
import pylab

def graphPlotter():
	G = nx.Graph()
	G.add_edge(1, 2, weight=3)
	G.add_edge(2, 3, weight=5)
	G.add_edge(1,3, weight=20)
	pos=nx.spring_layout(G)
	pylab.figure(2)
	nx.draw(G,pos)
	nx.draw_networkx_labels(G,pos)
	edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])
	nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
	pylab.show()