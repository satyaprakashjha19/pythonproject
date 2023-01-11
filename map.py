a = [10,20,30,40,50]

def inc(n):
    return n+2

result = list(map(inc, a))
print(result)
print(type(result))
for i in result:
    print(i)


print("Using Lambda Function")
a = [10,20,30,40,50]



result = list(map(lambda n :n+2, a))
print(result)
print(type(result))
for i in result:
    print(i)