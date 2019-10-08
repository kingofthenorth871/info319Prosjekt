## fra hit

import codecs
from collections import Counter

import json
import pandas as pd

import nltk
nltk.download('punkt')

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')

ps = PorterStemmer()


with open("tweets.json", encoding='utf-8') as file:
    data = json.load(file)
#saves all the tweets in a list
tweet = []
for x in data:
    tweet.append(x['tweets'])

##fra hit stemming og stopwords

#creates a string to hold all the tweets for word count
tweet_string = ''.join(tweet)

words = word_tokenize(tweet_string)

stemTweet = []
for w in words:
    stemTweet.append(ps.stem(w))

tweet_string2 = ' '.join(stemTweet)

stop_words = set(stopwords.words("english"))

words2 = word_tokenize(tweet_string2)
filtered_sentence = [w for w in words2 if not w in stop_words]

tweet_string3 = ' '.join(filtered_sentence)

##til hit stemming og stopwords

#Counts word frequency for each tweet
word_freq = []
tokens = tweet_string2.split(" ")
cnt = Counter(tokens)
freq = cnt.most_common()
word_freq.append(freq)


print(word_freq)
file_out = codecs.open("word_frq.txt", "w", "utf-8")
file_out.write(str(word_freq))
file_out.close()