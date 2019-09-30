# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:28:46 2019

@author: Tor Aasheim
"""
import codecs

# from googletrans import Translator
# import re
# opens and saves datasett in string
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
while x in clean:
    test = clean[count].split(",")
    split.append(test)
    count += 1

# opens the output file and writes the list to file
file_out = codecs.open("clean_tweet.csv", "w", "utf-8")
for x in clean:
    file_out.write(x)

file_out.close()

print("hei")

# trans = translator.translate(x, src="ar", dest="en")
# print(trans.text)
# print(x)
# translator = Translator()
# print(translator.detect('이 문장은 한글로 쓰여졌습니다.'))
# test = translator.translate("خلافة", src="ar", dest="en")
# print(test.text)