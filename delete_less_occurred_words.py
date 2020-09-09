import csv

word_dict = dict()

with open('data/clear_covid_tweets.csv', newline='') as data:
	reader = csv.DictReader(data)
	for w in reader:
		if w['text'] != '':
			for word in w['text'].split(' '):
				if word in word_dict.keys():
					word_dict[word] += 1
				else:
					word_dict[word] = 1

with open('data/clear_and_covid_tweets.csv', 'w', newline='') as counter:
	with open('data/clear_covid_tweets.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		writer = csv.DictWriter(counter, fieldnames=['id', 'date', 'text'])
		for w in reader:
			temp = []
			for word in w['text'].split(' '):
				if word_dict[word] >= 5:
					temp.append(word)
			writer.writerow({'id': w['id'], 'date': w['date'], 'text': ' '.join(temp)})
