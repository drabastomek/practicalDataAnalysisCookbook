import json

# path to the training json file
train_path = '../../Data/Chapter9/train.json'

# open and read the contents of the file
with open(train_path, 'r') as f:
    read = f.read()

# parse to json
parsed = json.loads(read)

# and print the first review
print(parsed[0])