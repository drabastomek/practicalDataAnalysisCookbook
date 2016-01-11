import nltk

def print_tree(tree, filename):
    '''
        A method to save the parsed NLTK tree to a PS file
    '''
    # create the canvas
    cf = nltk.draw.util.CanvasFrame()

    # create tree widget
    tc = nltk.draw.TreeWidget(cf.canvas(), tree)

    # add the widget to canvas
    cf.add_widget(tc, 10, 10)

    # save the file
    cf.print_to_file(filename)

    # release the object
    cf.destroy()

# two sentences from the article
sentences = ['Washington state voters last fall passed Initiative 594', 'The White House also said it planned to ask Congress for $500 million to improve mental health care, and Obama issued a memorandum directing federal agencies to conduct or sponsor research into smart gun technology that reduces the risk of accidental gun discharges.']

# the simplest possible word tokeniser
sentences = [s.split() for s in sentences]

# part-of-speech tagging
sentences = [nltk.pos_tag(s) for s in sentences]

# pattern for recognizing structures of the sentence
pattern = '''
  NP: {<DT|JJ|NN.*|CD>+}   # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}           # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP>+}     # Chunk verbs and their arguments
'''

# identify the chunks
NPChunker = nltk.RegexpParser(pattern)
chunks = [NPChunker.parse(s) for s in sentences]

# save to file
print_tree(chunks[0], '../../Data/Chapter9/charts/sent1.ps')
print_tree(chunks[1], '../../Data/Chapter9/charts/sent2.ps')