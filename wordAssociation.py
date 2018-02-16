import nltk
corpus = open("/home/prasanthtootcat/input.txt", "r")
#inputfile = corpus.read()
tokenizedCorpus = nltk.tokenize.word_tokenize(corpus.read())
userInput = input("Enter the sentence to form Word Association Graph\n")
tokenizedInput = nltk.tokenize.word_tokenize(userInput)
print(tokenizedInput)