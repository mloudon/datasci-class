import sys
import json

terms = {}
total_terms = 0

def count_words(tweettext):
    global total_terms
    for word in tweettext.split():
        total_terms +=1
        if word in terms:
            terms[word]+=1
        else:
            terms[word]=1
def main():
    tweet_file = open(sys.argv[1])
    lines = tweet_file.readlines()
    
    for line in lines:
        tweetstream_json_line = json.loads(line)
        
        #check that it's a tweet and not some other live stream object
        if "text" in tweetstream_json_line:
            tweettext = tweetstream_json_line["text"]
            count_words(tweettext)
            
        for term in terms:
            encoded_term = term.encode('utf-8')
            print "%s %f" %(encoded_term,float(terms[term])/total_terms)

if __name__ == '__main__':
    main()
