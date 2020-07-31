import numpy as np

arr = np.arange(0, 11)

print(arr)

# we can use simple operators to operate on arrays

print(arr+arr)
print(arr-arr)
print(arr*arr)

# scalars are a single number that numpy broadcasts

print(arr + 100)

# to square root:

print(np.sqrt(arr))

# to calculate exponential:

print(np/exp(arr))

# for min/max:
print(arr.max())
print(arr.min())

# trig:
print(np.sin(arr))

# log:
print(np.log(arr))

# find ufunc for numpy operations cmd+f math functions

