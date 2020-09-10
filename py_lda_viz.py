import pyLDAvis.gensim as gensimvis
import pyLDAvis
import gensim
import csv
import logging

from gensim.corpora import Dictionary
from gensim.models.wrappers import LdaMallet

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
path_to_mallet_binary = "/home/xiu-xiu/Mallet/bin/mallet"

tweets = []
with open('data/clear_covid_tweets.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for tweet in reader:
		tweets.append(tweet['text'].split(' '))

dictionary = Dictionary(tweets)
corpus = [dictionary.doc2bow(tweet) for tweet in tweets]
model = gensim.models.wrappers.ldamallet.malletmodel2ldamodel(
	LdaMallet(path_to_mallet_binary, corpus=corpus, num_topics=50, id2word=dictionary))

vis_data = gensimvis.prepare(model, corpus, dictionary)
pyLDAvis.save_html(vis_data, 'lda.html')
