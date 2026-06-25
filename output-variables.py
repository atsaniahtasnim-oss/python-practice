# Output Variables
x = "Python is awesome!"
print(x)

x = "Python"
y = "is"
z = "awesome!"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome!"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)  # This will print the integer and the string separated by a space.
'''
x = 5
y = "John"
print(x + y)  # This will raise a TypeError because you cannot add an integer and a string together.
'''
x = 5
y = "John"
print(str(x) + y)  # This will convert the integer to a string and then concatenate it with the other string.
