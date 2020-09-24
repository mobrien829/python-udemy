import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

# we can evaluate by using operators on a dataframe

# booldf = df > 0

# print(df[booldf])
# print(df[df['W'] > 0])
# print(df > 0)

# print(df[df['0']<0])

# to set multiple conditions with pandas, use & rather than "and"
# use the pipe operator (|) rather than "or"

# resetting/changing an index:
# have to use the inplace=true option in order to mutate the dataframe
print(df.reset_index())

newind = ' CA NY WY OR CO'.split()
df['States'] = newind
print(df)
df.drop("States", axis=1, inplace=True)
print(df)

# we can use .set_index(index name, or blank) to move a column to become an index rather than a column of datapoints

