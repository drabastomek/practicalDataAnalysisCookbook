import nltk

guns_laws = '../../Data/Chapter9/ST_gunLaws.txt'

with open(guns_laws, 'r') as f:
    article = f.read()

# print(article)

# load sentence tokenizer
sentencer = nl.data.load('tokenizers/punkt/english.pickle')

sentences = sentencer.tokenize(article)

tokenizer = nltk.StanfordTokenizer()

for sentence in sentences[1:5]:
    print(sentence, '\n')