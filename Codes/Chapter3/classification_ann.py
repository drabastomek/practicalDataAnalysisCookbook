# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd 
import pybrain.datasets as dt
import pybrain.structure as st
import pybrain.supervised.trainers as tr
import pybrain.tools.shortcuts as pb
import pybrain.utilities as ut


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
        inputs_cnt / 2, 
        target_cnt,
        hiddenclass=st.TanhLayer,
        outclass=st.SoftmaxLayer,
        bias=True
    )

    # create the trainer object
    trainer = tr.BackpropTrainer(ann, data, 
        verbose=True, batchlearning=False)

    # and train the network
    trainer.trainUntilConvergence(maxEpochs=50, verbose=True, 
        continueEpochs=3, validationProportion=0.25)

    # and return the classifier
    return ann

# the file name of the dataset
r_filename = '../../Data/Chapter3/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# split the data into training and testing
train_x, train_y, \
test_x,  test_y, \
labels = hlp.split_data(
    csv_read, 
    y = 'credit_application',
    x = ['n_duration','n_euribor3m','n_age','n_emp_var_rate','n_pdays','month_mar','prev_ctc_outcome_success','n_cons_price_idx','month_apr','n_cons_conf_idx']
)

# create the ANN training and testing datasets
training = hlp.prepareANNDataset((train_x, train_y))
testing  = hlp.prepareANNDataset((test_x,  test_y))

# train the model
classifier = fitANN(training)

# classify the unseen data
predicted = classifier.activateOnDataset(testing)

# the lowest output activation gives the class
predicted = predicted.argmin(axis=1)

# print out the results
hlp.printModelSummary(test_y, predicted)