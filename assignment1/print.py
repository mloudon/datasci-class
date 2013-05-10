import urllib
import json

def get_tweets(numpages):
    try:
        response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=%d"%numpages)
    except:
        print "no response"
    
    return json.load(response)

def print_text(tweetjson):
    #print tweetjson[u"id"]
    print tweetjson[u"text"]

for result in get_tweets(10)["results"]:
    print_text(result)