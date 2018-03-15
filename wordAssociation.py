'''
Created by prasanthtootcat

'''

import nltk,graph,collections
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
from nltk.tokenize import RegexpTokenizer

wordAssociation = []
tokenizedInput = []
tokenizedCorpus = []
stopWords=set(stopwords.words('english'))
location=input("Enter the corpus file location\n")
corpus = open(location, "r")
punctuationRemovalRegex = RegexpTokenizer(r'\w+')
tokenizedCorpusNotPreprocessed = punctuationRemovalRegex.tokenize(corpus.read())	#punctuations removed & corpus tokenized
userInput = input("Enter the sentence to form Word Association Graph\n")
tokenizedInputNotPreprocessed = punctuationRemovalRegex.tokenize(userInput)			#punctuations removed & userInput tokenized
stemmer = PorterStemmer()

for w in tokenizedCorpusNotPreprocessed:
	wLower = w.lower()
	if wLower not in stopWords:							#Stop words removal from corpus
		wLower = stemmer.stem(wLower)					#Stemming of corpus
		tokenizedCorpus.append(wLower)

for w in tokenizedInputNotPreprocessed:
	wLower = w.lower()
	if wLower not in stopWords:							#Stop words from user input
		wLower = stemmer.stem(wLower)					#Stemming of user input
		tokenizedInput.append(wLower)


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