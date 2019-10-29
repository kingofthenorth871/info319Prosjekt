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


token = nltk.word_tokenize(data)
pos = nltk.pos_tag(token)



file_out = codecs.open("posTweet.txt", "w", "utf-8")
file_out.write(str(pos))
file_out.close()




