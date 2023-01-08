x = [10,20,30,40,50,60,70,80,90,100]
print("Original list")
n = len(x)
for i in range(n):
    print(i, "=", x[i])

print()

print("from 1st position to 4rt position")

a = x[1:5]
for i in a:
    print(i)

print("from 0 to last position")

a = x[0:]
for i in a:
    print(i)

print("last 4 elements")

d = x[-4:]
for i in d:
    print(i)

print("From 0 to 6th position and stepsize 2")

s = x[0:7:2]
for i in s:
    print(i)