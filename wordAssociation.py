'''
Created by prasanthtootcat

'''

import nltk,graph,collections

wordAssociation = []
location=input("Enter the corpus file location\n")
corpus = open(location, "r")
tokenizedCorpus = nltk.tokenize.word_tokenize(corpus.read())
userInput = input("Enter the sentence to form Word Association Graph\n")
tokenizedInput = nltk.tokenize.word_tokenize(userInput)

inputLen = len(tokenizedInput)
corpusLen = len(tokenizedCorpus)

for i in range(0,inputLen):
	for j in range(0,corpusLen):
		if tokenizedInput[i] == tokenizedCorpus[j] and j+1<corpusLen:
			for k in range(0,inputLen):
				if tokenizedCorpus[j+1] == tokenizedInput[k]:
					if i!=k :
						wordAssociation.append((i,k))

corpusCountDict = collections.Counter(tokenizedCorpus)
graphDict = collections.Counter(wordAssociation)
graph.graphPlotter(tokenizedInput,graphDict,corpusCountDict)