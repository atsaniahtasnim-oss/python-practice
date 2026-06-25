
#many variables can be assigned in one line
x, y, z = "Hello", "World", "!"
print(x, y, z)
print(x)
print(y)
print(z)

#one value can be assigned to multiple variables
a = b = c = "Python"
print(a)
print(b)
print(c)

#unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

cats = ["Miko", "Komeng", "Jujun"]
a, b, c = cats
print(a)
print(b)
print(c)

#unpack a string
s = "Hello!"
a, b, c, d, e, f = s
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
