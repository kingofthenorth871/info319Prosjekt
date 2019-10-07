import json
import pandas as pd
from collections import Counter


with open("tweets.json", encoding='utf-8') as file:
    data = json.load(file)

#Counts word frequency for each tweet
word_freq = []
for x in data:
    tokens = x['tweets'].split(" ")
    cnt = Counter(tokens)
    freq = cnt.most_common()
    word_freq.append(freq)


print(word_freq[0][0][1])

