import nltk
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
nltk.download('punkt_tab')

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenize_sentence, all_words):
    pass

a = "See you later?"
a = tokenize(a)
print(a)
