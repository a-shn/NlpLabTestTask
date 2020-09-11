import csv
import sys

filename, result = str(sys.argv[1]), str(sys.argv[2])
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


def stop_words_deleter(filename, result_filename):
	with open(result_filename, 'w', newline='') as ws_csvfile:
		with open(filename, newline='') as lemmatized_csvfile:
			reader = csv.DictReader(lemmatized_csvfile)
			writer = csv.DictWriter(ws_csvfile, fieldnames=['text'])
			for w in reader:
				if w['text'] != '':
					text = delete_stopwords(w['text'])
					writer.writerow({'text': text})


stop_words_deleter(filename, result)
