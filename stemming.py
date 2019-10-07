## fra hit

import json
import pandas as pd

import nltk
nltk.download('punkt')

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythoned", "Pythonly"]

## for w in example_words:
## print(ps.stem(w))

new_text = "It is very important to be pythonly while you are pythoning with python. All Pythoners have Pythoned"

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))


with open("tweets.json", encoding='utf-8') as file:
    data = json.load(file)

for x in data:
    freq = pd.Series((x['tweets']).split()).value_counts()[:20]
    freq = pd.Series((x['tweets']).split()).value_counts()[:20]
    freq

## til hit