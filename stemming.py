import codecs
from collections import Counter
import json
import nltk

nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

nltk.download('stopwords')

# Reads the json file with the data
with open("tweets.json", encoding='utf-8') as file:
    data = json.load(file)
# saves all the tweets in a list
tweet = []
for x in data:
    tweet.append(x['tweets'])

# creates a string to hold all the tweets for word count
tweet_string = ''.join(tweet)
# tokenizes the tweet string and saves them into the word variable
words = word_tokenize(tweet_string)

# stemming
ps = PorterStemmer()
stemTweet = []
for w in words:
    stemTweet.append(ps.stem(w))

# joines the stemmed words
tweet_string2 = ' '.join(stemTweet)

# Stopwords
stop_words = set(stopwords.words("english"))
words2 = word_tokenize(tweet_string2)
filtered_sentence = [w for w in words2 if not w in stop_words]

# joines stemmed and stopword
tweet_string3 = ' '.join(filtered_sentence)

# Remove special characters
tokenizer = RegexpTokenizer(r'\w+')
spec_char = tokenizer.tokenize(tweet_string3)

# joines stemmed, stopwords and removed special characters
tweet_string4 = ' '.join(spec_char).lower()

# Counts word frequency for each word
word_freq = []
tokens = tweet_string4.split(" ")
cnt = Counter(tokens)
freq = cnt.most_common()
word_freq.append(freq)

# Writes to file
file_out = codecs.open("word_frq.txt", "w", "utf-8")
file_out.write(str(word_freq))
file_out.close()

file_out = codecs.open("cloud.txt", "w", "utf-8")
file_out.write(str(tweet_string3))
file_out.close()
