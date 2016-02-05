#group G3 
import csv
import re

tweets = []
newtweets = []
category = []
i=0;

q = re.compile(r'\bRT\b')

with open('dataset_v1.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		tweets.append(row[0])
		category.append(row[1])
		i+=1

	for row in tweets:
		rownew = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",row).split())
		rownewer = ' '.join(re.sub(q," ",rownew).split())
		newtweets.append(rownewer)


with open('dataset_v2.csv', 'w') as fp:
	a = csv.writer(fp, delimiter=',')
	data = zip(newtweets,category)
	a.writerows(data)
