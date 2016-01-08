import nltk
import re
import numpy as np
import matplotlib.pyplot as plt

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

preprocess_data(article)

# part-of-speech tagging
tagged_sentences = [nltk.pos_tag(w) for w in tokenized]

# extract names entities -- regular expressions approach
tagged = []

pattern = '''
    ENT: {<DT|PP\$>?(<NNP|NNPS>)+}
'''

tokenizer = nltk.RegexpParser(pattern)

for sent in tagged_sentences:
    tagged.append(tokenizer.parse(sent))

# keep named entities together
words = []
lemmatizer = nltk.WordNetLemmatizer()

for sentence in tagged:
    for pos in sentence:
        if type(pos) == nltk.tree.Tree:
            words.append(' '.join([w[0] for w in pos]))
        else:
            words.append(lemmatizer.lemmatize(pos[0]))

# remove stopwords
stopwords = nltk.corpus.stopwords.words('english')
words = [w for w in words if w not in stopwords]

# and calculate frequencies
freq = nltk.FreqDist(words)

# sort descending on frequency
f = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# print top words
top_words = [w for w in f if w[1] > 1]
print(top_words)

# plot 10 top words
top_words_transposed = list(zip(*top_words))
y_pos = np.arange(len(top_words_transposed[0][:10]))[::-1]

plt.barh(y_pos, top_words_transposed[1][:10], align='center', alpha=0.5)
plt.yticks(y_pos, top_words_transposed[0][:10])
plt.xlabel('Frequency')
plt.ylabel('Top words')

plt.savefig('../../Data/Chapter9/charts/word_frequency.png',
    dpi=300)