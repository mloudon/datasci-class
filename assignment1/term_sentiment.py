import sys
import json

scores = {} # initialize an empty dictionary
tweet_sentiment = {}
term_scores = {}

def get_sentiment(tweet):
    score = 0
    for word in tweet.split():
        if word in scores:
            score+=scores[word]
            #print "added %d points for word %s; new score is %d" % (scores[word],word, score)
    
    tweet_sentiment[tweet]=float(score)
        
def get_scores(sent_file):
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items()
    
def score_terms():
    for tweet in tweet_sentiment:
        for word in tweet.split():
            if word in scores:
                term_scores[word]=scores[word]
            else:
                if not word in term_scores:
                    term_scores[word] = 0
                term_scores[word] += tweet_sentiment[tweet] #add the score of the tweet to the score of the word


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
        
    score_terms()
        
    for term in term_scores:
        encoded_term = term.encode('utf-8')
        print "%s %f" %(encoded_term,float(term_scores[term]))
        

if __name__ == '__main__':
    main()
