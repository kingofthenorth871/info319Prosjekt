import json

with open("tweets.json", encoding='utf-8') as file:
    data = json.load(file)
    for x in data:
        print('Name: ' + x['name'])
        print('Username: ' + x['username'])
        print('Description: ' + x['description'])
        print('Location: ' + x['location'])
        print('Followers: ' + str(x['followers']))
        print('NumberStatuses: ' + str(x['numberstatuses']))
        print('Time: ' + x['time'])
        print('Tweets: ' + x['tweets'])



