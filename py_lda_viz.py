import pyLDAvis.gensim as gensimvis
import pyLDAvis
import csv
import logging

from gensim.corpora import Dictionary
from gensim.models import LdaModel

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

tweets = []
with open('data/clear_covid_tweets.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for tweet in reader:
		tweets.append(tweet['text'].split(' '))

dictionary = Dictionary(tweets)
corpus = [dictionary.doc2bow(tweet) for tweet in tweets]
model = LdaModel(corpus=corpus, num_topics=50, id2word=dictionary)

vis_data = gensimvis.prepare(model, corpus, dictionary)
res = pyLDAvis.display(vis_data)
pyLDAvis.show(vis_data)
