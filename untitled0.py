# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:28:46 2019

@author: Tor Aasheim
"""
import codecs
# from collections import defaultdict
# from googletrans import Translator
import re

# opens and saves datasett in string
hyphen_dict = defaultdict(int)
file_in = codecs.open("tweets.csv", "r", "utf-8")
csv = file_in.read()
file_in.close()
# splits the string on new line
tweet = csv.split("\n")
# list for the cleaned tweets
clean = []
# initializing translate api


# counts number of , to remove unwanted instances and adds to list
for x in tweet:
    if x.count(",") > 6:
        clean.append(x)

    # word_list = []
# for x in clean:
#    word = re.split(',|\s',x)
#    word_list.append(word)


# trans_list = []
# for x in word_list:
#    for y in x:
#        translator = Translator()
#        word = translator.detect(y)         
#        if word.lang == "ar":
#            translator.translate(y, src="ar", dest="en") 
#            trans_list.append(y)            
#        else:
#            trans_list.append(y)

count = 0
split = []
while count < len(clean):
    test = clean[count].split(",")
    split.append(test)
    count += 1

check = []
regex = re.compile("^[2][0][1][3-7]\W[0-1][0-9]\W[0-3][0-9][T][0-2][0-9][:][0-9][0-9][:][0-5][0-9]")
for x in split:
    for y in x:
        if re.search(regex, y):
            # print(str(y) + "  " + str(i))
            i = x.index(y) + 1
            check.extend((y, "æøå", x[i]))

i = 0
time_tweet = []
while i < len(check):
    time = check[0:3]
    time_tweet.append(time)
    time_tweet.append("\n")
    del check[0:3]

print(time_tweet[0][2])

# opens the output file and writes the list to file
file_out = codecs.open("clean_tweet.csv", "w", "utf-8")
for x in clean:
    file_out.write(x)

file_out.close()

file_out = codecs.open("split_tweets.csv", "w", "utf-8")
for x in time_tweet:
    file_out.write(str(x))

file_out.close()

# trans = translator.translate(x, src="ar", dest="en")
# print(trans.text)
# print(x)
# translator = Translator()
# print(translator.detect('이 문장은 한글로 쓰여졌습니다.'))
# test = translator.translate("خلافة", src="ar", dest="en")
# print(test.text)
