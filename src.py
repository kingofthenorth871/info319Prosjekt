
import json
import pandas as pd
from collections import Counter


with open("tweets.json", encoding='utf-8') as file:
    data = json.load(file)
#saves all the tweets in a list
tweet = []
for x in data:
    tweet.append(x['tweets'])

#creates a string to hold all the tweets for word count
tweet_string = ''.join(tweet)


#Counts word frequency for each tweet
word_freq = []
for x in tweet_string:
    tokens = tweet_string.split(" ")
    cnt = Counter(tokens)
    freq = cnt.most_common()
    word_freq.append(freq)

print(word_freq)








