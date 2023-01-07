#IIFE( Immediately Invoked Function Expressions )
(lambda x : print(x + 1))(5)

(lambda x, y : print(x + y))(5,2)

# Global variable

a = 50
def show():
    x = 10
    print(x)
    print(a)
    
show()

# recursion

def myfun():
    print("geekyshows")
    myfun()

myfun()