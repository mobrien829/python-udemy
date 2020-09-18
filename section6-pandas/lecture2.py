import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)
# seeds make sure we get the same rndom numbers

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)

# each column of the dataframe is a series

df['new'] = df['W'] + df['Y']
print(df)

# can use df.drop(column name, axis=1) to remove a column
# however this doesn't modify the original
# we need to set the inplace attribute to true
# do df.drop(column name, axis=1, inplace=True)
# can also be used to drop rows
