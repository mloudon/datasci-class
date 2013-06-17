import numpy as np
from nltk.probability import FreqDist
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import json
from nltk.tokenize import RegexpTokenizer

def train():
    pipeline = Pipeline([('tfidf', TfidfTransformer()),
                         ('chi2', SelectKBest(chi2, k=40)),
                         ('nb', MultinomialNB())])
    classif = SklearnClassifier(pipeline)
    
    
    pos = [FreqDist(i) for i in open('/home/mel/workspace/datascience/assignment5_kaggle/data/useful.txt', 'r').readlines()]
    neg = [FreqDist(i) for i in open('/home/mel/workspace/datascience/assignment5_kaggle/data/not.txt', 'r').readlines()]
    add_label = lambda lst, lab: [(x, lab) for x in lst]
    classif.train(add_label(pos, 'pos') + add_label(neg, 'neg'))
    return classif

def word_feats(words):
    return dict([(word, True) for word in words])

def main():

    review_file = open("/home/mel/workspace/datascience/assignment5_kaggle/data/yelp_test_set/yelp_test_set_review.json")
    lines = review_file.readlines()
    output_file = open('/home/mel/workspace/datascience/assignment5_kaggle/output.csv', 'w+')
    
    tokenizer = RegexpTokenizer(r'\w+')
    clf = train()
    
    for line in lines:
        json_line = json.loads(line)
        encoded_review = json_line["text"].encode('utf-8')
        review_id = json_line["review_id"]
        tokens = tokenizer.tokenize(encoded_review)
        pos_likelihood = clf.prob_classify(word_feats(tokens)).prob('pos')
        print pos_likelihood
        
        if (pos_likelihood < 0.25):
            output_file.write("%s,%d\n" %(review_id,0))
        elif (pos_likelihood < 0.30):
            output_file.write("%s,%d\n" %(review_id,1))
        elif (pos_likelihood < 0.35):
            output_file.write("%s,%d\n" %(review_id,2))
        else:
            output_file.write("%s,%d\n" %(review_id,3))
            
        
if __name__ == '__main__':
    main()