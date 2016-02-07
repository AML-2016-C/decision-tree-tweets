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

# function to calculate entropy 
# parameters - dataset, target_attribute
def calc_entropy(data_set, target_attribute):
	val_freq     = {}
	data_entropy = 0.0

	# Calculate the frequency of each of the values in the target attr
	for record in data:
		if (val_freq.has_key(record[target_attr])):
			val_freq[record[target_attr]] += 1.0
		else:
			val_freq[record[target_attr]]  = 1.0
	#Calculate the entropy of the data for the target attribute
	for freq in val_freq.values():
		data_entropy += (-freq/len(data)) * math.log(freq/len(data), 2) 
	return data_entropy

def gain(data, attr, target_attr):
	"""
	Calculates the information gain (reduction in entropy) that would
	result by splitting the data on the chosen attribute (attr).
	"""
	val_freq       = {}
	subset_entropy = 0.0

	# Calculate the frequency of each of the values in the target attribute
	for record in data:
		if (val_freq.has_key(record[attr])):
		    val_freq[record[attr]] += 1.0
		else:
		    val_freq[record[attr]]  = 1.0

	# Calculate the sum of the entropy for each subset of records weighted
	# by their probability of occuring in the training set.
	for val in val_freq.keys():
		val_prob        = val_freq[val] / sum(val_freq.values())
		data_subset     = [record for record in data if record[attr] == val]
		subset_entropy += val_prob * entropy(data_subset, target_attr)

	# Subtract the entropy of the chosen attribute from the entropy of the
	# whole data set with respect to the target attribute (and return it)
	return (entropy(data, target_attr) - subset_entropy)		

def best_attribute(data, attributes, target_attribute):
	list_gain = []
	for attr in attributes:
		list_gain.append(data, attr, target_attribute)
	return attributes[list_gain.index(max(list_gain))]
		
