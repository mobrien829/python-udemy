import pandas as pd
import numpy as np

# use .loc[index] to access a specific row
# can name indexes by using .index.names = ['name1', 'name2'...]

# to access a multilevel index: .loc[].loc[]...

# df.xs: .xs(index, level=index label)

# this can be used to go inside a multilevel index.