'''
Created by prasanthtootcat

'''

import networkx as nx
import pylab

def graphPlotter(tokenizedInput,graphDict,corpusCountDict):
	G = nx.Graph()

	for i in graphDict:
		G.add_edge(i[0],i[1])
		num = graphDict[i] / corpusCountDict[tokenizedInput[i[0]]]
		G[i[0]][i[1]]['weight'] = num

	labels = {}
	nodes = []
	toBeDeleted = []
	k=0
	for string in tokenizedInput:
		labels[k] = string
		k+=1

	for i in graphDict:
		if i[0] not in nodes:
			nodes.append(i[0])
		if i[1] not in nodes:
			nodes.append(i[1])

	for n in labels:
		if n not in nodes:
			toBeDeleted.append(n)

	for n in toBeDeleted:
		if n in labels:
			del(labels[n])


	print(labels)

	print("\nCount of word occurances...\n")
	for i in graphDict:
		print("\"%s\" after \"%s\" is %d" %(labels[i[1]],labels[i[0]],graphDict[i]))


	print("\nProbability of word occurances...\n")
	for i in graphDict:
		print("\"%s\" after \"%s\" is %f" %(labels[i[1]],labels[i[0]],graphDict[i] / corpusCountDict[tokenizedInput[i[0]]]))


	edge_labels=dict([((u,v,),round(d['weight'],4))
             for u,v,d in G.edges(data=True)])	


	if bool(edge_labels):
		pos=nx.spring_layout(G)
		pylab.figure("Graph")
		nx.draw(G,pos)
		nx.draw_networkx_labels(G,pos,labels)
		nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
		pylab.show()