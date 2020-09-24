import numpy as np
import pandas as pd

# we can create dataframes from dictionaries, just like we can create series

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}

df = pd.DataFrame(d)
print(df)

# we can use .dropna() to drop any NaN values
# we can use axis and inplace here as well to manipulate rows/columns
# the thresh value is how many non-NA values are required to show a row

print(df.dropna())

# if we want to fill in Na values, we can use .fillna()
# the value argument is what we use to fill the Na
# ex:

print(df['A'].fillna(value=df['A'].mean()))
