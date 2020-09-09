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

with open('data/words_occurrences.csv', 'w', newline='') as counter:
	writer = csv.DictWriter(counter, fieldnames=['word', 'occurrences'])
	for w in sorted(word_dict, key=word_dict.get, reverse=True):
		if word_dict[w] < 5:
			continue
		writer.writerow({'word': w, 'occurrences': word_dict[w]})
