# lambda function
a = lambda x : x + 10
print(a(5))

add = lambda x,y : x + y
print(add(5,2))

add_sub = lambda x , y : (x+y, x-y)
a,s = add_sub(5,2)
print(a)
print(s)

add = lambda x,y=3 : x + y
print(add(5))

x = lambda a , b , c : a + b + c
print(x(10,20,30))

#Nested lambda function

add = lambda x = 10: (lambda y : x + y)
a = add()
print(a(20))