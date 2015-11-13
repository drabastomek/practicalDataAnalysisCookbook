# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd 
import numpy as np
import pybrain.structure as st
import pybrain.supervised.trainers as tr
import pybrain.tools.shortcuts as pb

@hlp.timeit
def fitANN(data):
    '''
        Build a neural network classifier
    '''
    # determine the number of inputs and outputs
    inputs_cnt = data['input'].shape[1]
    target_cnt = data['target'].shape[1]

    # create the classifier object
    ann = pb.buildNetwork(inputs_cnt, 
        inputs_cnt * 10,
        inputs_cnt * 10,
        inputs_cnt,
        target_cnt,
        hiddenclass=st.TanhLayer,
        outclass=st.LinearLayer,
        bias=True
    )

    # create the trainer object
    trainer = tr.BackpropTrainer(ann, data, 
        verbose=True, batchlearning=False)

    # trainer.train()
    # and train the network
    trainer.trainUntilConvergence(maxEpochs=50, verbose=True, 
        continueEpochs=2, validationProportion=0.25)

    # and return the classifier
    return ann

# the file name of the dataset
r_filename = '../../Data/Chapter6/power_plant_dataset_pc.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# keep only principal components
independent_reduced = [
    col 
    for col 
    in csv_read.columns 
    if col.startswith('p')
]

csv_read = csv_read[independent_reduced + 
    ['net_generation_MWh']]

# split the data into training and testing
train_x, train_y, \
test_x,  test_y, \
labels = hlp.split_data(csv_read, y='net_generation_MWh')

# create the ANN training and testing datasets
training = hlp.prepareANNDataset((train_x, train_y), 
    prob='regression')
testing  = hlp.prepareANNDataset((test_x, test_y),
    prob='regression')

# train the model
classifier = fitANN(training)

# classify the unseen data
predicted = classifier.activateOnDataset(testing)

# and calculate the R^2
score = hlp.get_score(test_y, predicted[:, 0])
print(score)