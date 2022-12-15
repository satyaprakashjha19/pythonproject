def function1():
    print("ahhh")
    print("ahhhh2")
print("this is outside the function")

function1()

# mapping

def function2(x):
    return 2*x

a = function2(3)
b = function2(5)

print(a)
print(b)

def function3(x ,y):
    return x + y
e = function3(1,2)
print(e)

# function
# user defind function
#write once and use as many times you need

def add():
    x = 10
    y = 20
    c = x + y
    print(c)
add()   

def disp():
    name = "satyaprakash"
    print(name)

disp()

# Divide large task in to many small task
# separate function for addition
def add():
    x = 10
    y = 50
    c = x + y
    print(c)
add()

# separate function for subtraction
def sub():
    x = 10
    y = 50
    c = y - x
    print(c)
sub()

def add():
    x = 10
    y = 50
    c = x + y
    z = y + x + 100
    print(c,z)
add()

# function without parameter and argument

def add():
    a = 10
    b = 20
    c = a + b
    print(c)

add()   # calling without argument

# function withparameter and argument

def add(b):
    a = 100
    c = a + b
    print(c)
# calling with argument

add(500)

# return statement

def add(y):
    x = 10
    return x + y
sum = add(50)
print(sum)

def add_sub(y):
    x = 10
    c = x + y
    d = y - x
    return c , d
sum , sub = add_sub(20)
print(sum)
print(sub)

# nested function

def disp():
    def show():
        print("show function")
    print("disp function")
    show()
disp()