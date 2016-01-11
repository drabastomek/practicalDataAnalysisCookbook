import nltk
import re

def preprocess_data(text):
    global sentences, tokenized
    tokenizer = nltk.RegexpTokenizer(r'\w+')

    sentences =  nltk.sent_tokenize(text)
    tokenized = [tokenizer.tokenize(s) for s in sentences]

# import the data
guns_laws = '../../Data/Chapter9/ST_gunLaws.txt'

with open(guns_laws, 'r') as f:
    article = f.read()

# chunk into sentences and tokenize
sentences = []
tokenized = []
words = []

preprocess_data(article)

# part-of-speech tagging
tagged_sentences = [nltk.pos_tag(s) for s in tokenized]

# extract named entities -- the Named Entity Chunker
ne = nltk.ne_chunk_sents(tagged_sentences)

# get a distinct list
named_entities = []

for s in ne:
    for ne in s:
        if type(ne) == nltk.tree.Tree:
            named_entities.append((ne.label(), tuple(ne)))
        
named_entities = list(set(named_entities))
named_entities = sorted(named_entities)

# and print out the list
for t, ne in named_entities:
    print(t, ne)
