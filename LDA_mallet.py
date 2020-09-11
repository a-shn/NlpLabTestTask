import logging
import csv
import sys
from gensim.models.wrappers import LdaMallet
from gensim.corpora import Dictionary

filename = str(sys.argv[1])


def lda(filename):
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	path_to_mallet_binary = "/home/xiu-xiu/Mallet/bin/mallet"

	tweets = []
	with open(filename, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for tweet in reader:
			tweets.append(tweet['text'].split(' '))

	dictionary = Dictionary(tweets)
	corpus = [dictionary.doc2bow(tweet) for tweet in tweets]

	for num_topics in [20, 30, 50]:
		lines = []
		model = LdaMallet(path_to_mallet_binary, corpus=corpus, num_topics=num_topics, id2word=dictionary)
		with open('lda' + str(num_topics) + '.txt', 'w') as result:
			for topic in range(num_topics):
				for word in model.show_topic(topic, topn=20):
					result.write(word[0] + ' ')
				result.write('\n')


lda(filename)
