import numpy as np


# numpy arrays are 1d, matrices are 2d
my_list = [1, 2, 3]

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

arr = np.array(my_list)
mat = np.array(my_mat)

print(mat)

# numpy has built in generation methods for building lists and matrices

# usually this is done using :

# 1) np.arange - similar to python's range()
# np.arange(start(inc), stop(exc), step size
(np.arange(0, 11, 2))
# prints [ 0  2  4  6  8 10]

# 2) to print all zeros:
# np.zeros(indices) or np.zeros((tuple)) such that np.zeros((rows, columns))
np.zeros(3)
# prints [0, 0 ,0]
np.zeros((3,3))
# prints [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# 3) np.ones also exists, works the same as np.zeros

# 4) np.linspace(start, stop, # of pts) - np.linspace fills an array with the specified number of evenly spaced points
# ex:

print(np.linspace(0, 5, 10))
# prints [0.         0.55555556 1.11111111 1.66666667 2.22222222 2.77777778
#  3.33333333 3.88888889 4.44444444 5.        ]

# 5) identity matrix: np.eye(digit)
# identity matrices are for linear algebra: produces 2dimensional square matrix (digit = # row = # columns) and diagonal of 1s, everything else is 0s

print(np.eye(4))
# prints [[1, 0 , 0, 0], [0, 1, 0 , 0], [0, 0, 1, 0], [0, 0 , 0, 1]]

# 6) arrays of random numbers: np.random.xyzMethod

# np.random.rand(digit) produces 1 dimensional array of numbers from 0 to 1, of length digit

# np.random.rand(5, 5) creates a 2 dimensional array of 5 arrays of 5 uniformly distributed numbers 0 to 1

# to return samples from standard normal distrib or gaussian distriub:
# np.random.randn(2) gives 2 random numbers from a gaussian distribution

# np.random.randint(low, high, size) low is inclusive, high exclusive. size is # of integers

print(np.arange(25))
print(np.random.randint(0, 50, 10))

# reshape method allows us to modify our array orders/dimensions

print(np.arange(25).reshape(5, 5))

# finding max/min values:
# finding max value:
print(np.random.randint(0, 50, 10).max())
# finding min:
print(np.random.randint(0, 50, 10).min())

# using argmax() or argmin() will give the index of the max/min value

# the .shape tells us the dimensions of the vector: ex a 1 dimensional array will be the length, a 5x5 will return (5, 5)

# the .dtype method will give the datatype of the array contents