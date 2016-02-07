from __future__ import division
import csv
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
		tweets.append(row[0])
		category.append(row[1])
		i+=1

# get a set of all words - attributes
for tweet in tweets:
	all_words.update(nltk.word_tokenize(tweet))

attributes = list(all_words)


# function to calculate entropy
# parameters - dataset, target_attribute
def calc_entropy(target_attribute):
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
	for tweet in range(len(data)):
		if (attr in nltk.word_tokenize(data[tweet])):
			target_has.append(target_attr[(tweet)])
		else:
			target_has_not.append(target_attr[(tweet)])


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
		new_gain = gain(data, attr, target_attribute)
		list_gain.append(new_gain)
		print "in iteration ", i, " of ", total_iter
		print new_gain
		i+=1
	return attributes[list_gain.index(max(list_gain))]


#testing if best_attribute works
#print best_attribute(tweets, attributes, category)


def build_tree(data_set, attributes, target_attr):
	# if all the samples have the same attribute, we return that attribute
	if (target_attr.count('0') == len(target_attr)):
		return '0'
	elif (target_attr.count('1') == len(target_attr)):
		return '1'
	else :
		# we choose the best attribute
		best = best_attribute(data_set, attributes, target_attr)
		tree = {best: {}}
		# we split the dataset based on the best attribute
		subset_has = []
		subset_has_not = []
		target_has = []
		target_has_not = []
		for tweet in range(len(data_set)):
			if (best in nltk.word_tokenize(data[tweet])):
				subset_has.append(data[tweet])
				target_has.append(target_attr[(tweet)])
			else:
				subset_has_not.append(data[tweet])
				target_has_not.append(target_attr[(tweet)])
		# we make two recursive calls
		attributes.remove(best)
		tree[best]['True'] = build_tree(subset_has, attributes, target_has)
		tree[best]['False'] = build_tree(subset_has_not, attributes, target_has_not)
		return tree
build_tree(tweets, attributes, category)
