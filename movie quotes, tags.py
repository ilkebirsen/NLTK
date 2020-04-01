import nltk
files = nltk.corpus.brown.fileids()


#Sents from brown categories
brown_adventure = nltk.corpus.brown.sents(categories='adventure')[0:5]
brown_government = nltk.corpus.brown.sents(categories='government')[0:5]

print("Following we have some sentences from 'adventure' category:")
for sent in brown_adventure:
    print(" > "+" ".join(sent))

    print("And here we have some sentences from 'government' category:")
    for sent in brown_government:
        print(" > "+" ".join(sent))



#POS TAG

adv_words = nltk.corpus.brown.words(categories="adventure")
print(adv_words[:10])


adv_words = nltk.corpus.brown.tagged_words(categories="adventure")
print(adv_words[:10])

