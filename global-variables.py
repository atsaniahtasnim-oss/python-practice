

# A variable created outside of a function is known as a global variable and can be used by anyone, both inside of functions and outside.
x = "Tasnim"

def myfunc():
    print("My name is " + x)

myfunc()

# A variable created inside a function is known as a local variable and can only be used inside that function.
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()

print("Python is " + x)

# To create a global variable inside a function, you can use the global keyword. If you use the global keyword, the variable belongs to the global scope.
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword, and then assign a new value to it.
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)



