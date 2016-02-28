# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import nltk
import nltk.sentiment as sent
import json

@hlp.timeit
def classify_movies(train, sentim_analyzer):
    '''
        Method to estimate a Naive Bayes classifier
        to classify movies based on their reviews
    '''
    nb_classifier = nltk.classify.NaiveBayesClassifier.train
    classifier = sentim_analyzer.train(nb_classifier, train)

    return classifier

@hlp.timeit
def evaluate_classifier(test, sentim_analyzer):
    '''
        Method to estimate a Naive Bayes classifier
        to classify movies based on their reviews
    '''
    for key, value in sorted(sentim_analyzer.evaluate(test).items()):
        print('{0}: {1}'.format(key, value))

# read in the files
f_training = '../../Data/Chapter09/movie_reviews_train.json'
f_testing  = '../../Data/Chapter09/movie_reviews_test.json'

with open(f_training, 'r') as f:
    read = f.read()
    train = json.loads(read)

with open(f_testing, 'r') as f:
    read = f.read()
    test = json.loads(read)

# tokenize the words
tokenizer = nltk.tokenize.TreebankWordTokenizer()

train = [(tokenizer.tokenize(r['review']), r['sentiment']) 
    for r in train]

test  = [(tokenizer.tokenize(r['review']), r['sentiment']) 
    for r in test]

# analyze the sentiment of reviews
sentim_analyzer = sent.SentimentAnalyzer()
all_words_neg_flagged = sentim_analyzer.all_words(
    [sent.util.mark_negation(doc) for doc in train])

# get most frequent words
unigram_feats = sentim_analyzer.unigram_word_feats(
    all_words_neg_flagged, min_freq=4)

# add feature extractor
sentim_analyzer.add_feat_extractor(
    sent.util.extract_unigram_feats, unigrams=unigram_feats)

# and create the training and testing using the newly created
# features
train = sentim_analyzer.apply_features(train)
test  = sentim_analyzer.apply_features(test)

# what is left is to classify the movies and then evaluate
# the performance of the classifier
classify_movies(train, sentim_analyzer)
evaluate_classifier(test, sentim_analyzer)
