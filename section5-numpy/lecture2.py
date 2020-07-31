# numpy indexing and selection

import numpy as np
arr = np.arange(1,11)
print(arr)
print(arr[1:5])

# numpy arrays are different from python lists because they can broadcast
# that means that you can do something like this:
# arr[0:5] = 100
# arr will now print [100, 100, 100, 100, 100, 5, 6, 7, 8, 9]
# this means that when you slice from arrays, you are viewing the data from the original array, rather than copying it
# this means that any mutations to sliced data will be copied over to the original data

# to prevent this:
arr_copy = arr.copy()

# now we have a secondary copy of the array to mutate without modifying the original

# we can access a matrix using either single bracket notation (arr[index1, index2]) or double bracket (arr[index1][index2])

arr_2d = np.arange(5, 50, 5).reshape(3, 3)
print(arr_2d)
print(arr_2d[0, 2])
print(arr_2d[1][2])

# to access a submatrix:

print(arr_2d[:2, 1:])

# this will return a matrix of everything up to index 2 of the first array (row 2), then everything from column 1 onwards

# to create an array of boolean values:

print(np.arange(1,11) > 5)

# using a comparison operator on an array will create an array of booleans. using this boolean array as the index for the original array will then only return elements that evaluated to true

bool_arr = arr > 5

print(arr[bool_arr])
# or as one liner:
print(arr[arr > 5])

