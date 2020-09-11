import csv
import sys

word_dict = dict()
filename, result = str(sys.argv[1]), str(sys.argv[2])


def delete_less_occurred_words(filename, result_filename):
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
		with open(filename) as csvfile:
			counter.write('text\n')
			reader = csv.DictReader(csvfile)
			writer = csv.DictWriter(counter, fieldnames=['text'])
			for w in reader:
				temp = []
				for word in w['text'].split(' '):
					if word_dict[word] >= 5:
						temp.append(word)
				writer.writerow({'text': ' '.join(temp)})


delete_less_occurred_words(filename, result)
