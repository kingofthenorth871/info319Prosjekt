import json
import pandas as pd
import codecs
from collections import Counter

#reads the file
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
tokens = tweet_string.split(" ")
cnt = Counter(tokens)
freq = cnt.most_common()
word_freq.append(freq)



file_out = codecs.open("word_frq.txt", "w", "utf-8")
file_out.write(str(word_freq))
file_out.close()







