import numpy as np

import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

# can use Series() to list data by labels

print(pd.Series(data=my_data, index=labels))
print(pd.Series(d))

# .Series can take data in the form of a list, a numpy array, or a dictionary

print(pd.Series(data=labels))

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
ser2 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'Italy', 'Japan'])

print(ser1['USA'])