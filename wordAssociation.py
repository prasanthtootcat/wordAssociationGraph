'''
Created by prasanthtootcat

'''

import nltk,graph
corpus = open("/home/prasanthtootcat/input.txt", "r")
tokenizedCorpus = nltk.tokenize.word_tokenize(corpus.read())
userInput = input("Enter the sentence to form Word Association Graph\n")
tokenizedInput = nltk.tokenize.word_tokenize(userInput)

inputLen = len(tokenizedInput)
corpusLen = len(tokenizedCorpus)
count=0

for i in range(0,inputLen):
	for j in range(0,corpusLen):
		if(tokenizedInput[i]==tokenizedCorpus[j]):
			count+=1

print(count)	
graph.graphPlotter()