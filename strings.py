#Strings are a sequence of characters. They can be enclosed in single quotes (' ') or double quotes (" ").
print("Hello")
print('Hello')

#Quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assign Strings to a variable
a = "Hello"
print(a)

#Multiline Strings
#To create a multiline string, use three quotes (''' or """).
a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a='''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are arrays
a = "Hello, World!"
print(a[1]) #prints the second character of the string
print(a[0]) #prints the first character of the string
print(a[7]) #prints the eighth character of the string

#Looping through a string
for x in "banana":
  print(x)

for z in "cherry":
    print(z)

#String Length
a = "Hello, World!"
print(len(a)) #prints the length of the string
b = "Mississippi"
print(len(b)) #prints the length of the string

#Check String
txt = "The best things in life are free!"
print("free" in txt) #returns True if "free" is found in the string
print("expensive" in txt) #returns False if "expensive" is not found
print("not free" in txt) #returns False if "not free" is not found
#using if statement
txt = "The best things in life are free!"
if "free" in txt:
   print("Yes, 'free' is present.")
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt) #returns True if "expensive" is NOT found in the string
#using if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
   print("No, 'expensive' is NOT present.")

a = "Tasnim"
print(a[0:3]) #prints the first three characters of the string
txt = "Tasnim"
x = txt[0] #gets the first character of the string
print (x)