import nltk
from nltk.corpus import opinion_lexicon

negative_words = list(opinion_lexicon.negative())
positive_words = list(opinion_lexicon.positive())

choice = ""

while choice != "exit":
    choice = input("Please enter a word = ")
    for word in {choice}:
        if word in negative_words:
            print("That's a negative one")
        elif word in positive_words:
            print("That's a positive one")
        elif word == "exit":
            choice = "exit"
        else:
            print("Not in the dictionary")
