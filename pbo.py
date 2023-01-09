# pass by object

def val(lst):
    print("IFBA:", lst, id(lst))
    lst.append(4)
    print("IFAA:", lst, id(lst))

lst = [1,2,3]
print("BCF:", lst, id(lst))
val(lst)
print("ACF:", lst, id(lst))

# Passing array to function

from array import *
def show(ar):
    print(ar)
    print(type(ar))
    for i in ar:
        print(i)

a = array('i', [101,102,103,104])
show(a)

# returnig array from function

from array import *
def show(ar):
    print("Passed array ar: ", ar)
    print(type(ar))
    for i in ar:
        print(i)
    return ar

a = array('i', [10,11,12,13])
y = show(a)
print("Returning array Y :", y)
print(type(y))
for i in y:
    print(i)

# Create empty list using list function

a = list("Geekyshows")
print(a)
print(type(a))

a = list(range(0,5))
print(a)
print(type(a))