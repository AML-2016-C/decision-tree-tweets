import csv
import nltk

tweets = []
category = []
occurence_list_1= dict() 
occurence_list_2= dict() 
occurence_list_3= dict() 
reverse_dict_1 = dict()
reverse_dict_2 = dict()
reverse_dict_3 = dict()

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
		#print words
		#print category[i]
		for blub in words:
			#print "category is ", category[i]
			if (category[i]=='1'):
				#print "In one"
				if (occurence_list_1.__contains__(blub)):
					occurence_list_1[blub]+=1
				else :
					occurence_list_1[blub]=1


			if (category[i]=='2'):
				#print "In two"
				if (occurence_list_2.__contains__(blub)):
					occurence_list_2[blub]+=1
				else :
					occurence_list_2[blub]=1
			if (category[i]=='3'):
				#print "In three"
				if (occurence_list_3.__contains__(blub)):
					occurence_list_3[blub]+=1
				else :
					occurence_list_3[blub]=1
	#print occurence_list_1
	#print occurence_list_2
	#print occurence_list_3
	for blub in occurence_list_1.keys():
		# reverse dictionary
		if (reverse_dict_1.__contains__(occurence_list_1[blub])):
			reverse_dict_1[occurence_list_1[blub]].append(blub)
		else:
			reverse_dict_1[occurence_list_1[blub]] = [blub]
	for blub in occurence_list_2.keys():
		# reverse dictionary
		if (reverse_dict_2.__contains__(occurence_list_2[blub])):
			reverse_dict_2[occurence_list_2[blub]].append(blub)
		else:
			reverse_dict_2[occurence_list_2[blub]] = [blub]
	for blub in occurence_list_3.keys():
		# reverse dictionary
		if (reverse_dict_3.__contains__(occurence_list_3[blub])):
			reverse_dict_3[occurence_list_3[blub]].append(blub)
		else:
			reverse_dict_3[occurence_list_3[blub]] = [blub]

	count = 0
	print "Dictionary one"
	for i in sorted(reverse_dict_1, reverse=True):
		print i, reverse_dict_1[i]
		#if (count==5):
		#	break
		count+=1
	
	count = 0
	print "Dictionary two "
	for i in sorted(reverse_dict_2, reverse=True):
		print i, reverse_dict_2[i]
		#if (count==5):
		#	break
		count+=1
	count = 0
	print "Dictionary three"
	for i in sorted(reverse_dict_3, reverse=True):
		print i, reverse_dict_3[i]
		#if (count==5):
		#	break
		count+=1
	return 
		
build_occurrence_list()
#print tweets
#print category
