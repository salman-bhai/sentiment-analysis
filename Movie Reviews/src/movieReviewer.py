import csv
from textblob.classifiers import NaiveBayesClassifier

train = []
count_train = 0
count_test = 0

with open('train.tsv','r') as t:
    trainFileReader = csv.reader(t,delimiter='\t')
    next(trainFileReader)
    for row in trainFileReader:
        train.append([row[2], row[3]])
        count_train += 1
        if count_train % 100 == 0:
        	print(str(count_train) + " examples have been appended!")
        	
    cl = NaiveBayesClassifier(train)
        # if count_train % 200 == 0:
        #     del(train[:])
			
with open('test.tsv', 'r') as test:
	with open('submission.csv', 'w') as subm:
 	
 		testFileReader = csv.reader(test,delimiter='\t')
 		next(testFileReader)

 		submissionFileWriter = csv.writer(subm)
 		submissionFileWriter.writerow(["PhraseId","Sentiment"])

 		for row in testFileReader:
 			submissionFileWriter.writerow([row[0], cl.classify(row[2])])
 			count_test += 1
 			if count_test % 100 == 0:
 				print(str(count_test) + " examples have been classified!")

