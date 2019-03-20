import json


with open('tweets.json', 'r') as f:
    json_data = f.read()

data = json.loads(json_data)

for tweet in data:

    print("Full Text", tweet["full_text"])
    print("Time of Creation", tweet["created_at"])
    print("No. of likes", tweet["favorite_count"])    
    print("No. of retweet", tweet["retweet_count"])

    try:
        print("No. of images in tweet", len(tweet["entities"]["media"]))
    except KeyError:
        print("None")
    
    print()
