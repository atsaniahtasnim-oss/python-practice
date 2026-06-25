#Upper and lower case
a = "Hello, World!"
print(a.upper())
print(a.lower())

#Remove whitespace
a = " Hello, World! "
print(a) #returns " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace Strings
a = "Hello, World!"
print(a.replace("H", "J")) # returns "Jello, World!"
print(a.replace("H", "M")) # returns "Mello, World!"

#Split Strings
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
b = "apple,banana,cherry"
print(b.split(",")) # returns ['apple', 'banana', 'cherry']
c = "one;two;three"
print(c.split(";")) # returns ['one', 'two', 'three']
d = "John Doe"
print(d.split()) # returns ['John', 'Doe']

