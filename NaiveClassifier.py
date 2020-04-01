import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import movie_reviews

#gutenberg
gb = nltk.corpus.gutenberg

#poems text
poems = nltk.corpus.gutenberg.words('blake-poems.txt')
text = nltk.Text(poems)

#stopwords
sw = nltk.corpus.stopwords.words()

#poems filtered text
poems_filtered = [w for w in poems if w.lower() not in sw and w.isalnum()]

#freqdist
fd = nltk.FreqDist(poems_filtered)

#trigrams
trigrams = nltk.FreqDist(nltk.trigrams(poems_filtered))


#documents
documents = [ (list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]


import random

random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())

word_features = list(all_words.keys()) [:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

featuresets=[(document_features(d),c) for (d,c) in documents]

print(len(featuresets))


train_set, test_set = featuresets[400:], featuresets[:400]

classifier = nltk.NaiveBayesClassifier.train(train_set)

print(classifier.show_most_informative_features(5))
