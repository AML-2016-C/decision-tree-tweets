import csv
import nltk

tweets = []
category = []
occurence_list_1= dict() 
occurence_list_2= dict() 
occurence_list_3= dict() 

with open('dataset_v2.csv') as f:
	read = csv.reader(f)
	i=0
	for row in read:
		tweets.append(row[0])
		category.append(row[1])
		i+=1

def build_occurrence_list():
	for i in range(len(tweets)):
		words = nltk.word_tokenize(tweets[i])
		for blub in words:
			if (category[i]=='1'):
				if (occurence_list_1.__contains__(blub)):
					occurence_list_1[blub]+=1
				else :
					occurence_list_1[blub]=1
			if (category[i]=='2'):
				if (occurence_list_2.__contains__(blub)):
					occurence_list_2[blub]+=1
				else :
					occurence_list_2[blub]=1
			if (category[i]=='3'):
				if (occurence_list_3.__contains__(blub)):
					occurence_list_3[blub]+=1
				else :
					occurence_list_3[blub]=1
	return 
		
build_occurrence_list()
