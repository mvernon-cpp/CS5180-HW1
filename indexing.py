#-------------------------------------------------------------------------
# AUTHOR: Moina Vernon
# FILENAME: indexing.py
# SPECIFICATION: Program reads the file collection.csv and output the tf-idf document-term matrix following the same requirements defined in question 7
# FOR: CS 5180 - Assignment #1
# TIME SPENT: ~3hr
#-----------------------------------------------------------*/

#Importing some Python libraries
import csv
import math

# Helper methods
def removeStopWords(words, stopWords):
    for word in words:
        if word in stopWords:
            words.remove(word)
    return words

def stemming(words, stemming):
    for word in words:
        if word in stemming:
            stem = stemming.get(word)
            words = [w.replace(word, stem) for w in words]
    return words

def termCount(document):
    freq = {}
    for word in document:
      if (word in freq):
          freq[word] += 1
      else:
          freq[word] = 1
    return freq
    # for key, value in freq.items():
    #     print("%s : %d" % (key, value))

def ranking(word, termCounts):
    print('='*50)
    print('ranking word', word)
    numOfDocuments = 3
    index = 0

    #Calculating tf
    tf = []
    df = 0
    while index < numOfDocuments:
      totalCountOfDocument = sum(termCounts[index].values())

      termCount = termCounts[index].get(word)
      tc = int(0 if termCount is None else termCount)

      tf.append( tc / totalCountOfDocument)

      #Calculating df
      keysList = list(termCounts[index].keys())
      if word in keysList:
          df+= 1
      index += 1
    print('tf ', tf)
    print ('df ', df)

    #Calculating idf
    x=numOfDocuments / df
    idf = math.log10(x)
    print('idf ', idf)
    
    #Calculating tf-idf
    tfidf = []
    for num in tf:
        tfidf.append( format(num * idf, ".4f"))
    print('tf-idf ', tfidf)
    
    return tfidf


if __name__ == "__main__": 

  documents = []

  #Reading the data in a csv file
  with open('collection.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
          if i > 0:  # skipping the header
              documents.append (row[0])

  print('Documents: ', documents)

  #Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
  #--> add your Python code here
  stopWords = {"I","She","They","her","their","and"}

  #Conducting stemming. Hint: use a dictionary to map word variations to their stem.
  #--> add your Python code here
  stemSet = {"loves":"love",
              "cats":"cat",
              "dogs":"dog"}

  d=[]
  for term in documents:
      words = term.split(' ')
      words = removeStopWords(words,stopWords)
      # print('Stopword removal: ', words)
      words = stemming(words, stemSet)
      # print('Stemming: ', words)

      d.append(words)
  print('Documents after stopword removal & stemming: ', d)

  #Identifying the index terms.
  #--> add your Python code here
  termCounts = []
  termCounts.append(termCount(d[0]))
  termCounts.append(termCount(d[1]))
  termCounts.append(termCount(d[2]))
  print('\nTerm counts: ', termCounts)

  # place the terms in the matrix following the sequence of their occurrences in the documents
  terms = ['love', 'cat', 'dog']

  #Building the document-term matrix by using the tf-idf weights.
  #--> add your Python code here
  docTermMatrix = []
  for term in terms:
    docTermMatrix.append(ranking(term, termCounts))

  #Printing the document-term matrix.
  #--> add your Python code here
  print('='*50)
  print('\nDocument Term Matrix')
  index= 0
  print('\t', terms)
  while index < 3:
    print('d',index+1,'\t', docTermMatrix[0][index],docTermMatrix[1][index],docTermMatrix[2][index])

    # print(terms[index], '\n', docTermMatrix[index])
    index += 1