import csv
from textblob.classifiers import NaiveBayesClassifier

train = []
count_train = 0
count_test = 0

with open('sample_train1.tsv','r') as t:
    trainFileReader = csv.reader(t,delimiter='\t')
    next(trainFileReader)
    for row in trainFileReader:
        train.append([row[2], row[3]])
        count_train += 1
        if count_train % 5 == 0:
        	print(str(count_train) + " examples have been trained!")
        	print(train)
        	print("")
        	del(train[:])
