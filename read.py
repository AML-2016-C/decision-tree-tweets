from __future__ import division
import csv
import time
import nltk
import math
tweets = []
category = []
all_words = set()
# we use a list to store attributes for convenience
attributes = []
#taking input and preparing
with open('dataset_v2.csv') as f:
	read = csv.reader(f)
	i=0
	for row in read:
		tweets.append(row[0].lower())
		if (row[1]=='1'):
			category.append(row[1])
		else:
			category.append('0')
		i+=1

# get a set of all words - attributes
for tweet in tweets:
	all_words.update(nltk.word_tokenize(tweet))

attributes = list(all_words)


# function to calculate entropy
# parameters - dataset, target_attribute
def calc_entropy(target_attribute):
	start_time = time.time()
	val_freq     = {}
	data_entropy = 0.0
	subset_has = target_attribute.count('1')
	subset_has_not = target_attribute.count('0')
	# Calculate the frequency of each of the values in the target attr
	'''for i in range(len(target_attribute)):
		if (target_attribute[i]=='1'):
			subset_has+=1
		else:
			subset_has_not+=1'''

	if ((subset_has)!=0):
		data_entropy += (-(subset_has)/len(target_attribute)) * math.log((subset_has)/len(target_attribute), 2)

	if ((subset_has_not)!=0):
		data_entropy += (-(subset_has_not)/len(target_attribute)) * math.log((subset_has_not)/len(target_attribute), 2)
	end_time = time.time()
	##print "Entropy took ", end_time - start_time
	return data_entropy

def gain(data, attr, target_attr):
	"""
	Calculates the information gain (reduction in entropy) that would
	result by splitting the data on the chosen attribute (attr).
	"""
	target_has = []
	target_has_not = []
	subset_entropy = 0.0

	# Calculate the frequency of each of the values in the target attribute
	# find the number of tweets that contain the word and ones that don't
	start_time = time.time()
	for tweet in range(len(data)):
		if (attr in data[tweet]):
			target_has.append(target_attr[(tweet)])
		else:
			target_has_not.append(target_attr[(tweet)])
	end_time = time.time()
	##print "splitting took ", end_time - start_time

	# Calculate the sum of the entropy for each subset of records weighted
	# by their probability of occuring in the training set.
	# for things that have the word
	val_prob        = len(target_has)/len(data)
	subset_entropy += val_prob * calc_entropy(target_has)

	val_prob        = len(target_has_not)/len(data)
	subset_entropy += val_prob * calc_entropy(target_has_not)

	# Subtract the entropy of the chosen attribute from the entropy of the
	# whole data set with respect to the target attribute (and return it)
	return (calc_entropy(target_attr) - subset_entropy)

def best_attribute(data, attributes, target_attribute):
	list_gain = []
	i=0
	total_iter = len(attributes)
	for attr in attributes:
		start_time  =time.time()
		new_gain = gain(data, attr, target_attribute)
		list_gain.append(new_gain)
	#	#print "in iteration ", i, " of ", total_iter
		end_time = time.time()
#		#print end_time - start_time
		##print new_gain
		i+=1
	return attributes[list_gain.index(max(list_gain))]


#testing if best_attribute works
##print best_attribute(tweets, attributes, category)

# data_set or data is the tweets
# attributes is the words 
def build_tree(data_set, attributes, target_attr):
	# if all the samples have the same attribute, we return that attribute
	if (target_attr.count('0') == len(target_attr)):
		#print "Stopped here, all 0" 
		return '0'
	elif (target_attr.count('1') == len(target_attr)):
		#print "Stopped here, all 1"
		return '1'
	else :
		# we choose the best attribute
		#print "Num0 - ", target_attr.count('0'), " Num1 - ", target_attr.count('1')
		best = best_attribute(data_set, attributes, target_attr)
                #print "best attribute", best
		tree = {best: {}}
		# we split the dataset based on the best attribute
		subset_has = []
		subset_has_not = []
		target_has = []
		target_has_not = []
		for tweet in range(len(data_set)):
			if (best in nltk.word_tokenize(data_set[tweet])):
				subset_has.append(data_set[tweet])
				target_has.append(target_attr[(tweet)])
			else:
				subset_has_not.append(data_set[tweet])
				target_has_not.append(target_attr[(tweet)])
		# we make two recursive calls
		attributes.remove(best)
		#print "left of ", best
		tree[best]['True'] = build_tree(subset_has, attributes, target_has)
		#print "right of ", best
		tree[best]['False'] = build_tree(subset_has_not, attributes, target_has_not)
		#print "Tree till now is", tree
		return (best, tree)

decision_tree = build_tree(tweets[0:1200], attributes, category[0:1200])
#print decision_tree
#lookup function for prediction
def lookup(tweet):
	value = decision_tree 
	#print "starting lookup"
	key = decision_tree[1].keys()[0]
	#print key
	while (value!='0' and value!='1'):
		#print value[1].keys()[0]
		#print value[1][value[1].keys()[0]]
		key =value[1].keys()[0]
		#print "key is ",key 
		#print "value is ", value
		if (key in tweet.split(' ')):
		
			# we go to the 'true' child
			#print "it was true, going to ", value[1][key.lower()]
			value = value[1][key.lower()]['True']
		else:
			#print "it was false, going to ", value[1][key.lower()]
			value = value[1][key.lower()]['False']
		#print "value is now ", value
		#print "condition ", (value!='0' and value!='1')
	return value 

#print "Doing lookups for all tweets"
correct=0
for index in range(1200,len(tweets)):
	if (lookup(tweets[index])==category[index]):
		correct+=1
print "Moment of truth, number of correct values ", correct
print "Percentage - ", correct/300
	


