import csv

stopwords = []
with open('data/stopwords-ru.txt', newline='') as stopwords_file:
	for line in stopwords_file:
		stopwords.append(line[0:-1])


def delete_stopwords(text):
	old_array = text.split(' ')
	new_array = []
	for word in old_array:
		if word in stopwords:
			continue
		new_array.append(word)
	return ' '.join(new_array)


with open('data/clear_covid_tweets.csv', 'w', newline='') as clear_csvfile:
	with open('data/lemmatized_covid_tweets.csv', newline='') as lemmatized_csvfile:
		reader = csv.DictReader(lemmatized_csvfile)
		writer = csv.DictWriter(clear_csvfile, fieldnames=['id', 'date', 'text'])
		for w in reader:
			if w['text'] != '':
				tweet_id = w['id']
				date = w['date']
				text = delete_stopwords(w['text'])
				writer.writerow({'id': tweet_id, 'date': date, 'text': text})
