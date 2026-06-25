#F-Strings
age = 36
name = "John"
txt = f"My name is {name} and I am {age} years old."
print(txt) # returns "My name is John and I am 36 years old."

#Placeholders
price = "59"
txt = f"The price is {price} dollars"
print(txt) # returns "The price is 59 dollars"

#Placeholders and modifiers
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) # returns "The price is 59.00 dollars"

txt = f"The price is {20*59} dollars"
print(txt) # returns "The price is 1180 dollars"

txt = f"The price is {20*59:.2f} dollars"
print(txt) # returns "The price is 1180.00 dollars"