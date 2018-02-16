'''
Created by prasanthtootcat

'''

import networkx as nx
import pylab

def graphPlotter(tokenizedInput,graphDict):
	G = nx.Graph()
	print(graphDict)
	for i in graphDict:
		G.add_edge(i[0],i[1])
		G[i[0]][i[1]]['weight'] = graphDict[i]
	labels={}
	k=0
	for str in tokenizedInput:
		labels[k]=str
		k+=1
	pos=nx.spring_layout(G)
	pylab.figure(2)
	nx.draw(G,pos)
	nx.draw_networkx_labels(G,pos,labels)
	nx.draw_networkx_edge_labels(G,pos,edge_labels=graphDict)
	pylab.show()