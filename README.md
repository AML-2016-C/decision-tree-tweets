# decision-tree-tweets
An implementation of decision trees for a given dataset of tweets. 
#TODO
1. A function to split the tweets based on an attribute (one list with the tweets that have the word, one list with the tweets that don't) (returns a tuple)
2. A function that chooses the best attribute based on entropy and information gain

#Algorithm
tree = dictionary{}
function build-tree(data-set, attribute-set)
	if (category of all elements in the data-set is the same)
		do nothing, return
	else
		attribute = choose-next-best(data-set, attribute-set)
		split-tuple = split-dataset(data-set, attribute)
		attribute-set.remove(attribute)
		tree = {attribute:{}}
		// for the left child, pass the dataset which have the word
		subtree-1 = build-tree(split-tuple[0], attribute-set)
		// for the right child, pass the dataset that doesn't have the word
		subtree-2 = build-tree(split-tuple[1], attribute-set)
		tree[attribute][true] = subtree-1	
		tree[attribute][false] = subtree-2
		return tree
