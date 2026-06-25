#Escape cHaracters in a string
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#single quote
txt = 'It\'s alright.'
print(txt) #This example uses a backslash to escape the single quote, allowing it to be included in the string without causing an error.

#backslash
txt = "This will insert one \\ (backslash)."
print(txt) #This example inserts a backslash in the string by using two backslashes.

#New Line
txt = "Hello\nWorld!"
print(txt) #This example inserts a new line between Hello and World!

#Carriage Return
txt = "Hello\rWorld!"
print(txt) #This example returns the cursor to the beginning of the line, so "World!" will overwrite "Hello". The result will be "World!".

#Tab
txt = "Hello\tWorld!"
print(txt) #This example inserts a tab between Hello and World!

#Backspace
txt = "Hello\bWorld!"
print(txt) #This example erases one character (backspace) between Hello and World!

#Form Feed
txt = "Hello\fWorld!"
print(txt) #This example inserts a form feed between Hello and World!

#Octal value
txt = "\110\145\154\154\157"
print(txt) #This example uses octal values to represent the characters in "Hello". Each set of three octal digits corresponds to a character in the string.

#Hex value
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) #This example uses hexadecimal values to represent the characters in "Hello". Each pair of hexadecimal digits corresponds to a character in the string.