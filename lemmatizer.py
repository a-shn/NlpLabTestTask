import re

import pandas
import pymorphy2
import csv
import sys

morph = pymorphy2.MorphAnalyzer()
filename, result = str(sys.argv[1]), str(sys.argv[2])


def lemmatize(text):
	text = re.sub(r'@[^\s]+', '', text)
	words = re.findall(r'\w+', text)
	res = list()
	for word in words:
		p = morph.parse(word)[0]
		res.append(p.normal_form)

	return res


def lemmatizer(filename, result_filename):
	data = pandas.read_csv(filename, compression='gzip')
	tweets = data['text']
	with open(result_filename, 'w', newline='') as csvfile:
		csvfile.write('text\n')
		writer = csv.DictWriter(csvfile, fieldnames=['text'])
		for tweet in tweets:
			lemmatized_tweet = ' '.join(lemmatize(tweet))
			writer.writerow({'text': lemmatized_tweet})


lemmatizer(filename, result)
