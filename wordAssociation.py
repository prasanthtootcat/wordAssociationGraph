'''
Created by prasanthtootcat

'''

import nltk,graph,collections
from nltk.corpus import stopwords

wordAssociation = []
tokenizedInput = []
tokenizedCorpus = []
stopWords=set(stopwords.words('english'))
location=input("Enter the corpus file location\n")
corpus = open(location, "r")
tokenizedCorpusNotPreprocessed = nltk.tokenize.word_tokenize(corpus.read())
userInput = input("Enter the sentence to form Word Association Graph\n")
tokenizedInputNotPreprocessed = nltk.tokenize.word_tokenize(userInput)

for w in tokenizedCorpusNotPreprocessed:
	wLower = w.lower()
	if wLower not in stopWords:
		tokenizedCorpus.append(wLower);

for w in tokenizedInputNotPreprocessed:
	wLower = w.lower()
	if wLower not in stopWords:
		tokenizedInput.append(wLower);

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
graphDictSortedList = sorted(graphDict,reverse=True)

inputCountDict = collections.Counter(tokenizedInput)

print("\nCount of occurance of each word in corpus corresponding to the input")

for i in inputCountDict:
	print("%s occurs %d times"%(i,corpusCountDict[i]))

graph.graphPlotter(tokenizedInput,graphDict,corpusCountDict,graphDictSortedList)