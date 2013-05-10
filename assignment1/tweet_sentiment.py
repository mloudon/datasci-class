import sys
import json

scores = {} # initialize an empty dictionary

def get_sentiment(tweet):
    score = 0
    for word in tweet.split():
        if word in scores:
            score=score+scores[word]
            #print "added %d points for word %s; new score is %d" % (scores[word],word, score)
    
    print float(score)
        
def get_scores(sent_file):
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items()

def main():
    sent_file = open(sys.argv[1])
    get_scores(sent_file)
    
    tweet_file = open(sys.argv[2])
    lines = tweet_file.readlines()
    
    for line in lines:
        tweetstream_json_line = json.loads(line)
        
        #check that it's a tweet and not some other live stream object
        if "text" in tweetstream_json_line:
            tweet= tweetstream_json_line["text"]
            #print tweet
            get_sentiment(tweet)

if __name__ == '__main__':
    main()
