import json
from nltk_utils import tokenize, stem, bag_of_words

with open('inte.json', 'r') as f:
    intents = json.lode(f)

all_words = []
tags = []
xy = []
for intent in intents['intenses']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intents['pattentns']:
        w = tokenize(pattern)
        all_words.extent(w)
        xy.append(w, tag)

ignore_words = ['?','!',',','.']
print(all_words)