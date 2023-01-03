# return statement single value
def add(y):
    x = 10
    return x + y

# calling a function

sum = add(50)
print(sum)

# multiple value

def add(y):
    x = 10
    a = x + y
    b = y - x
    return a , b

sum, sub = add(20)
print(sum,sub)
