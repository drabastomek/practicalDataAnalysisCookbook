import nltk

def print_tree(tree, filename):
    '''
        A method to save the parsed NLTK tree to a PS file
    '''
    # create the canvas
    canvasFrame = nltk.draw.util.CanvasFrame()

    # create tree widget
    widget = nltk.draw.TreeWidget(canvasFrame.canvas(), tree)

    # add the widget to canvas
    canvasFrame.add_widget(widget, 10, 10)

    # save the file
    canvasFrame.print_to_file(filename)

    # release the object
    canvasFrame.destroy()

# two sentences from the article
sentences = ['Washington state voters last fall passed Initiative 594', 'The White House also said it planned to ask Congress for $500 million to improve mental health care, and Obama issued a memorandum directing federal agencies to conduct or sponsor research into smart gun technology that reduces the risk of accidental gun discharges.']

# the simplest possible word tokenizer
sentences = [s.split() for s in sentences]

# part-of-speech tagging
sentences = [nltk.pos_tag(s) for s in sentences]

# pattern for recognizing structures of the sentence
pattern = '''
  NP: {<DT|JJ|NN.*|CD>+}   # Chunk sequences of DT, JJ, NN
  VP: {<VB.*><NP|PP>+}     # Chunk verbs and their arguments
  PP: {<IN><NP>}           # Chunk prepositions followed by NP
'''

# identify the chunks
NPChunker = nltk.RegexpParser(pattern)
chunks = [NPChunker.parse(s) for s in sentences]

# save to file
print_tree(chunks[0], '../../Data/Chapter9/charts/sent1.ps')
print_tree(chunks[1], '../../Data/Chapter9/charts/sent2.ps')