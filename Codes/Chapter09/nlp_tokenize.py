import nltk

# read the text
guns_laws = '../../Data/Chapter09/ST_gunLaws.txt'

with open(guns_laws, 'r') as f:
    article = f.read()

# load NLTK modules
sentencer = nltk.data.load('tokenizers/punkt/english.pickle')
tokenizer = nltk.RegexpTokenizer(r'\w+')
stemmer = nltk.PorterStemmer()
lemmatizer = nltk.WordNetLemmatizer()

# split the text into sentences
sentences = sentencer.tokenize(article)

words = []
stemmed_words = []
lemmatized_words = []

# and for each sentence
for sentence in sentences:
    # split the sentence into words
    words.append(tokenizer.tokenize(sentence))

    # stemm the words
    stemmed_words.append([stemmer.stem(word) 
        for word in words[-1]])

    # and lemmatize them
    lemmatized_words.append([lemmatizer.lemmatize(word) 
        for word in words[-1]])

# and save the results to files
file_words  = '../../Data/Chapter09/ST_gunLaws_words.txt'
file_stems  = '../../Data/Chapter09/ST_gunLaws_stems.txt'
file_lemmas = '../../Data/Chapter09/ST_gunLaws_lemmas.txt'

with open(file_words, 'w') as f:
    for w in words:
        for word in w:
            f.write(word + '\n')

with open(file_stems, 'w') as f:
    for w in stemmed_words:
        for word in w:
            f.write(word + '\n')

with open(file_lemmas, 'w') as f:
    for w in lemmatized_words:
        for word in w:
            f.write(word + '\n')