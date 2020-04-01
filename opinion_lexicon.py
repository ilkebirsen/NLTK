import nltk
from nltk.corpus import opinion_lexicon
nltk.download('opinion_lexicon')

negatives = opinion_lexicon.negative()[:10]
positives = opinion_lexicon.positive()[:10]

print("If you find some negative words, here you are: %s" % negatives)
print("But let us try to see the positive side of life! Described with these words: %s" % positives)
