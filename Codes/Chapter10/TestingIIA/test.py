import pandas as pd

read = pd.read_csv('../../../Data/Chapter10/choices.dat', delimiter='\t')

# print(read.head())
cols = list(read.columns)[1:17]

# print(cols)

for i, col in enumerate(cols):
    choice = read[read.choice == i + 1]
    print(i, col, choice[choice[col] == 0])
