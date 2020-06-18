out = []
for num in range(5):
    print(num)
    out.append(num)
print(out)

out = [num ** 2 for num in range(5)]
print(out)


# functions

def my_function(name='DefaultName'):
    print('Hello ' + name)


my_function("Michael")
my_function()


def square(num):
    """
    THIS IS A DOC STRING THAT CAN GO MULTIPLE LINES LOL YOLO
    THIS FUNCTION SQUARES A NUMBER
    """
    return num**2


print(square.__doc__)
output = square(2)
print(output)
