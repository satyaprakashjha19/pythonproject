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