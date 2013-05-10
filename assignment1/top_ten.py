import sys
import json

hashtagfreqs = {}

def main():
    tweet_file = open(sys.argv[1])
    lines = tweet_file.readlines()
    
    for line in lines:
        tweetstream_json_line = json.loads(line)
        
        if "entities" in tweetstream_json_line:
            entities= tweetstream_json_line["entities"]
            if "hashtags" in entities:
                hashtags = entities["hashtags"]
                for hashtag in hashtags:
                    hashtagtext = hashtag["text"]
                    if hashtagtext in hashtagfreqs:
                        hashtagfreqs[hashtagtext]+=1
                    else:
                        hashtagfreqs[hashtagtext]=1
            
    topten = sorted(hashtagfreqs.iteritems(), key=lambda x:-x[1])[:10]
    for toptag in topten:
        print "%s %s" % (toptag[0], float(toptag[1]))

if __name__ == '__main__':
    main()
