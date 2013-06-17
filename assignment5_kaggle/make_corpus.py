import json
from nltk import word_tokenize
from nltk import corpus
from nltk.tokenize import RegexpTokenizer

def main():
    review_file = open("/home/mel/workspace/datascience/assignment5_kaggle/data/yelp_training_set/yelp_training_set_review.json")
    lines = review_file.readlines()
    
    useful_file = open('/home/mel/workspace/datascience/assignment5_kaggle/data/useful.txt', 'w+')
    not_useful_file = open('/home/mel/workspace/datascience/assignment5_kaggle/data/not.txt', 'w+')
    
    tokenizer = RegexpTokenizer(r'\w+')
    
    for line in lines:
        json_line = json.loads(line)
        votes = json_line["votes"]["useful"]
        text = json_line["text"].encode("UTF-8").lower()
        trimmed = list(set(tokenizer.tokenize(text)) - set(corpus.stopwords.words('english')))
        if votes >= 3:
            useful_file.write(" ".join(trimmed))
            useful_file.write("\n")
        elif votes == 0:
            not_useful_file.write(" ".join(trimmed))
            not_useful_file.write("\n")


if __name__ == '__main__':
    main()
