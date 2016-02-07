#group G3 
import csv
import re

tweets = []
newtweets = []
category = []

hyperlinks =re.compile(r'http\S+')
q = re.compile(r'\bRT\b')
z = re.compile(r'\'')


with open('dataset_v1.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		tweets.append(row[0])
		category.append(row[1])
		

	for row in tweets:
		rowwithnohyperlinks = ' '.join(re.sub(hyperlinks," ",row).split())
		rowwithnoquotes = ' '.join(re.sub(z,"",rowwithnohyperlinks).split())
		rownew = ' '.join(re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|([^0-9A-Za-z \t])"," ",rowwithnoquotes).split())
		rownewer = ' '.join(re.sub(q," ",rownew).split())
		newtweets.append(rownewer)
		

with open('dataset_v2.csv', 'w') as fp:
	a = csv.writer(fp, delimiter=',')
	data = zip(newtweets,category)
	a.writerows(data)
