import json

# read the data
with open('../../Data/Chapter1/realEstate_trans.json', 'r') \
    as json_file:
        json_read = json.loads(json_file.read())

# print the last 10 records
print(json_read[-10:])

# write back to the file
with open('../../Data/Chapter1/realEstate_trans.json', 'w') \
    as json_file:
        json_file.write(json.dumps(json_read))
