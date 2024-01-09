""" from sklearn.feature_extraction.text import CountVectorizer

vectorizer=CountVectorizer()
data_corpus=["python is the best language for the data science. I love the python language."]

vocabulary=vectorizer.fit(data_corpus)
X= vectorizer.transform(data_corpus)

print(X.toarray())
print(vocabulary.get_feature_names_out()) """

import nltk
import gensim
from nltk.corpus import abc


model= gensim.models.Word2Vec(abc.sents())
X= list(model.wv.key_to_index)
data=model.wv.most_similar('science')
print(data)