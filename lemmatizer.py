import pymorphy2
import csv
import time

morph = pymorphy2.MorphAnalyzer()

def lemmatize(text):
	words = text.split()
	res = list()
	for word in words:
		p = morph.parse(word)[0]
		res.append(p.normal_form)

	return res


with open('data/covid_tweets.csv', newline='') as csvfile:
	with open('data/lemmatized_covid_tweets.csv', 'w', newline='') as lemmatized_csvfile:
		reader = csv.DictReader(csvfile)
		writer = csv.DictWriter(lemmatized_csvfile, fieldnames=['id', 'date', 'text'])
		for w in reader:
			if w['text'] != '':
				tweet_id = w['id']
				date = w['date']
				text = ' '.join(lemmatize(w['text']))
				writer.writerow({'id': tweet_id, 'date': date, 'text': text})
