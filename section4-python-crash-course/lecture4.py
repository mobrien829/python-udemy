# function review


def times2(var):
    return var*2


# map
# format is map(function, list)

seq = [1,2,3,4,5]

print(list(map(times2, seq)))

# lambda expressions (anonymous functions): replace def with lambda, remove return

print(list(map(lambda num: num*3, seq)))

# filter returns elements that match the conditions, otherwise same usage as map

print(list(filter(lambda num: num % 2 == 0, seq)))

