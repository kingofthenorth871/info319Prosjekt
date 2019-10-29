from pyspark import SparkConf, SparkContext
import nltk
import json
import codecs

#sc = SparkContext(master="local", appName="SvmTest")
with open("cloud.txt", encoding='utf-8') as file:
    data = file.read()

tweet = []
for x in data:
    tweet.append(x)

posTweet = []
for x in tweet:
    token = nltk.word_tokenize(str(x))
    pos = nltk.pos_tag(token)
    posTweet.append(pos)

file_out = codecs.open("posTweet.txt", "w", "utf-8")
file_out.write(str(posTweet))
file_out.close()




