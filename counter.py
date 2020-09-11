import csv
import sys

word_dict = dict()
filename, result = str(sys.argv[1]), str(sys.argv[2])


def count_words_occurrence(filename, result_filename):
	with open(filename, newline='') as data:
		reader = csv.DictReader(data)
		for w in reader:
			if w['text'] != '':
				for word in w['text'].split(' '):
					if word in word_dict.keys():
						word_dict[word] += 1
					else:
						word_dict[word] = 1

	with open(result_filename, 'w', newline='') as counter:
		counter.write('word,occurrences\n')
		writer = csv.DictWriter(counter, fieldnames=['word', 'occurrences'])
		for w in sorted(word_dict, key=word_dict.get, reverse=True):
			if word_dict[w] < 5:
				continue
			writer.writerow({'word': w, 'occurrences': word_dict[w]})


count_words_occurrence(filename, result)
