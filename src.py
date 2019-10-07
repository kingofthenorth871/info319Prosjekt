
import json
import pandas as pd

with open("tweets.json", encoding='utf-8') as file:
    data = json.load(file)

for x in data:
    freq = pd.Series((x['tweets']).split()).value_counts()[:20]
    freq




print(freq)


