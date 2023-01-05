def disp():
    def show():
        print("show function")
    print("disp function")
    show()

disp()

#with return

def disp():
    def show():
        return "show function"
    result = show() + " Disp function"
    return result
a = disp()
print(a)

# pass a function

def disp(sh):
    print("disp function" + sh())

def show():
    return "show function"

disp(show)

#positional arguments

def pw(x , y):
    z = x**y
    print(z)

pw(2,5) 

# keyword arguments

def show(name, age):
    print(name, age)

show(name = "Geekyshows", age = 30)

# default argument
def show(name, age = 27):
    print(name, age)

show(name = "satyaprakash")

# variable length argument
# variable length argument is written with * symbol

def add(x,y):
    z = x+y
    print(z)
add(5,2)

def add(*num):
    z = num[0] + num[1] + num[2]
    print(z)
add(5,2,4)

def add(x , *num):
    z = x + num[0] + num[1]
    print(z)
add(5,2,4)

# keyword variable length argument

def add(**num):
    z = num['a'] + num['b'] + num['c']
    print(z)
add(a = 100, b = 200, c = 300)

def add(x , **num):
    z = x + num['b'] + num['c']
    print(z)
add(500, b = 200, c = 300)