import sys
import json

states = ["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","AS","GU","MP","PR","VI"]
state_scores = dict.fromkeys(states,0) # initialize an empty dictionary
scores = {}

def get_sentiment(tweet):
    score = 0
    for word in tweet.split():
        if word in scores:
            score=score+scores[word]
    return score
            
def get_state(placejson):
    if placejson["country_code"]==u"US":
        split_place = placejson["full_name"].split(", ")
        if len(split_place)>1 and split_place[1] in states:
            return split_place[1]
        else:
            return None           
        
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
    
    tweets_with_states = 0
    for line in lines:
        tweetstream_json_line = json.loads(line)
        
        if (("text" in tweetstream_json_line) and ("place" in tweetstream_json_line)):
            place = tweetstream_json_line["place"]
            if place:
                usstate=get_state(place)
                if usstate:
                    tweets_with_states+=1
                    text = tweetstream_json_line["text"]
                    state_scores[usstate]+=get_sentiment(text)
                    
    print max(state_scores,key=state_scores.get)
    print tweets_with_states

if __name__ == '__main__':
    main()
