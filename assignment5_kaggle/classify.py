import json
from nltk.corpus.reader import CategorizedPlaintextCorpusReader
from nltk import FreqDist
from nltk.classify.naivebayes import NaiveBayesClassifier
from nltk import word_tokenize

def make_training_data(rdr):
    for c in rdr.categories():
        for f in rdr.fileids(c):
            print "freqdist for %s" % f
            freq = FreqDist(rdr.words(fileids=[f]))
            print freq
            yield freq, c

def word_feats(words):
    return dict([(word, True) for word in words])


def main():
    rdr = CategorizedPlaintextCorpusReader('/home/mel/workspace/datascience/assignment5_kaggle/data/', r'.*\.txt', cat_pattern=r'(.*)\.txt')
    clf = NaiveBayesClassifier.train(list(make_training_data(rdr)))
    clf.show_most_informative_features(10)
    
    review_file = open("/home/mel/workspace/datascience/assignment5_kaggle/data/yelp_test_set/yelp_test_set_review.json")
    lines = review_file.readlines()
    output_file = open('/home/mel/workspace/datascience/assignment5_kaggle/output.csv', 'w+')
    
    for word in ('good', 'service'):
        print('probability {w!r} is useful: {p:.2%}'.format(
                                                              w = word, p = clf.prob_classify({word : True}).prob('useful')))
    


if __name__ == '__main__':
    main()
