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
tagged_sentences = [nltk.pos_tag(w) for w in tokenized]

# extract named entities -- naive approach
named_entities = []

for sentence in tagged_sentences:
    for word in sentence:
        if word[1] == 'NNP' or word[1] == 'NNPS':
            named_entities.append(word)

named_entities = list(set(named_entities))

print('Named entities -- simplistic approach:')
print(named_entities)

# extract names entities -- regular expressions approach
named_entities = []
tagged = []

pattern = '''
    ENT: {<DT|PP\$>?(<NNP|NNPS>)+}
'''

# use regular expressions parser
tokenizer = nltk.RegexpParser(pattern)

for sent in tagged_sentences:
    tagged.append(tokenizer.parse(sent))

for sentence in tagged:
    for pos in sentence:
        if type(pos) == nltk.tree.Tree:
            named_entities.append(pos)

named_entities = list(set([tuple(e) for e in named_entities]))

print('\nNamed entities using regular expressions:')